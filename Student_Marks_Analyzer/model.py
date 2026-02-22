import pandas as pd
import matplotlib.pyplot as plt

class MarksAnalyzer:
    def __init__(self, filename="marks.csv", output="data.txt"):
        self.filename = filename
        self.output = output

        try:
            self.df = pd.read_csv(self.filename)
        except FileNotFoundError:
            print("Error: marks.csv file not found.")
            self.df = None

    def calculate_average(self):
        if self.df is None:
            return

        avg_math = self.df["math score"].mean()
        avg_reading = self.df["reading score"].mean()
        avg_writing = self.df["writing score"].mean()

        with open(self.output, "w") as f:
            f.write("===== Average Scores =====\n")
            f.write(f"Math: {avg_math:.2f}\n")
            f.write(f"Reading: {avg_reading:.2f}\n")
            f.write(f"Writing: {avg_writing:.2f}\n")

        print("\nAverage Scores:")
        print(f"Math    : {avg_math:.2f}")
        print(f"Reading : {avg_reading:.2f}")
        print(f"Writing : {avg_writing:.2f}")
        print("Saved to data.txt")

    def highest_lowest(self):
        if self.df is None:
            return

        highest = self.df.loc[self.df["math score"].idxmax()]
        lowest = self.df.loc[self.df["math score"].idxmin()]

        with open(self.output, "a") as f:
            f.write("\n===== Highest & Lowest (Math) =====\n")
            f.write(f"Highest Math Score: {highest['math score']}\n")
            f.write(f"Lowest Math Score: {lowest['math score']}\n")

        print("\nHighest Math Score:", highest["math score"])
        print("Lowest Math Score :", lowest["math score"])
        print("Saved to data.txt")

    def show_bar_chart(self):
        if self.df is None:
            return

        self.df["math score"].head(10).plot(kind="bar")
        plt.title("Top 10 Students - Math Scores")
        plt.xlabel("Student Index")
        plt.ylabel("Marks")
        plt.tight_layout()
        plt.show()

    def show_histogram(self):
        if self.df is None:
            return

        self.df["math score"].plot(kind="hist", bins=10)
        plt.title("Distribution of Math Scores")
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()