class Date:
    def __init__(self, day: int, month: int, year: int) -> None:

        self.day = day
        self.month = month
        self.year = year
    def get_day(self):
        return self.day
    
    def get_month(self):
        return self.month
    
    def get_year(self):
        return self.year
    
    def set_day(self, day):
        self.day = day

    def set_month(self, month):
        self.month = month
    
    def set_year(self, year):
        self.year = year

    def set_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year:}"
    
    def to_string(self):
        return f"KUN: {date1.get_day()}\nOY: {date1.get_month()}\nYIL: {date1.get_year()}"
    
date1 = Date(5, 6, 2023)

print(date1)
        
date1.set_day(13)
date1.set_month(7)
date1.set_year(2024)
print(date1)

date1.set_date(14, 7, 2024)

print(date1)

print(date1.to_string())