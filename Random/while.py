'''
cn = 1
while cn <= 5:
    print(cn)
    cn += 1


prompt = "\nSay smth i say it back: "
prompt += "\nEnter 'quit' to end\n"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print('\n', message)




prompt = "\nName City u like: "
prompt += "\nEnter 'quit' to end\n"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I like {city.title()}!")



cn = 0
while cn < 10:
    cn += 1
    if cn % 2 == 0:
        continue

    print(cn)




x = 1
while x <= 5:
    print(x)
    x += 1

#infinite loop
x = 1
while x <= 5:
    print(x)





prompt = "\nTopping u want to add: "
prompt += "\nEnter 'quit' to end\n"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"adding {topping}")






while True:
    age = int(input("Enter age:\n(0) to quit:\n"))

    if age == 0:
        break
    elif age <=3:
        print("Free")
    elif 3 <= age <=12:
        print('10$')
    elif age >=12:
        print('15$')


'''

