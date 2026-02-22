from model import SalesDashboard

dashboard = SalesDashboard("sales.csv")

while True:
    print("\n========== Sales Summary Dashboard ==========")
    print("1. Total Sales")
    print("2. Monthly Summary")
    print("3. Top Selling Product")
    print("4. Show Bar Chart")
    print("5. Show Line Chart")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        dashboard.total_sales()

    elif choice == "2":
        dashboard.monthly_summary()

    elif choice == "3":
        dashboard.top_product()

    elif choice == "4":
        dashboard.show_bar_chart()

    elif choice == "5":
        dashboard.show_line_chart()

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice. Try again.")