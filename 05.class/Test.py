def make_adder():
    print('this is a adder function')
    def add(x,y):
        z= x+y
        print('%d + %d = %d' %(x,y,z))
        return z
    return add

a=make_adder()
# ans=a(1,2)

# print(ans)