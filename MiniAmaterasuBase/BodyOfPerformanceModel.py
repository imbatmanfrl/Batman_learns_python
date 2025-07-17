from miniPerformanceModel import BudgetModel,WeeksPassed,Spending,Calc

calc = Calc(10000,2000,5000,3000)
calc.re_occurring("Data","Transport","Spotify","F")
calc.price(1500,400,0,3500)
calc.one_time_purchases(random=["FIFA","Workbook","Bread"],cost=[500,4250,500])
calc.starting_date()
calc.time_since_last_update()
calc.store("no")
calc.weekly_leftover()
calc.total_earned()
calc.total_spent()
calc.total_saved()
calc.projections(6)
