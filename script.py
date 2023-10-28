"""
Main code
"""
import os
import matplotlib.pyplot as plt
from mylib.lib import readfile


# generates summary statistics for the numeric columns in the DataFrame heart.csv.
def summary(a):
    df = readfile(a)
    summary_stats = df.describe()
    summary_stats.to_html("output/describe_summary.html", index=False)
    return summary_stats


# Calculate the median value for each column in heart.csv
def median(a):
    df = readfile(a)
    median_values = df.median()
    median_df = median_values.to_frame()
    median_df.reset_index(inplace=True)  # Reset the index to include it in the output
    # Save the DataFrame to an HTML file
    median_df.to_html("output/describe_median.html", index=False)
    return median_values


# Generate histogram for each column in heart.csv
def histogram(a, output_dir="output"):
    df = readfile(a)
    columns = df.columns

    for column in columns:
        plt.figure(figsize=(8, 4))  # Create a new figure for each column
        plt.hist(df[column])
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.title(f"Histogram of {column}")
        plt.grid(True)
        # plt.show()  # Display the histogram for the current column

        # Generate a unique filename for each histogram
        output_path = os.path.join(output_dir, f"histogram_{column}.png")

        # Save the histogram plot as an image
        plt.savefig(output_path, format="png")
        plt.close()


# Generate scatter plot
# for the 4th column(resting blood pressure)
# and the 1st column (age) in heart.csv


def scatter_age_blood_pressure(a):
    df = readfile(a)
    x = df.iloc[:, 0]  # 1st column (age)
    y = df.iloc[:, 3]  # 4th column (resting blood pressure)
    plt.scatter(x, y, alpha=0.5, label="Data Points")
    plt.xlabel("Age")
    plt.ylabel("Resting Blood Pressure (mm Hg)")
    plt.title("Scatter Plot: Age vs. Resting Blood Pressure")
    plt.grid(True)
    # plt.legend()
    # plt.show()

    plt.savefig("output/scatter.png", format="png")
    plt.close()


# make output directory to save html and png
def create_output_directory(directory="output"):
    """Create an output directory if it doesn't exist."""
    os.makedirs(directory, exist_ok=True)


def save_to_markdown(csv):
    """save summary report to markdown"""
    describe_df = summary(csv)
    markdown_table1 = describe_df.to_markdown()
    mean_df = median(csv)
    markdown_table2 = mean_df.to_markdown()

    # Write the markdown report to a file
    with open("heart_summary.md", "w", encoding="utf-8") as file:
        file.write("## Descriptive Summary Statistics:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("## Median Statistics:\n")
        file.write(markdown_table2)
        file.write("\n\n")  # Add a new line
        directory = "output"
        file.write("## Histograms and Scatter Plot: \n")
        # Generate plots and add them to the report for each item in plots
        i = 0
        for plot in os.listdir(directory):
            f = os.path.join(directory, plot)
            if "histogram" in f:
                # print(f)
                file.write(f"![histogram_{i}]({f})\n")
                file.write("\n\n")  # Add a new line
            elif "output/scatter.png" == f:
                # print(f)
                file.write(f"![scatter_{i}]({f})\n")

            i += 1


# if __name__ == "__main__":
# create_output_directory()
# summary("heart.csv")
# median("heart.csv")
# histogram("heart.csv")
# scatter_age_blood_pressure("heart.csv")
