class SuperpowerProduct:
    def __init__(self, name, description, stock_quantity, buying_price, selling_price, manufacturer, id = None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.manufacturer = manufacturer
        self.id = id

    def full_name_and_description(self):
        return f"{self.name} {self.description}"
    
    
        