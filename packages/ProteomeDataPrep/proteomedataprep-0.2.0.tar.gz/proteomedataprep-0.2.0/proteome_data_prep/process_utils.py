import re
import pandas as pd
from dataclasses import dataclass, field
import json
import os
import pkg_resources
from typing import Optional, List, Dict, Union
import numpy as np
from .data_loader import DataLoader
from .data_container import DataContainer

from .data_utils import *

pd.options.mode.chained_assignment = None


@dataclass
class Processor:

    dropna_percent_threshold: float = 50

    label_screens: bool = False
    screen_split: Dict[Union[tuple, str], str] = field(default_factory= 
                               # MSR numbers by which to split screens
                               lambda: {(0, 5863): "THP-1 1K",  
                               (5863, 1e16): "Anborn"})
    ignore_missing_ranges: bool = False
    label_tfs: bool = True
    tf_list: Optional[List[str]] = None
    gene_info_by_acc: Optional[Dict] = None


    def __post_init__(self):
        if self.label_screens:
            if self.screen_split is None:
                raise ValueError("Provide a dictionary to label screens.")
            if not self.ignore_missing_ranges:
                missing_ranges = self._check_missing_ranges()
                if len(missing_ranges) > 0:
                    raise ValueError(f"Missing MSR numbers in screen" \
                                     " dictionary.\nUnable to label MSR" \
                                     " numbers in range(s) {missing_ranges}.\n"
                                     "To ignore missing ranges, " \
                                     "set ignore_missing_ranges=True. Invalid "\
                                      "screen numbers will be labeled 'NaN'."
                                    ) 
        if self.dropna_percent_threshold <= 1.0:
            raise Warning(f"dropna_percent_threshold is a percent. " \
                          "Not a portion. Passing a value of 1 or less will " \
                          "exlude columns unless they are 99%+ not NaN.")
        
        self.tf_list = self.load_tf_list()
    
    def process_and_normalize(
            self, data_container: DataContainer,
            normalize_abundance: bool=True,
            label_tfs: bool=False,
            label_screens: bool=False,
            keep_filename: bool=False
            ) -> DataContainer:

        log_df = self.log_transform(data_container.raw_df)

        if label_tfs:
            log_df = self.label_tfs
        
        normalized_df = self.median_normalize_df(
            log_df, 
            normalize_abundance=normalize_abundance
        )

        if label_screens:
            normalized_df["screen"] = normalized_df.apply(self._get_screen)
        
        normalized_df["Compound"] = normalized_df["Filename"].apply(
            self.get_compound_name
        )

        if not keep_filename:
            normalized_df = normalized_df.drop(columns=["Filename"])

        data_container.normalized_df = normalized_df

        return data_container

    
    def log_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        quant_cols = get_quant_columns(df)

        id_cols = detect_id_columns(df)
        
        # Replace 0 and None with np.nan across the selected columns
        df_safe = df[quant_cols].replace(
            {0: np.nan, None: np.nan}
            ).astype(float)
        log_df = np.log(df_safe)

        log_df = pd.concat([df[id_cols], log_df], axis=1)

        log_df = self._drop_nan_cols(log_df)

        return log_df

    def median_normalize_df(self, 
                            log_df: pd.DataFrame, 
                            normalize_abundance: bool=True
                            ) -> pd.DataFrame:
        quant_cols = get_quant_columns(log_df)

        non_empty_cols = log_df[
            quant_cols].columns[log_df[quant_cols].notna().any()
        ]
        
        # Calculate the overall median for non-empty columns only
        overall_median = log_df[non_empty_cols].median().median()
        
        # Normalize by subtracting the median for each column
        log_df[non_empty_cols] = (
            log_df[non_empty_cols] - log_df[non_empty_cols].median()
        )

        # Melt to get a single abundance column, drop nans
        melted_df = self.melt_df(log_df)
        melted_df.dropna(inplace=True)

        # Add back in overall median so log abundance values are
        # more "realistic"
        if normalize_abundance:
            melted_df["Normalized Abundance"] = (
                melted_df["Abundance"] + overall_median
            )
   
        return melted_df
    
    def melt_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """Melt a dataframe with mass spec runs as columns so that new 
        dataframe has "Filename" and "Abundance" as columns
        in addition to the ID columns.

        Args:
            raw_df (pd.DataFrame): Dataframe from diann or encyclopedia with 
            mass spec runs as columns

        Returns:
            pd.DataFrame: Melted dataframe with mass spec filenames as rows.
        """
        # Restructure df so columns are peptides
        id_vars = detect_id_columns(df)    
        melt_df = df.melt(id_vars=id_vars, # Melt so filename is col.
                        var_name="Filename",
                        value_name="Abundance")
        return melt_df


    def _drop_nan_cols(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Drop columns from the DataFrame that exceed a specified percentage 
        of NaN values.

        Parameters:
        df (pandas.DataFrame): The input DataFrame from which columns with 
                            too many NaN values will be dropped.

        Returns:
        pandas.DataFrame: The input DataFrame with columns dropped based 
                        on the NaN percentage threshold.
        """
        # Calculate the percentage of NaN values for each column
        nan_percentage = df.isnull().sum() * 100 / len(df)
        
        # Identify columns to drop
        cols_to_drop = nan_percentage[
            nan_percentage >= self.dropna_percent_threshold
        ].index
        
        df = df.drop(columns=cols_to_drop)
        
        return df

    def load_tf_list(self) -> List[str]:
        """
        Load transcription factors from a JSON file and return a list of 
        keys.

        Returns:
        List[str]: A list of transcription factor keys from the JSON file.
        """
        tf_path = pkg_resources.resource_filename(
            'proteome_data_prep',
            'data/acc_by_tf_gene.json'
        )
        
        try:
            with open(tf_path, 'r') as file:
                acc_by_tf_gene = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {tf_path} was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from the file {tf_path}.")
        
        return list(acc_by_tf_gene.keys())


    @staticmethod
    def load_gene_info():
        gene_info_path = pkg_resources \
            .resource_filename('proteome_data_prep',
                                'data/gene_info_by_acc.json')
        with open(gene_info_path, 'r') as file:
            return json.load(file)
        
    def _is_tf(self, gene):
        gene_list = gene.split(';')
        return any(gene in self.tf_list for gene in gene_list)

    def label_tfs(self, df):
        df["Is TF"] = df["Genes"].apply(self._is_tf)
        return df

    def get_compound_name(self, s: str) -> str:
        """
        Extracts the compound name from the name of the file.
    
        Parameters
        ----------
        s: str
            An entry from the "Filename" column, a path to where 
            the file is located
        
        Returns
        -------
        str
            The name of the treatment compound
        """
        # Look for compounds with the name TAL####
        if "TAL" in s.upper():
            tal_num = re.search(r'TAL\d+(-\d+)?', s)[0]
            # Strip leading zeros if present
            num = int(re.search(r'\d+(-\d+)?', tal_num)[0])
            new_name = "TAL" + str(num)
            return new_name
        elif "DMSO" in s.upper():
            return "DMSO"
        elif "PRTC" in s.upper():
            return "PRTC"
        elif "nuclei" in s.lower():
            return "NUC"
        elif "nuc" in s.lower(): # cases where it is labeled as NUC2
            nuc_num = re.search(r'NUC\d+(-\d+)?', s)
            if nuc_num is None:
                return "NUC"
            else:
                return nuc_num[0]
        elif "dbet" in s.lower():
            return "dBET6"
        elif "FRA" in s.upper():
            return "FRA"
        elif "none" in s.lower():
            return "None"
        else:
            raise Exception(f"Unable to extract compound from filename {s}.")
    
    def _get_screen(self, msr_str):
        if msr_str.startswith("MSR"):
            try:        
                msr = re.search(r'MSR\d+(-\d+)?', msr_str)[0]
            except:
                raise ValueError(f"Unable to match MSR for filename {msr_str}.")
            
            msr = int(re.search(r'\d+(-\d+)?', msr)[0])
        
            for msr_range, screen_name in self.screen_split.items():
                if isinstance(msr_range, tuple):
                    if msr_range[0] <= msr < msr_range[1]:
                        return screen_name
            raise ValueError(f"Unable to determine screen for MSR {str(msr)}.")
        else:
            screen_name = msr_str.split("_")[0]
            try:
                screen = self.screen_split[screen_name]
            except KeyError:
                raise KeyError(f"Screen name {screen_name} not in screen_dict.")
            return screen

    @staticmethod
    def convert_encyclopedia_file(data_container):
        gene_info_by_acc = Processor.load_gene_info()
        # Take an encyclopedia file and convert it to look like a diann file
        rename_dict = {"Peptide": "Precursor.Id",
                       "Protein": "Protein.Ids"}
        df = data_container.raw_df 
        df = df.rename(columns=rename_dict)
        df[["Genes", "Protein.Ids"]] = (
            df["Protein.Ids"].apply(
                lambda x: Processor._extract_gene_info(x, gene_info_by_acc)
            ))
        data_container.raw_df = df
        data_container.filetype = "diann"
        return data_container
    
    @staticmethod
    def _extract_gene_info(protein_ids, gene_info_by_acc):
        protein_list = protein_ids.split(';')

        gene_ids = set() 
        clean_proteins = [] 
        
        for protein in protein_list:
            if '|' in protein:
                protein_id = protein.split('|')[1]
            else:
                protein_id = protein
                
            base_protein_id = protein_id.split('-')[0]

            base_protein_id = protein_id.split('-')[0]
            gene_info = gene_info_by_acc.get(base_protein_id, {})
            gene_name = gene_info.get('id', 'Unknown')
            if gene_name is None:
                gene_name = "None"

            gene_ids.add(gene_name)
            clean_proteins.append(protein_id)
        
        genes = ';'.join(sorted(gene_ids))
        return pd.Series([genes, ';'.join(clean_proteins)])

    # @staticmethod
    # def drop_controls(self, df: pd.DataFrame,
    #                   control_compounds: List[str]=None,
    #                   control_genes: List[str]=None) -> pd.DataFrame:
    #     control_g
