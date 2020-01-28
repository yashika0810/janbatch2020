'''class employee:
    def name(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
obj=employee()
print(obj.name("welcome","training"))


class candidate:
    def check(self,par1,par2):
        return par1+par2
obj1=candidate()
print(obj1.check(1,2))
'''

class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj1=test('yashika',24)
print(obj1.name,obj1.age)