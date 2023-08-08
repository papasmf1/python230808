# class2.py 
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    def print(self):
        print("{0}, {1}, {2}".format(
            self.id, self.name, self.price))
        
#인스턴스 생성
p1 = Product(100, "아이폰14", 950000)
p1.print() 
