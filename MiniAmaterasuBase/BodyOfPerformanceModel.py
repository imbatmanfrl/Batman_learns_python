from miniPerformanceModel import BudgetModel,WeeksPassed,Calc

calc = Calc()
#calc.input(10000,800,3000,3000)
calc.earn_daily(2500)
calc.spent_today("phone keep", 200)
calc.spent_today("puff puff", 300)
calc.spent_today("transport", 400)
calc.save_today(0)
calc.invest(name="",cost=0)
calc.starting_date(2025,8,28)
calc.weekly_amounts()
calc.weekly_leftover()
calc.tottal_earned()
calc.tottal_spent()
calc.tottal_saved()
calc.tottal_invested()
calc.projections(6)


#N.B, file.readlines() gives all lines inside a list in a file
#line.strip() removes \n and spaces
#if line,strip() ignores blank lines
#float(line.strip()) turns the clean line into a number