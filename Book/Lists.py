
'''



def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('CJ', 'Lame', location = 'Furth', field = 'CS', likes = 'Cash' )


print('\n\n', user_profile)





def make_sandwich(picker, s_name, **sandwich):
    sandwich['customer'] = picker
    sandwich['sandwich_name'] = s_name

    return sandwich


sandwich_order = make_sandwich('CJ', 'Tuna', drink = 'Cola',)
print("\n--- Sammich ----  ")
for picker, s_name in sandwich_order.items():
    print(f"{picker}: {s_name} ")

sandwich_order = make_sandwich('JC', 'Parmisian', drink = 'Sprite', extra = 'napkins')
print("\n--- Sammich ----  ")
for picker, s_name in sandwich_order.items():
    print(f"{picker}: {s_name} ")

sandwich_order = make_sandwich('BJ', 'Peperoni', drink = 'Pepsi', extra = 'mustard')
print("\n--- Sammich ----  ")
for picker, s_name in sandwich_order.items():
    print(f"{picker}: {s_name}")



'''



def make_car(manufacturer, model_name, **car_build):
    car_build['manufacturer'] = manufacturer
    car_build['model'] = model_name

    return car_build

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print("--- Car Order ---")
for manufacturer, model_name in car.items():
    print(f"{manufacturer}: {model_name}")

