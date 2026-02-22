from model import MarksAnalyzer

def main():
    analyzer = MarksAnalyzer()

    while True:
        print("\n========== Student Marks Analyzer ==========")
        print("1. Calculate Average Scores")
        print("2. Show Highest & Lowest (Math)")
        print("3. Display Bar Chart")
        print("4. Display Histogram")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            analyzer.calculate_average()

        elif choice == "2":
            analyzer.highest_lowest()

        elif choice == "3":
            analyzer.show_bar_chart()

        elif choice == "4":
            analyzer.show_histogram()

        elif choice == "5":
            print("Exiting Program...")
            break

        else:
            print("Invalid choice. Please enter between 1 and 5.")

if __name__ == "__main__":
    main()