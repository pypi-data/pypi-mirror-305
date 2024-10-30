import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional, Tuple

def get_control_peptide(melted_df: pd.DataFrame) -> str:
    """
    Identify the control peptide with the highest score to serve as a control
    against which to compare relative abundances

    Parameters:
    melted_df (DataFrame): Data with 'Precursor.Id' and 'Abundance' columns.

    Returns:
    str: The peptide ID with the highest Z-score, excluding cysteine peptides.
    """
   # Calculate mean abundance and standard deviation for each peptide
    mean_df = melted_df.groupby("Precursor.Id")["Abundance"].mean().to_frame()
    mean_df["STD"] = melted_df.groupby("Precursor.Id")["Abundance"].std()
    mean_df = mean_df.reset_index()

    # Get rid of any peptides that contain cysteine
    mean_df = mean_df[~mean_df["Precursor.Id"].str.contains("C")]
    if mean_df.empty:
        raise ValueError("No suitable control peptides found")

    # Calculate the Z scores
    overall_mean = mean_df["Abundance"].mean()
    mean_df["Z Score"] = (mean_df["Abundance"] - overall_mean) / mean_df["STD"]

    # Get the peptide with the highest Z Score
    control_peptide = mean_df.loc[
        mean_df["Z Score"] == mean_df["Z Score"].max(), "Precursor.Id"
    ].iloc[0]
    
    return control_peptide

def subset_dataframe(
        melted_df: pd.DataFrame, precursors: List[str]
        ) -> pd.DataFrame:
    """
    Subset the DataFrame to only include specified precursors.

    Parameters:
    melted_df (pd.DataFrame): DataFrame containing 'Precursor.Id', 'Abundance',
                              and 'Compound' columns.
    precursors (List[str]): List of precursor IDs to subset by.

    Returns:
    pd.DataFrame: Subsetted DataFrame with only specified precursors.
    """
    # Subset for only the required columns
    df = melted_df[['Precursor.Id', 'Abundance', 'Compound']]

    # Further subset for control and test peptides
    df = df[df['Precursor.Id'].isin(precursors)]
    
    return df


def aggregate_pivot(
        melted_df: pd.DataFrame, control_precursor: str
        ) -> pd.DataFrame:
    """
    Aggregate and pivot DataFrame, separating control and test peptides.
    Label replicate peptides with numbers

    Parameters:
    melted_df (pd.DataFrame): DataFrame with 'Precursor.Id', 'Compound', and
                              'Abundance' columns.
    control_precursor (str): ID of the control precursor to aggregate separately.

    Returns:
    pd.DataFrame: Aggregated DataFrame with pivoted peptide data.
    """
    # Get the mean of any control precursor replicates
    aggregate_df = (
        melted_df[melted_df['Precursor.Id'] == control_precursor]
        .groupby('Compound')['Abundance']
        .mean()
        .reset_index()
    )
    aggregate_df.rename(
        columns={'Abundance': f'{control_precursor}'}, inplace=True
        )

    # Number other replicates and pivot
    remaining_df = melted_df[
        melted_df['Precursor.Id'] != control_precursor
        ].copy()
    remaining_df['Duplicate_ID'] = (
        remaining_df.groupby(['Compound', 'Precursor.Id'])
        .cumcount() + 1
    )
    pivot_df = remaining_df.pivot(
        index='Compound', columns=['Precursor.Id', 'Duplicate_ID'],
        values='Abundance'
    )

    # Flatten column names
    pivot_df.columns = [f"{col[0]}_{col[1]}" for col in pivot_df.columns]
    pivot_df = pivot_df.reset_index()

    # Merge the control peptide dataframe with others
    final_df = pd.merge(aggregate_df, pivot_df, on='Compound', how='left')

    # Drop columns that are more than 50% NaN
    final_df.dropna(thresh=len(final_df) / 2, axis=1, inplace=True)

    return final_df



def scale_series(series: pd.Series) -> pd.Series:
    """
    Scale a series to a specified range with a target mean.

    Parameters:
    series (pd.Series): Series to scale.

    Returns:
    pd.Series: Scaled series with values in the specified range.
    """
    new_min = 0.00001
    new_mean = 0.5
    new_max = 1

    # Normalize series to [0, 1]
    normalized = (series - series.min()) / (series.max() - series.min())

    # Calculate scaling factor to adjust the mean
    scaling_factor = (new_mean - new_min) / normalized.mean()
    scaled = normalized * scaling_factor

    # Adjust to new min and max
    scaled = scaled * (new_max - new_min) + new_min

    # Replace infinities with NaN
    scaled = scaled.replace([np.inf, -np.inf], np.nan)

    return scaled

def normalize(df: pd.DataFrame, control_peptide: str) -> pd.DataFrame:
    """
    Normalize a DataFrame to a specified control peptide.

    Parameters:
    df (pd.DataFrame): DataFrame with 'Compound' column and peptide abundance
                       columns.
    control_peptide (str): Name of the control peptide column to normalize by.

    Returns:
    pd.DataFrame: Normalized DataFrame with values scaled and divided by the
                  control peptide.
    """
    # Select numeric columns (excluding 'Compound')
    numeric_columns = df.columns[1:]

    # Scale to [0, 1]
    df[numeric_columns] = df[numeric_columns].apply(scale_series)

    # Normalize to control peptide
    df[numeric_columns] = df[numeric_columns].div(df[control_peptide], axis=0)

    # Drop rows where all values (excluding 'Compound') are NaN
    df = df.dropna(
        how='all', 
        subset=[col for col in df.columns if col != 'Compound']
        )

    return df

