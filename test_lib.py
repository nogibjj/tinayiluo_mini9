"""
Test for library goes here

"""
from mylib.lib import readfile
import pandas as pd


def test_readfile():
    file_path = "heart.csv"
    data_csv = readfile(file_path)
    assert isinstance(data_csv, pd.DataFrame)
    assert not data_csv.empty


if __name__ == "__main__":
    test_readfile()
