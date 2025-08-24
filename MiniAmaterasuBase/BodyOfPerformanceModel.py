from miniPerformanceModel import BudgetModel,WeeksPassed,Spending,Calc

calc = Calc()
#calc.input(10000,800,3000,3000)
calc.re_occurring("Data","Transport","Spotify","F")
calc.price(1500,800,0,0)
#calc.one_time_purchases(random=["FIFA","Workbook","Bread"],cost=[500,4250,500])
calc.one_time_purchases(random=[""],cost=[0])
calc.starting_date(2025,8,3)
calc.time_since_last_update()
calc.store("yes")
calc.weekly_leftover()
calc.total_earned()
calc.total_spent()
calc.total_saved()
calc.projections(6)


#N.B, file.readlines() gives all lines inside a list in a file
#line.strip() removes \n and spaces
#if line,strip() ignores blank lines
#float(line.strip()) turns the clean line into a number