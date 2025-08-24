class Daily:

    def earn_daily(self,*args):
        self.weekly_earn = []
        earned = list(args)
        earned_today = sum(earned)
        print(f"You earned #{earned_today} today")

    def spent_today(self, name, cost):
        self.item_name = list(name)
        self.item_cost = list(cost)
        the_zip = zip(self.item_name, self.item_cost)
        self.weekly_expenditure = dict(the_zip)
        print(self.weekly_expenditure)

daily = Daily()
daily.earn_daily(300,67767,766737,5662626,2726252,7782782)
daily.spent_today(name=["rice","garri","beans"],cost=[234,23456,12345])