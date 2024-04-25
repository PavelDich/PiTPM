class Month:
    def __init__(self, num_month) -> None:
        self.last_day_of_month = dict()
        self.num_month = num_month
        self.name_month = {1 : 'Январь', 2 : 'Февраль', 3 : 'Март', 4 : 'Апрель',
                           5 : 'Май', 6 : 'Июнь', 7 : 'Июль', 8 : 'Август',
                           9 : 'Сентябрь', 10 : 'Октябрь', 11 : 'Ноябрь', 12 : 'Декабрь'}

        for i in range(12):
            if self.num_month <= 7:
                if self.num_month % 2 == 1:
                    self.last_day_of_month.update(i + 1, 31)
                else:
                    self.last_day_of_month.update(i + 1, 30)
            else:
                if self.num_month % 2 == 0:
                    self.last_day_of_month.update(i + 1, 31)
                else:
                    self.last_day_of_month.update(i + 1, 30)

    def get_num_month(self):
        return self.num_month
    
    def get_name_month(self):
        return self.name_month(self.num_month)
    
    def get_last_num_day_month(self):
        return self.last_day_of_month(self.num_month)
    
    def first_day_week_of_month(self):
        num = 0

        for i in range(self.num_month - 1):
            num += self.last_day_of_month(i + 1)

        return (num + 1) % 7
    
    def last_day_week_of_month(self):
        num = 0

        for i in range(self.num_month):
            num += self.last_day_of_month(i + 1)

        return num % 7