class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    
    @classmethod
    def margheritha(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
    




print(Pizza(['chesse', 'tomatoes']))

print(Pizza.margheritha())
 
print(Pizza.prosciutto())
