from random import randint

"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    shipped = False
    # base_price = 5

    def __init__(self, species, qty):
        """Runs as instantiation,tax is a decimal"""

        self.species = species
        self.qty = qty

    def get_base_price(self):
        return randint(5, 9)

    def get_total(self):
        """Calculate price."""
        self.base_price = self.get_base_price()
        self.base_price = self.base_price if self.species.lower() != "christmas melon" else self.base_price * 1.5
        total = (1 + self.tax) * self.qty * self.base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08


    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        total = total if self.qty >= 10 else total + 3 
        # if self.qty < 10:
        #     total += 3
        return total


class GovermentMelonOrder(AbstractMelonOrder):
    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):
        self.passed_inspection = passed