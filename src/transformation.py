import os

import pandas as pd


def clean_dataframe(df):
    """
    Cleans the given dataframe by handling missing values, duplicates, and renaming columns.
    It also removes specific characters from the 'referrer', 'resource', and 'link_type' columns.

    Args:
        df (pandas.DataFrame): The input dataframe to be cleaned.

    Returns:
        pandas.DataFrame: The cleaned dataframe.
    """
    
    # Handling Missing Values
    df.dropna(inplace=True)
    # Handling Duplicates
    df.drop_duplicates(inplace=True)
    # Rename Columns
    df = df.rename(
        columns={
            "prev": "referrer",
            "curr": "resource",
            "type": "link_type",
            "n": "count",
        },
    )

    # Remove specific characters from columns
    df["referrer"] = df["referrer"].str.replace("'", "")
    df["resource"] = df["resource"].str.replace("'", "")
    df["link_type"] = df["link_type"].str.replace("'", "")

    return df


# add columns
def add_columns(df, name: str, value):
    """
    Add a new column to the DataFrame with the specified name and value.

    Args:
        df (pandas.DataFrame): The DataFrame to add the column to.
        name (str): The name of the new column.
        value: The value to assign to the new column.

    Returns:
        pandas.DataFrame: The DataFrame with the new column added.
    """
    df[name] = value
    return df


def transform_file(directory, file, lang, month):
    """
    Transforms a file by reading it as a DataFrame, cleaning the data, and adding necessary columns.

    Args:
        directory (str): The directory path where the file is located.
        file (str): The name of the file to be transformed.
        lang (str): The language of the data.
        month (str): The month of the data.

    Returns:
        pandas.DataFrame: The transformed DataFrame.
    """
    
    df = pd.read_csv(
        os.path.join(directory, file),
        sep="\t",
        header=None,
        names=["prev", "curr", "type", "n"],
        index_col=None,
    )

    df = clean_dataframe(df)
    df = add_columns(df, "lang", lang)
    df = add_columns(df, "month", month)
    return df
