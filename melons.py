"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """Abstract class for DomesticMelonOrder and InternationalMelonOrder"""

    def __init__(self, species, qty, order_type, tax):        
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

               
    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""


    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        # self.species = species
        # self.qty = qty     
        # self.order_type = "domestic"
        # self.tax = 0.08
        
        #take the parameters passed to DomesticMelonOrder & pass default arguments 
        #to super class AbstractMelonOrder's __init__ & DomesticMelonOrder grabs
        #arguments that it doesn't already have
        #
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        # self.species = species
        # self.qty = qty
        self.order_type = "international"
        self.country_code = country_code
        self.tax = 0.17
        super(InternationalMelonOrder, self).__init__(species, qty)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code