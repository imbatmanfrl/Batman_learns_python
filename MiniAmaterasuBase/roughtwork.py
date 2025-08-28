def spent_today(self, name, cost):
    item_date = datetime.date.today().isoformat()

    # Handle both single items and lists
    if isinstance(name, list) and isinstance(cost, list):
        # Multiple items
        total_spent_today = 0
        for item_name, item_cost in zip(name, cost):
            spent = {
                "item": item_name,
                "cost": item_cost,
                "date": item_date
            }
            self.weekly_expenditure.append(item_cost)
            self.all_expenditure.append(spent)
            total_spent_today += item_cost

        # Print once with total
        print(f"You spent #{total_spent_today} today")

    else:
        # Single item
        spent = {
            "item": name,
            "cost": cost,
            "date": item_date
        }
        self.weekly_expenditure.append(cost)
        self.all_expenditure.append(spent)
        print(f"You spent #{cost} today")

    with open("all_expenditure.json", "w") as file:
        json.dump(self.all_expenditure, file, indent=2)
