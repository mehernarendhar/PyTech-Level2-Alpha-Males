import pandas as pd
import matplotlib.pyplot as plt

class SalesDashboard:

    def __init__(self, file_name):
        self.data = pd.read_csv(file_name)
        self.data["Date"] = pd.to_datetime(self.data["Date"])
        self.data["Month"] = self.data["Date"].dt.month

    def total_sales(self):
        total = self.data["Amount"].sum()
        print(f"\nTotal Sales: ₹{total}")
        self.save_to_file(f"Total Sales: ₹{total}")

    def monthly_summary(self):
        summary = self.data.groupby("Month")["Amount"].sum()
        print("\nMonthly Sales Summary:")
        print(summary)
        self.save_to_file(f"\nMonthly Summary:\n{summary}")

    def top_product(self):
        top = self.data.groupby("Product")["Amount"].sum().idxmax()
        print(f"\nTop Selling Product: {top}")
        self.save_to_file(f"Top Product: {top}")

    def show_bar_chart(self):
        summary = self.data.groupby("Month")["Amount"].sum()
        summary.plot(kind="bar")
        plt.title("Monthly Sales")
        plt.xlabel("Month")
        plt.ylabel("Sales Amount")
        plt.show()

    def show_line_chart(self):
        summary = self.data.groupby("Month")["Amount"].sum()
        summary.plot(kind="line", marker="o")
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Sales Amount")
        plt.show()

    def save_to_file(self, text):
        with open("sales_report.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")