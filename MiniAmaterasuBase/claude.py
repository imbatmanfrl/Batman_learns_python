from datetime import datetime, timedelta
import json
import os


class FinanceTracker:
    def __init__(self):
        self.weekly_earnings = []  # Only current week
        self.all_earnings = []  # All time earnings with dates
        self.weekly_expenses = []  # Current week expenses
        self.all_expenses = []  # All time expenses
        self.data_file = "finance_data.json"
        self.load_data()

    def earn_daily(self, *args):
        """Add daily earnings to both weekly and total tracking"""
        earned = list(args)
        earned_today = sum(earned)
        today = datetime.now().strftime('%Y-%m-%d')

        print(f"You earned #{earned_today} today")

        # Add to weekly earnings (just amounts for easy weekly calculation)
        self.weekly_earnings.append(earned_today)

        # Add to all-time earnings with date
        earning_entry = {
            'amount': earned_today,
            'date': today,
            'breakdown': earned
        }
        self.all_earnings.append(earning_entry)

        self.save_data()
        return earned_today

    def spend_daily(self, *args):
        """Add daily expenses"""
        spent = list(args)
        spent_today = sum(spent)
        today = datetime.now().strftime('%Y-%m-%d')

        print(f"You spent #{spent_today} today")

        # Add to weekly expenses
        self.weekly_expenses.append(spent_today)

        # Add to all-time expenses with date
        expense_entry = {
            'amount': spent_today,
            'date': today,
            'breakdown': spent
        }
        self.all_expenses.append(expense_entry)

        self.save_data()
        return spent_today

    def calculate_weekly_leftover(self):
        """Calculate how much is left from this week's earnings after expenses"""
        total_earned_this_week = sum(self.weekly_earnings)
        total_spent_this_week = sum(self.weekly_expenses)
        leftover = total_earned_this_week - total_spent_this_week

        print(f"This Week Summary:")
        print(f"Earned: #{total_earned_this_week}")
        print(f"Spent: #{total_spent_this_week}")
        print(f"Leftover: #{leftover}")

        return {
            'earned': total_earned_this_week,
            'spent': total_spent_this_week,
            'leftover': leftover
        }

    def reset_weekly(self):
        """Call this at the start of each week"""
        # Archive current week data before resetting
        if self.weekly_earnings or self.weekly_expenses:
            week_summary = self.calculate_weekly_leftover()
            # You could save this to a weekly_summaries list if needed

        self.weekly_earnings = []
        self.weekly_expenses = []
        self.save_data()
        print("Weekly data reset for new week!")

    def get_total_earnings(self):
        """Get all-time total earnings"""
        return sum(entry['amount'] for entry in self.all_earnings)

    def get_total_expenses(self):
        """Get all-time total expenses"""
        return sum(entry['amount'] for entry in self.all_expenses)

    def get_overall_balance(self):
        """Get overall financial position"""
        total_earned = self.get_total_earnings()
        total_spent = self.get_total_expenses()
        return total_earned - total_spent

    def save_data(self):
        """Save all data to file"""
        data = {
            'weekly_earnings': self.weekly_earnings,
            'weekly_expenses': self.weekly_expenses,
            'all_earnings': self.all_earnings,
            'all_expenses': self.all_expenses,
            'last_updated': datetime.now().isoformat()
        }

        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        """Load data from file if it exists"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)

                self.weekly_earnings = data.get('weekly_earnings', [])
                self.weekly_expenses = data.get('weekly_expenses', [])
                self.all_earnings = data.get('all_earnings', [])
                self.all_expenses = data.get('all_expenses', [])

                print(f"Data loaded from {self.data_file}")
            except Exception as e:
                print(f"Error loading data: {e}")

    def show_recent_activity(self, days=7):
        """Show recent earnings and expenses"""
        cutoff_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

        print(f"\n--- Last {days} Days Activity ---")

        recent_earnings = [e for e in self.all_earnings if e['date'] >= cutoff_date]
        recent_expenses = [e for e in self.all_expenses if e['date'] >= cutoff_date]

        print("Earnings:")
        for earning in recent_earnings:
            print(f"  {earning['date']}: #{earning['amount']}")

        print("Expenses:")
        for expense in recent_expenses:
            print(f"  {expense['date']}: #{expense['amount']}")


# Example usage:
if __name__ == "__main__":
    tracker = FinanceTracker()

    # Add some earnings
    tracker.earn_daily(1000, 500, 200)  # Multiple income sources
    tracker.earn_daily(1500)

    # Add some expenses
    tracker.spend_daily(300, 150, 50)  # Multiple expenses
    tracker.spend_daily(200)

    # Check weekly summary
    tracker.calculate_weekly_leftover()

    # Check totals
    print(f"\nAll-time earned: #{tracker.get_total_earnings()}")
    print(f"All-time spent: #{tracker.get_total_expenses()}")
    print(f"Overall balance: #{tracker.get_overall_balance()}")

    # Show recent activity
    tracker.show_recent_activity()