class Zate:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day

        self.last_day_of_month = dict()
        self.name_month = {1 : 'Январь', 2 : 'Февраль', 3 : 'Март', 4 : 'Апрель',
                           5 : 'Май', 6 : 'Июнь', 7 : 'Июль', 8 : 'Август',
                           9 : 'Сентябрь', 10 : 'Октябрь', 11 : 'Ноябрь', 12 : 'Декабрь'}
        self.name_day_of_week = {1 : 'Понедельник', 2 : 'Вторник', 3 : 'Среда', 4 : 'Четверг',
                                 5 : 'Пятница', 6 : 'Суббота', 7 : 'Воскресенье'}

        for i in range(12):
            if month <= 7:
                if month % 2 == 1:
                    self.last_day_of_month.update(i + 1, 31)
                else:
                    self.last_day_of_month.update(i + 1, 30)
            else:
                if self.num_month % 2 == 0:
                    self.last_day_of_month.update(i + 1, 31)
                else:
                    self.last_day_of_month.update(i + 1, 30)
        
        num = 0
        for i in range(self.num_month):
            num += self.last_day_of_month(i + 1)
        
        self.days_after = (year * 365 + year // 4) + num + day
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month
    
    def get_day(self):
        return  self.day
    
    def get_num_day_of_week(self):
        return self.days_after % 7
    
    def get_name_day_of_week(self):
        return self.name_day_of_week(self.days_after % 7)
    
    def get_name_month(self):
        return self.name_month(self.month)

class ZateExt(Zate):
    def sum_year(self, year):
        self.year += year
    
    def dif_year(self, year):
        self.year -= year
    
    def sum_month(self, month):
        self.month += month
    
    def dif_month(self, month):
        self.month -= month
    
    def sum_day(self, day):
        self.day += day
    
    def dif_day(self, day):
        self.day -= day