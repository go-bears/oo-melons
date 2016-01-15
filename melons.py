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
        
        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == "international" and self.qty < 10:
            total += 3

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


"""

part 3

create class GovernmentMelonOrder(AbstractMelonOrder)
include variable passed_inspection = False

create method inspect_melons(takes in a Boolean) 

 and inspect_melons updates passed_inspection variable
 set tax = 0
takes in passed_inspection variable
 

splurge prices:

need random_int (5,10)
random_int needs to be an instance attribute

add to AbstractMelonOrder() class:
get_base_price method
update get_total() to include get_base_price method



"""