"""Assertion is a debug tool, no a  mechanism for handling errors"""

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    
    assert 0 <= price <= product['price'] #if not, raise assertion 
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900} #cents

print(apply_discount(shoes, 0.25))

print(apply_discount(shoes, 2.0)) #200%


