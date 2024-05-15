from config_loader import ConfigFileLoader
import pandas as pd
from sklearn.model_selection import train_test_split


def split_raw_data_train_test(
    df: pd.DataFrame,
    y_name: str,
    train_ratio: float = None,
    test_ratio: float = None,
    shuffle: bool = True,
    stratify: list = None,
    seed: int = None,
    config_file_path: str = None,
) -> tuple:
    """split_raw_data_train_test

    Args:
        df (pd.DataFrame): dataframe to be splitted.
        train_ratio (float, optional): train_ratio. Defaults to None.
        test_ratio (float, optional): test_ratio. Defaults to None.
        shuffle (bool, optional): if is to be shuffled. Defaults to True.
        stratify (list, optional): if is to be stratified. Defaults to None.
        seed (int, optional): seed, for randomness. Defaults to None. if None, gets from config.
        config_file_path (str, optional): path for a config file, if none is passed uses the default one in config.yaml. Defaults to None.

    Returns:
        tuple: tuple(X_train, X_test, Y_train, Y_test)
    """
    if seed is None:
        seed = ConfigFileLoader(config_file_path).get_seed()

    X = df.drop(y_name, axis=1)
    Y = df[y_name]
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=test_ratio,
        train_size=train_ratio,
        shuffle=shuffle,
        random_state=seed,
        stratify=stratify,
    )

    return (X_train, X_test, Y_train, Y_test)
