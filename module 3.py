class Order:
    def __init__(self, items):
        self.order = {}
        self.items = items

    def add(self, item, quantity=1):
        self.order[item] = self.order.get(item, 0) + quantity

    def modify(self, item, quantity=1):
        self.order[item] = quantity

    def remove(self, item):
        if item not in self.order:
            print("Did not order {}".format(item))
        del self.order[item]

    def start_over(self):
        self.order = {}

    def checkout(self):
        total = 0
        with open('order.txt', 'w') as f:
            f.write(";item;quantity;total\n")
            for item in self.order:
                count = self.order[item]
                single_price = self.items[item]['price']
                total += count * single_price
                f.write("N/A; {}; {}; {}\n".format(item, count, count * single_price))

            f.write("Tax; N/A; N/A; {}\n".format(count * single_price * 0.1))
            f.write("Total amount; N/A; N/A; {}\n".format(count * single_price * 1.1))
            total *= 1.1
        print("The total is {}".format(total))
        return total


if __name__ == "__main__":
    order = Order(items)
    order.add("chicken 8pc")
    order.checkout()