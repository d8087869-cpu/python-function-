#1
# 8 -becuse in the scope you added a score and it did not get out to the global 
# 10 -becuse you printed only from the global . 

#2
#spy - becouse the func was activeted and printed 
#40  - also was activeted by the function and printed 
#agent - printed from the global and nothing to do with the function
# 2 - level in the global was printed . and level in the scope was not active

#3 
#30 - the function takes the val of coins and changes the val to coins 20 =+10 =30
# 20 after that coins is worth 10 its multiply by 2 = 20 and you activeted the func and the coines that are inside . 

#4
#  
#70 - in the global its 100 / in func we made a new val helth= helth-damge, and activated the fun with 30 uts 100-30=70 
#35 - made a new val in the fun +5 /30+5 and 70 -35 = 35 
#100 - printed the global val 

#5 
#['map', 'key', 'torch', 'coin']- in the scope was added 2 new val in the list so when active the func you will see all new info 
#['map', 'key', 'torch', 'coin'] - when printed the items from global it points all the val that are exciting and add in to the list

#6 
#potion,shild = in the func you replaced the vals to potion . and then add by append added shild
#map , key = printed from global items = map and key 

#7 
#20 = in local you over rite the globl to a new vals 3+=10 and thed you multiply by 2 
#20 = vals in global no more exists becouse you overite the previos vals 

#8
#runing = even do its in the second func we printed it first by the first opretion of the second func 
#ready = noe out of the line of func we activet tjhe func and the val of status in fun is radey 
#waiting = we print the global val 

#9 
#16 =in second func we toke the val of first of func = 5 , and added 5+3=8 and multiply by 2 , and prints ,
#16 =  after we active the func and printed agian coins under the second func so will give the same result becose coins got a new valuy
#10 = printed the global val

#10 
#25= I take the val of firest 10 and i go to the inner abd there befoer was activeted we change it agin to 10*2=20 , 20+5 -and thes result is the new val for the outer func and also to the inner func . 
#25 = the new val from the inner becouse we used the  nonlocal and wiil print 25 
#1 = we printed  the global 
#key,map,coin will show evry print becous in list the print points to all val that in the list . 

#part 2
#1 
''''
def meters_to_centimeters(meters):
    return meters * 100 
def report_distance(centimeters):
    return f"robot moved{centimeters} centimeters"
distance_in_meters = 2.5 
centimeters_val = meters_to_centimeters(distance_in_meters)
message = report_distance(centimeters_val)
print(message)'''

#2
def add_delivary(price):
    return price + 10 
def double_price(new_price):
    return new_price * 2
iteam_price = 50
final_price = double_price(add_delivary(iteam_price))
print(final_price)

#3
def clinte_name(first, last):
    return first + last

def caps_name(name):
    return name.upper()

first_name = 'david'
last_name = 'kalaora'
final_name = caps_name(clinte_name(first_name , last_name))
print(final_name)