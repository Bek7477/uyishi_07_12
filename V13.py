class Book:
    def __init__(self, name, page_count, price) -> None:
        self.name = name
        self.page_count = page_count
        self.price = price

    def add_pages(self):
        self.page_count += 10    

    def adjust_price(self):
        if self.page_count > 100:
            self.price /= 2
    def __str__(self) -> str:
        return f"Kitob nomi: {self.name}, Sahifalar soni: {self.page_count}, Narxi ${self.price}"
    
kitoblar = []
for i in range(2):
    name = input(f"{i + 1} - kitob nomi: ")
    page_count = int(input(f"{i + 1}- kitob sahifasi soni: "))
    price = float(input(f"{i + 1}- kitob narxi: "))
    kitoblar.append(Book(name,page_count,price))

for kitob in kitoblar:
    kitob.add_pages()
    kitob.adjust_price()

for kitob in kitoblar:
    print(kitob)