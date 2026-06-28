# part 1
#1 
'''
def greet(name):
    print('hello' ,name )
greet('agent x ')    
#2 
def add(a, b):
    print(a+b)
add(3 , 4) 
#3 
def square(n):
    print(n ** 2) 
square(5)
square(12)  
#4 
def greet_with_title(name, title='agent'):
    print('hello',title,name  ) 
greet_with_title('david')
greet_with_title('david', 'ceo')  
#5 
def describe(name, level, active):
    print('name: ' , name)
    print('level: ' , level)
    print('active :' , active)
describe(level= 7 , name= 'david' , active= True) 
#6 
def multiply(a, b=2):
    print(a*b)
multiply(7)
multiply(9,9)   
'''
#7
def print_largest(a, b, c):
    if a >= b :
        if a>=c :
            print (a) 
    elif c>=b :
        print(c)  
    else:
        print(b)  
print_largest(3,8,5)    
print_largest(10,2,7)
print_largest(4,4,1)
#8 
def show_fahrenheit(c):
    print((c * 9 / 5) + 32)
show_fahrenheit(0)
show_fahrenheit(100)
show_fahrenheit(37.5) 
#9 
def check_even(n):
    if n %2 == 0: 
        print(n, 'is even')
    else :
        print(n, 'is odd')    
check_even(4)
check_even(7)
#10
def summarize(items):
    print('sum' , sum(items))
    print('min' , min(items))
    print('max', max(items))
summarize([4, 9, 2, 10, 3])    
        