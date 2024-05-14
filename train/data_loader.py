import pandas as pd

def load_raw_data_from_url(url: str, header: list = None) -> pd.DataFrame:
    """load_raw_data_from_url

    Args:
        url (str): url from data source

    Returns:
        pd.DataFrame: df
    """
    try:
        if header:
            df = pd.read_csv(url, names=header)
        else:
            df = pd.read_csv(url)
        return df
    except Exception as e:
        raise e
