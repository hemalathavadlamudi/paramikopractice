class print_tables:
    def __init__(self,num):
        self.num=num
    def print_table(self):
        f=open("output.txt","w")
        for value in range(1,11):
            print(f'{self.num}X{value}={self.num*value}',file=f)
if __name__=="__main__":
    obj1=print_tables(3)
    obj1.print_table()
