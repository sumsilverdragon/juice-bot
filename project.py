"""This is a basic chat-bot that interacts with the user to help order a juice.
It can be used for any similar product or service. Customer can order multiple juices.
In the next stage of development it could help a customer with their decision,
based on emotion - a personal shopper"""

import random
from simpleimage import SimpleImage

ALL_JUICE = 'all_juice.jpg'

#helper functions:
def random_name_response(name):
    #a fun random response to the customer name, chosen from a list
    response_list = ["No way, that's my cousin's name!", "Cool name!", "I like your name!", "What a name!"]
    random_num = random.randint(0, 3)

    if name == "Simone" or name == "simone":
        print("Hey, that's cool! My creator's name is Simone! 😎")
    else:
        print(response_list[random_num])

def order_name():
    order = input("Can I get your name, please? ")
    return order

def read_back_order(customer_name, juice, juice_orders):
    print("\nOkay,", customer_name, "\nGetting the following ready for you:")
    for juice in juice_orders:
        print('-', *juice, sep=' ')

def order_extra_shot():
    order = input("\nWould you like an extra shot of: \n[a] Fiery Ginger \n[b] Cooling Turmeric \n[c] No, thanks!")
    if order == 'a':
        return "with a shot of ginger"
    elif order == 'b':
        return "with a shot of turmeric"
    elif order == 'c':
        return "no shot"
    else:
        wrong_choice_message()
        return order_extra_shot()

def order_size():
    order = input("\nWhich size do you prefer? \n[a] 250ml \n[b] 500ml ")
    if order == 'a':
        return "250ml"
    elif order == 'b':
        return "500ml"
    else:
        wrong_choice_message()
        return order_size()

def order_juice_flavour():
    order = input("\nWhich flavour juice would you like? 😊 \n[a] Green Juice \n[b] Pine-Pear Juice \n[c] Vit C Juice ")
    if order == 'a':
        return "green juice"
    elif order == 'b':
        return "pine-pear juice"
    elif order == 'c':
        return "vit c juice"
    else:
        wrong_choice_message()
        return order_juice_flavour()

def wrong_choice_message():
    #a message to specify that customer has to choose form the given options
    print(" \nOops! Please choose the corresponding letter to enter your choice. \n ")

def welcome_image_pop_up():
    welcome_image = SimpleImage(ALL_JUICE)
    welcome_image.show()

def juice_bot():
    """The bot will welcome the customer with text and image. It will ask
    for their name, give a random response to it. It will take them through
    a series of questions to place their desired juice order. Finally, it will repeat their order
    back to them in text"""

    #1welcome statement + image
    print("Welcome to Juice-Bot-Café! \nMy name is 'Juice Bot 🍊🤖'\n")
    welcome_image_pop_up()
    #2name
    customer_name = order_name()
    #3random response to name, unless maker's name
    name_response = random_name_response(customer_name)

    #while loop to keep placing orders, in a list, until customer opts out
    order = 'y'
    juice_orders = []
    while order == 'y':
        #4juice flavour
        juice_flavour = order_juice_flavour()
        #5juice size
        juice_size = order_size()
        #6extra shot
        extra_shot = order_extra_shot()
        juice = (juice_flavour, juice_size, extra_shot)
        #add order to list
        juice_orders.append(juice)
        order = input('\nWould you like to place another order? y/n\n')
        if order == 'n':
            break

    #7read back order
    read_back_order(customer_name, juice, juice_orders)

def main():
    juice_bot()

if __name__ == '__main__':
    main()