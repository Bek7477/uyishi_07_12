class Time:
    def __init__(self, hour, minute, second) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def get_hour(self):
        return self.hour
    
    def get_minute(self):
        return self.minute
    
    def get_second(self):
        return self.second
    
    def set_hour(self, hour):
        self.hour = hour

    def set_minute(self, minute):
        self.minute = minute

    def set_second(self, second):
        self.second = second

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    def next_second(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
        return self
    
    def previous_second(self):
        self.second -= 1 
        if self.second == -1:
            self.second = 59
            self.minute -= 1
            if self.minute == -1:
                self.minute = 59
                self.hour -= 1
                if self.hour == -1:
                    self.hour = 23
        return self

time1 = Time(23, 59, 59)
print(time1) 

time1.next_second()
print(time1)

time1.previous_second()
print(time1)

time1.set_time(12, 30, 45)
print(time1)