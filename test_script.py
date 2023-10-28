"""
Test for script.py goes here

"""
import os
from script import (
    summary,
    median,
    histogram,
    scatter_age_blood_pressure,
    create_output_directory,
    save_to_markdown,
)

# test cases


def test_output_directory_exists():
    expected_directory = "output"
    create_output_directory(expected_directory)
    # Assert: Check if the directory exists
    assert os.path.exists(expected_directory)


def test_summary():
    file_path = "heart.csv"
    summary_result = summary(file_path)
    # mean value of the fourth column resting blood pressure
    mean_4_column = summary_result.iloc[:, 3]["mean"]
    # print(mean_4_column)
    assert mean_4_column == 131.62376237623764
    # standard deviation value of fourth column resting blood pressure
    std_4_column = summary_result.iloc[:, 3]["std"]
    # print(std_4_column)
    assert std_4_column == 17.5381428135171


def test_median():
    file_path = "heart.csv"
    median_result = median(file_path)
    # Calculate the median for the fourth column resting blood pressure
    median_4_column = median_result["trtbps"]
    # print(median_4_column)
    assert median_4_column == 130.0


def test_histogram():
    histogram("heart.csv")


def test_scatter_age_blood_pressure():
    scatter_age_blood_pressure("heart.csv")


def test_save_to_markdown():
    save_to_markdown("heart.csv")


if __name__ == "__main__":
    test_summary()
    test_median()
    test_histogram()
    test_scatter_age_blood_pressure()
    test_output_directory_exists()
    test_save_to_markdown()
