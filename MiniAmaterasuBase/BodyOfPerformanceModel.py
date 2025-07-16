from miniPerformanceModel import BudgetModel,WeeksPassed,Spending,Calc

calc = Calc(1000,2000,5000,3000)
calc.re_occurring("Data","Transport","Spotify","F")
calc.price(1500,800,2000,3500)
calc.one_time_purchases(random=["FIFA","Workbook","Bread"],cost=[500,4250,500])
calc.starting_date(2025-7-16)
calc.time_since_last_update()
calc.store()
calc.weekly_leftover()
calc.total_earned()
calc.total_spent()
calc.total_saved()
calc.projections(6)

"""error: Traceback (most recent call last):
  File "C:\Users\HP\PycharmProjects\BatmanLearnsPython\MiniAmaterasuBase\BodyOfPerformanceModel.py", line 7, in <module>
    calc.starting_date(2025-7-16)
  File "C:\Users\HP\PycharmProjects\BatmanLearnsPython\MiniAmaterasuBase\miniPerformanceModel.py", line 27, in starting_date
    self.get_how_long = datetime.datetime.strptime(self.the_date,"%Y-%m-%d").date()
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\HP\AppData\Local\Programs\Python\Python312\Lib\_strptime.py", line 554, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\HP\AppData\Local\Programs\Python\Python312\Lib\_strptime.py", line 333, in _strptime
    raise ValueError("time data %r does not match format %r" %
ValueError: time data '2002' does not match format '%Y-%m-%d'"""