import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


def main():

    if len(sys.argv) != 2:
        print("Usage: python project.py")
        sys.exit(1)

    file = sys.argv[1]

    data = load_data(file)

    cleaned_data = clean_data(data)

    analysis = analyze_data(cleaned_data)

    generate_charts(cleaned_data)

    generate_report(analysis)

    print("Analysis completed successfully.")
    print("Report saved as report.txt")
    print("Charts saved in charts folder")


def load_data(file):

    try:
        df = pd.read_csv(file)
        return df

    except FileNotFoundError:
        print("File does not exist.")
        sys.exit(1)

    except pd.errors.EmptyDataError:
        print("File is empty.")
        sys.exit(1)

    except pd.errors.ParserError:
        print("Invalid CSV format.")
        sys.exit(1)


def clean_data(df):

    if df is None:
        return None

    df = df.drop_duplicates()

    df = df.dropna()

    return df


def analyze_data(df):

    if df is None:
        return None

    results = {}

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:

        results[column] = {
            "mean": round(df[column].mean(), 2),
            "max": round(df[column].max(), 2),
            "min": round(df[column].min(), 2),
            "median": round(df[column].median(), 2)
        }

    return results


def generate_charts(df):

    if df is None:
        return

    os.makedirs("charts", exist_ok=True)

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) == 0:
        print("No numeric columns found.")
        return

    for column in numeric_columns:

        plt.figure(figsize=(8, 5))

        df[column].hist(bins=15)

        plt.title(f"{column} Distribution")

        plt.xlabel(column)

        plt.ylabel("Frequency")

        plt.grid(True)

        plt.savefig(f"charts/{column}.png")

        plt.close()


def generate_report(analysis):

    if analysis is None:
        return

    with open("report.txt", "w") as file:

        file.write("=" * 45 + "\n")
        file.write("         DATA ANALYSIS REPORT\n")
        file.write("=" * 45 + "\n\n")

        for column, stats in analysis.items():

            file.write(f"Column: {column}\n")
            file.write("-" * 30 + "\n")

            file.write(f"Mean: {stats['mean']}\n")
            file.write(f"Median: {stats['median']}\n")
            file.write(f"Max: {stats['max']}\n")
            file.write(f"Min: {stats['min']}\n")

            # Automatic insights
            if stats["mean"] > 1000:
                file.write("Insight: High average values detected.\n")

            elif stats["mean"] < 10:
                file.write("Insight: Low average values detected.\n")

            else:
                file.write("Insight: Values are within normal range.\n")

            file.write("\n")

        file.write("=" * 45 + "\n")
        file.write("End of report.\n")


if __name__ == "__main__":
    main()