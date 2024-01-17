import os

import pandas as pd


def clean_dataframe(df):
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
    df = pd.read_csv(
        os.path.join(directory, file),
        sep="\t",
        header=None,
        names=["prev", "curr", "type", "n"],
        index_col=None,
    )

    # The current data includes the following 4 fields:

    # prev: the result of mapping the referrer URL to the fixed set of values described above
    # curr: the title of the article the client requested
    # type: describes (prev, curr)
    # link: if the referrer and request are both articles and the referrer links to the request
    # external: if the referrer host is not en(.m)?.wikipedia.org
    # other: if the referrer and request are both articles but the referrer does not link to the request. This can happen when clients search or spoof their refer.
    # n: the number of occurrences of the (referrer, resource) pair
    df = clean_dataframe(df)
    # add necessary columns for the final output
    df = add_columns(df, "lang", lang)
    df = add_columns(df, "month", month)
    return df

