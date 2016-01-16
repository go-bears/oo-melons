import random

"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """Abstract class for DomesticMelonOrder and InternationalMelonOrder"""
    
    def __init__(self, species, qty, order_type, tax):        
        """attributes set for each instantiated object"""    

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False
        self.is_splurge_pricing = False
        self.random_splurge_pricing = random.choice(range(6, 10))

    def get_base_price(self):
        """sets base_price under normal and splurge conditions """

        self.base_price = 5
        
        if self.is_splurge_pricing == True:
            self.base_price = self.random_splurge_pricing

        return self.base_price


    def get_total(self):
        """Calculate price."""

        self.base_price = self.get_base_price()   

        if self.species == "Christmas melon":
            self.base_price = self.base_price * 1.5

        total = (1 + self.tax) * self.qty * self.base_price
        
        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


    def set_splurge_pricing(self):
        """Set splurge pricing to true."""

        self.is_splurge_pricing = True    



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
        #self.order_type = "international"
        self.country_code = country_code
        #self.tax = 0.17
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """Class contains inspect_melons method and checks if melons were inspected  """

    def __init__(self, species, qty):
        self.passed_inspection = False
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0.00)

    def inspect_melons(self):
        self.passed_inspection = True