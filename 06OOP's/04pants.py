class Pants:
    """The Pants class represents an article of clothing sold in a store
    """
    
    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object
    
        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)
            
        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        """
            
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
    
    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object
    
        Args: 
            new_price (float): the new price of the pants object
            
        Returns: None
        
        """
        self.price = new_price
    
    def discount(self, percentage):
        """The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price * (1 - percentage)
    
def check_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12
    
    pants.change_price(10) == 10
    assert pants.price == 10 
    
    assert pants.discount(.1) == 9
    
    print('You made it to the end of the check. Nice job!')

check_results()