def aggregate_reps(df: pd.DataFrame, control_peptide: str) -> pd.DataFrame:
    """
    Calculate mean and standard deviation across replicates for each peptide.

    Parameters:
    df (pd.DataFrame): DataFrame with peptide abundance columns and a 'Compound'
                       column.
    control_peptide (str): Name of the control peptide to exclude from 
                           aggregation.

    Returns:
    pd.DataFrame: DataFrame with added mean and std columns for each peptide.
    """
    # Identify peptide prefixes, excluding control and 'Compound' columns
    prefixes = set(
        col.split('_')[0]
        for col in df.columns
        if col not in ["Compound", control_peptide]
    )

    # For each peptide, calculate mean and std across replicate columns
    for prefix in prefixes:
        prefix_columns = [col for col in df.columns if col.startswith(prefix)]
        
        # Calculate mean, ignoring NaNs
        df[f'{prefix}_mean'] = df[prefix_columns].mean(axis=1, skipna=True)
        
        # Calculate std and set to NaN if all replicates are NaN
        std_series = df[prefix_columns].std(axis=1, skipna=True)
        std_series[df[prefix_columns].isna().all(axis=1)] = float('nan')
        df[f'{prefix}_std'] = std_series

    return df


def drop_max_compound(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop the row containing the compound with the maximum mean value.

    Parameters:
    df (pd.DataFrame): DataFrame with a 'Compound' column and other columns
                       ending in 'mean'.

    Returns:
    pd.DataFrame: DataFrame with the row containing the max mean compound
                  removed.
    """
    # Identify columns of interest ending in 'mean'
    columns_of_interest = [col for col in df.columns if col.endswith("mean")]

    # Check if columns_of_interest is empty or if all values are NaN
    if not columns_of_interest or df[columns_of_interest].isna().all().all():
        raise ValueError("No valid 'mean' columns to evaluate for max value.")


    # Find index of the row with the highest mean value across columns
    idx = df[columns_of_interest].max(axis=1).idxmax()
    compound = df.loc[idx, "Compound"]

    # Drop the row with this compound
    df = df.loc[df["Compound"] != compound]

    return df

def get_relative_abundance(melted_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate relative abundance for a single gene by normalizing peptide data.

    Parameters:
    melted_df (pd.DataFrame): DataFrame with columns 'Genes', 'Precursor.Id',
                              'Abundance', and 'Compound'.

    Returns:
    pd.DataFrame: DataFrame with relative abundances normalized to a control
                  peptide, with the maximum compound row removed.
    
    Raises:
    ValueError: If more than one unique gene is found in the DataFrame.
    """
    # Ensure only one gene is present
    if melted_df["Genes"].nunique() > 1:
        raise ValueError("Relative abundance can only be calculated for one "
                         "gene at a time.")
    
    # Identify control and cysteine-containing precursors
    control_precursor = get_control_peptide(melted_df)
    cysteine_precursor = [pep for pep in melted_df["Precursor.Id"].unique()
                          if "C" in pep]
    if len(cysteine_precursor) == 0:
        raise ValueError("No cysteine peptides found.")
    precursor_list = cysteine_precursor + [control_precursor]
    
    # Subset, pivot, normalize, aggregate, and remove max compound
    subset_df = subset_dataframe(melted_df, precursor_list)
    pivot_df = aggregate_pivot(subset_df, control_precursor)
    normalized_df = normalize(pivot_df, control_precursor)
    df = aggregate_reps(normalized_df, control_precursor)
    df = drop_max_compound(df)

    return df

def make_manhattan_plot(
    df: pd.DataFrame, peptide_name: str, ax: Optional[plt.Axes] = None,
    figsize: Optional[Tuple[int, int]] = (12, 6),
    show: bool=True
) -> None:
    """
    Create a Manhattan-style plot of relative abundance for a given peptide.

    Parameters:
    df (pd.DataFrame): DataFrame containing 'Compound' column and columns for
                       mean and standard deviation of specified peptide.
    peptide_name (str): Name of the peptide for which to plot abundance.
    ax (Optional[plt.Axes]): Matplotlib Axes to plot on. If None, creates a new
                             figure.
    figsize (Optional[Tuple[int, int]]): Figure size if ax is None. Defaults to
                                         (12, 6).

    Returns:
    None
    """
    mean_column = f'{peptide_name}_mean'
    std_column = f'{peptide_name}_std'
    
    # Step 1: Sort by mean values
    df_sorted = df.sort_values(by=mean_column)
    
    # Step 2: Plot mean values with error bars for standard deviation
    create_new_fig = False
    if ax is None:
        create_new_fig = True
        fig, ax = plt.subplots(figsize=figsize)
        
    ax.errorbar(
        df_sorted["Compound"],         # x-axis: Compound names (sorted)
        df_sorted[mean_column],        # y-axis: mean values (sorted)
        yerr=df_sorted[std_column],    # Error bars for standard deviation
        fmt='o',                       # Scatter plot (no connecting lines)
        capsize=4,                     # Error bar cap size
        label=peptide_name             # Label for the legend
    )
    
    ax.axhline(1, color="red", linestyle="--")
    
    # Step 3: Customize the plot
    ax.set_xlabel("Compound")
    ax.set_ylabel("Relative Abundance")
    ax.set_title(f"Relative Abundance for Peptide {peptide_name} by Compound")
    plt.xticks(rotation=45)   # Rotate x-axis labels for readability
    plt.tight_layout()        # Adjust layout to prevent overlap
    
    # Show plot only if a new figure was created
    if create_new_fig and show:
        plt.show()