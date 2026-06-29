#1
# 8 becuse in the scope you added a score and it did not get out to the global 
# 10 becuse you printed only from the global . 
#2
name = "Agent" 

level = 2 

 

def show_info(): 

    name = "Spy" 

    level = 4 

    power = level * 10 

    print(name) 

    print(power) 

 

show_info() 

print(name) 

print(level) 