class Car():
    """汽车类"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + '' + self.make + ''+ self.model
        return long_name.title()

    def fill_gas_tank(self):
        print("this cat doesn`t need a gas tank")

class ElectricCar(Car):
    """电动汽车"""
    def __init__(self, make, modle, year):
        """初始化父类的属性"""
        super().__init__(make, modle, year)
        """子类属性"""
        self.battery_size = 70
    """子类方法"""
    def describe_battery(self):
        print("This car has a "+ str(self.battery_size) +"-kwh battery." )

    def fill_gas_tank(self):
        print("this cat need a gas tank")


my_tesla = ElectricCar('tesla', 'models',   2016)
print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())
print(my_tesla.fill_gas_tank())