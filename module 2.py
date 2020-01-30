items = {'chicken 8pc': {'price': 17.99, 'modifications': 'All Winds', 'description': '1 Large Side and 4 Biscuits'},
         'chicken 16pc': {'price': 37.99, 'modifications': 'All Winds', 'description': '3 Large Side and 8 Biscuits'},
         'Cajun Fries': {'price': 3.99, 'modifications': 'N/A', 'description': 'French Fries'},
         'Spicy Garlic Butterfly Shrimp – Combo': {'price': 6.49, 'modifications': 'N/A', 'description': 'shrimp'},
         'Cajun Fries': {'price': 3.99, 'modifications': 'N/A', 'description': 'French Fries'},
         'Spicy Garlic Butterfly Shrimp – Combo': {'price': 6.49, 'modifications': 'N/A', 'description': 'shrimp'},
         'Spicy Garlic Butterfly Shrimp – Platter': {'price': 8.39, 'modifications': 'N/A', 'description': 'shrimp'},
         'Red Beans & Rice': {'price': 3.99, 'modifications': 'N/A', 'description': 'Beans & Rice'},
         'Biscuits 12 pc': {'price': 6.99, 'modifications': 'N/A', 'description': 'Biscuits'},
         'Soft Drink': {'price': 2.29, 'modifications': 'Cola, Fenta, Sprite,Pepsi', 'description': 'drink'},
         'Chicken Po’Boy – Combo': {'price': 6.49, 'modifications': 'N/A', 'description': 'sandwich'}
         }


# Print a list of all the items available on the menu
def menu():
    print(list(items.keys()))


# The price and description based on the name
def price_and_description(item):
    print("This {} include {}".format(item, items[item]['description']))
    print("The price of {} is ${}".format(item, items[item]['price']))


# The modification available based on the name of the item
def modification(item):
    print("The modification of {} is {}".format(item, items[item]['modification']))


if __name__ == "__main__":
    while True:
        menu()
        choice = input("Please choose one item you want to query: ")
        print(price_and_description(choice))
        ifQuit = input("Choose this? yes/no: ")
        if ifQuit.lower() == 'yes':
            break






