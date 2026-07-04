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

'''
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

#4
def cel_to_fahr(celsius):
    return (celsius * 9/5) +32 
def temp(fahr):
    return f'the temp is {fahr}*f'
report = temp(cel_to_fahr(25))
print(report)

#5
def apply_damage(starting_health, damage):
    return starting_health - damage


def apply_healing(damaged_health, healing):
    return damaged_health + healing
starting_health = 100
damage = 30
healing = 20

final_health = apply_healing(apply_damage(starting_health, damage), healing)
print(final_health)
#6 
def total_price(p1, p2, p3):
    return p1+p2+p3 
def discount(total):
    return total * 0.8
def final_price(discount_price):
    return f'the final price {discount_price} '
price1=10
price2=20
price3=30
message = final_price(discount(total_price(price1,price2,price3)))
print(message)
'''

'''
#7
def clean_password(password):
    return password.strip()
def password_length(cleaned_password):
    return len(cleaned_password)
def valid_pass(length):
    return length>=8
password = " mypassword "
result = valid_pass(password_length(clean_password(password)))
print(result)
#8
def bonus_grade(grade):
    return grade +5
def multi_grade(new_grade):
    return new_grade * 1.1
def final_grade(result):
    return min(result , 100)
grade = 85
final = final_grade(multi_grade(bonus_grade(grade)))
print(final)
#9
def sen_lower(sentence):
    return sentence.lower()
def count_a(lower_sen):
    return lower_sen.count('a')
def message(count):
    return f"The letter a appears {count} times."
sentence= 'a tiger and a dog and a lion and egal are my favorit '
result = message(count_a(sen_lower(sentence)))
print(result)
#10
def tatal_value(price,amount):
    return price*amount
def subtrac_storage(total):
    return total - 15
def werth_the_monye(new_val):
    return new_val > 100
price = 25
amount = 5
result= werth_the_monye(subtrac_storage(tatal_value(price,amount)))
print(result)
'''
#11

def first_part(first_name):
    return first_name[:3]
def last_part(last_name):
    return last_name[:3]
def join_parts(part1, part2):
    return part1 + "_" + part2
def to_lowercase(username):
    return username.lower()
first_name = "David"
last_name = "kalaora"
final_username = to_lowercase(join_parts(first_part(first_name), last_part(last_name)))
print(final_username)

#12
def total_fuel(distance, fuel_per_km):
    return distance * fuel_per_km
def fuel_cost(total_fuel, price_per_liter):
    return total_fuel * price_per_liter
def cost_per_passenger(total_cost, passengers):
    return total_cost / passengers
distance = 150
fuel_per_km = 2.5
price_per_liter = 7
passengers = 3

final_cost = cost_per_passenger(fuel_cost(total_fuel(distance, fuel_per_km), price_per_liter), passengers)
print(final_cost)

#13
def sum_scores(scores):
    return sum(scores)
def average_score(total, count):
    return total / count
def result(average):
    return "pass" if average >= 60 else "fail"
scores = [70, 80, 50, 90]
final_result = result(average_score(sum_scores(scores), len(scores)))
print(final_result)

#14
def short_sentence(product, amount):
    return f"{amount} {product}s"
def long_sentence(sentence, price_per_item, amount):
    total_price = price_per_item * amount
    return f"{sentence} for {total_price} shekels"
def ready_order(long_sentence):
    return long_sentence + " - order ready"
product = "keyboard"
amount = 3
price_per_item = 100

final_sentence = ready_order(long_sentence(short_sentence(product, amount), price_per_item, amount))
print(final_sentence)
