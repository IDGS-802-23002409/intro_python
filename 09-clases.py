class OperasBass:
    num1=0
    num2=0
    res=0
    
    def __init__(self):
        self.num1=0
        self.num2=0
    
    def sumar(self):
        self.res=self.num1+self.num2
        print("la suma es:{}".format(self.res))
        
    def resta(self):
        self.res=self.num1+self.num2
        print("la suma es:{}".format(self.res))

def main():
    obj=OperasBass()
    obj.suma()
    
if __name__ == "__main__":
    