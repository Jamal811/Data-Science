class item:
    # class attribute
    pay_rate = 0.8 # The pay rate after 20% discount
  
    # constructor
    def __init__(self, name: str, price: float, quantity=0):
       
        # Run validations to the  received arguments
        assert price >= 0, f"Price {price} should be a positive number not negative"
        assert quantity >= 0, f"Quantity {quantity} should be a positive number not negative"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate # you can use item.self_rate but you cant change it in instance level in order to apply different discount for another item
        
        
item1 = item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)
# print(item1.calculate_total_price())

item2 = item("Laptop", 500, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
#print(item2.calculate_total_price())

print(item.pay_rate)
print(item1.pay_rate) # if it could'nt find the value instance attribute assigned to it, then it will go ahead and look in class attribute
print(item2.pay_rate)

# use this for debugging resons to look at all the attributes from clas based and instance based
print(item.__dict__) # All the  attributes  for class level
print(item1.__dict__) # All the  attributes  for instance level



