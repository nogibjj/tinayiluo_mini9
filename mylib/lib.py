"""
Python Descriptive Statistics Script Library
"""
import pandas as pd


# read the Dataframe heart.csv.
def readfile(a):
    df = pd.read_csv(a)
    return df


# if __name__ == "__main__":
# readfile("heart.csv")
