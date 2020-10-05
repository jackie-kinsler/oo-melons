"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract class for other order classes to inherit from."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'christmas':
            base_price *= 1.5 


        total = (1 + self.tax) * self.qty * base_price
        
        if self.country_code != 'USA' and self.qty < 10: 
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, 'USA')
        self.order_type = "domestic"



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder): 

    passed_inspection = False 

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = 'USA'
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.00

    def mark_inspection(self, passed): 
        if passed == True: 
            self.passed_inspection = True 
        else: 
            self.passed_inspection = False 