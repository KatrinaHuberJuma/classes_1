"""This file should have our order classes in it."""

class AbstractMelonOrder(object):

    def __init__(self, species, qty, order_type, tax):
        """Runs as instantiation,tax is a decimal"""

        self.order_type = order_type
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax

    def get_total(self):
        """Calculate price."""
        base_price = 5
        base_price = base_price if self.species.lower() != "christmas melon" else base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""


    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty,"domestic", 
                                                 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 
                                                      0.17)

        self.country_code = country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        total = total if self.qty >= 10 else total + 3 
        # if self.qty < 10:
        #     total += 3
        return total


