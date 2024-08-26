from printing_functions import *



def make_pizza(size, *toppings):
    print(f"\nMaking a pizza {size} inch with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")




print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)