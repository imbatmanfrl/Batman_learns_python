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

"""['Data', 'Transport', 'Spotify', 'F']
one-time purchases {'FIFA': 500, 'Workbook': 4250, 'Bread': 500}
2025-07-16
You've been budgeting for 0 weeks
0 weeks has passed since you last budgeted!
Do you want to update your Budget?(YES/NO): no
Have a great day then!
You spent #7800 on ['Data', 'Transport', 'Spotify', 'F'] this week
You spent #5250 on ['FIFA', 'Workbook', 'Bread'] this week
You've spent a total of #13050 this week
You have #-12050 left this week
You have earned #9000.0 since 2025-07-16
So far, you have spent #5.0 since 2025-07-16
You have earned #5.0 since 2025-07-16
Zero weeks has passed since you started

Process finished with exit code 0"""