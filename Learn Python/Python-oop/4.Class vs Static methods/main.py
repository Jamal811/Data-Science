import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # append all items to this list
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self) # append items to this list
        
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    # read csv
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
        
        # for item in items:
        #     print(item)
    @staticmethod
    def is_integer(num): # the static methods are never sending in the background the instance as a first aurgument, not like class methods which send the class refrence as the first aurgument
        
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"item ('{self.name}', '{self.price}, '{self.quantity}'')"

print(Item.is_integer(4.5))
# Item.instantiate_from_csv()
# print(Item.all)

