class BudgetManagementPlatform:
    def __init__(self):
        self.expenses = []
        self.incomes = []
        self.categories = {
            'expense': ['Loyer', 'Manger', 'Transport'],
            'income': ['Salaire', 'Business']
        }

    def record_expense(self, amount, category):
        self.expenses.append({'amount': amount, 'category': category})

    def record_income(self, amount, category):
        self.incomes.append({'amount': amount, 'category': category})

    def calculate_balance(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        total_incomes = sum(income['amount'] for income in self.incomes)
        return total_incomes - total_expenses

    def display_categories(self, transaction_type):
        if transaction_type in self.categories:
            print("Categories for", transaction_type + ":")
            for category in self.categories[transaction_type]:
                print("-", category)
        else:
            print("Invalid transaction type. Use 'expense' or 'income'.")

    def show_transactions(self, transaction_type):
        if transaction_type == 'expense':
            transactions = self.expenses
        elif transaction_type == 'income':
            transactions = self.incomes
        else:
            print("Invalid transaction type. Use 'expense' or 'income'.")
            return

        print("Transactions for", transaction_type + ":")
        for transaction in transactions:
            print("-", transaction['category'], "-", transaction['amount'])

    def show_balance(self):
        balance = self.calculate_balance()
        print("Current balance:", balance)

    def start(self):
        print("Welcome to the Budget Management Platform!")
        while True:
            print("\nMenu:")
            print("1. Record an expense")
            print("2. Record an income")
            print("3. Display expense categories")
            print("4. Display income categories")
            print("5. Show all expenses")
            print("6. Show all incomes")
            print("7. Show current balance")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == '1':
                amount = float(input("Enter the expense amount: "))
                print("Expense categories:")
                self.display_categories('expense')
                category = input("Enter the category for the expense: ")
                self.record_expense(amount, category)
                print("Expense recorded successfully!")

            elif choice == '2':
                amount = float(input("Enter the income amount: "))
                print("Income categories:")
                self.display_categories('income')
                category = input("Enter the category for the income: ")
                self.record_income(amount, category)
                print("Income recorded successfully!")

            elif choice == '3':
                self.display_categories('expense')

            elif choice == '4':
                self.display_categories('income')

            elif choice == '5':
                self.show_transactions('expense')

            elif choice == '6':
                self.show_transactions('income')

            elif choice == '7':
                self.show_balance()

            elif choice == '8':
                print("Thank you for using the Budget Management Platform. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    platform = BudgetManagementPlatform()
    platform.start()
