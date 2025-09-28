class car:
    def _init_(self):
        self.acc = False
        self.brk = False 
        self.clutch = False
    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car is started vroommmmm ! ")

car1 = car()
car1.start() 