"""Currency data to be computed."""

__author__ = "Sahatsawat Kanpai 6210545629"
__email__ = "keyboard2543@gmail.com"

from enum import Enum


class Currency(Enum):
    """Currency Enumerator contains convert unit and currency name."""
    BAHT = {
        'unit': 1.000,
        'currency': 'Baht',
    }
    US_DOLLAR = {
        'unit': 0.033,
        'currency': 'US$'
    }
    EURO = {
        'unit': 0.0297,
        'currency': 'Euro'
    }
    YEN = {
        'unit': 3.5868,
        'currency': 'Yen'
    }

    def convert_to(self, amount, currency):
        """Convert this currency with amount to converted amount with given currency."""
        return amount / self.value['unit'] * currency.value['unit']

    def convert_to_in_string(self, amount, currency):
        """Convert this currency with amount to descriptive string."""
        return f"{self.convert_to(amount, currency):.2f} {currency.value['currency']}"

    def convert_to_all_in_string(self, amount):
        """Convert this currency with amount to all exist currency in this Enumerator except self currency."""
        msg = f"{amount} {self.value['currency']}"
        padding = ' ' * (len(msg) + 1)
        return_str = f"{msg} = "
        is_first_line = True
        for currency in Currency:
            if currency == self:
                continue
            if not is_first_line:
                return_str += padding + '= '
            return_str += self.convert_to_in_string(amount, currency) + '\n'
            is_first_line = False
        return return_str
