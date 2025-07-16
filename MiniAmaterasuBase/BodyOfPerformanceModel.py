from miniPerformanceModel import BudgetModel,WeeksPassed,Spending,Calc

calc = Calc(1000,2000,5000,3000)
calc.re_occurring("Data","Transport","Spotify","F")
calc.price(1500,800,2000,3500)
calc.one_time_purchases(random=["FIFA","Workbook","Bread"],cost=[500,4250,500])
calc.starting_date()
calc.time_since_last_update()
calc.store()
calc.weekly_leftover()
calc.total_earned()
calc.total_spent()
calc.total_saved()
calc.projections(6)

"""Traceback (most recent call last):
  File "C:\Users\HP\PycharmProjects\BatmanLearnsPython\MiniAmaterasuBase\BodyOfPerformanceModel.py", line 11, in <module>
    calc.total_earned()
  File "C:\Users\HP\PycharmProjects\BatmanLearnsPython\MiniAmaterasuBase\miniPerformanceModel.py", line 103, in total_earned
    lines = file.readlines()
            ^^^^^^^^^^^^^^^^
io.UnsupportedOperation: not readable"""