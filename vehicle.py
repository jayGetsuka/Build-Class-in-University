import datetime
class Vehicle:
    Species = "Personal Car"
    count = 0
    def __init__(self,brand, model, tanksize):
        self.brand = brand
        self.model = model
        self.tanksize = tanksize
        Vehicle.count += 1
       
    def Check_tank(self, used_oil):
        remain = self.tanksize - used_oil
        if remain == self.tanksize:
            return "Full"
        elif remain < 2:
            return "QUITE EMPTY"
        elif remain == 0:
            return "EMPTY"
        else:
            return "NORMAL"
    @classmethod
    def Showcount(cls):
        print(cls.count, cls.Species)
    @staticmethod
    def Calcharge(price, release_date):
        data = (datetime.datetime.now()).year - release_date
        if data > 10:
            charge = (price * 0.002) * data
            return f"จำนวนปี: {data} ดอกเบี้ย: {charge}"
        elif 3 < data < 10:
            charge = (price * 0.005) * data
            return f"จำนวนปี: {data} ดอกเบี้ย: {charge}"
        elif data < 3:
            charge = (price * 0.008) * data
            return f"จำนวนปี: {data} ดอกเบี้ย: {charge}"


obj = Vehicle("lambogini", "avantado", 30)
print(obj.Check_tank(20))
obj.Showcount()
print(obj.Calcharge(12000000,2012))
