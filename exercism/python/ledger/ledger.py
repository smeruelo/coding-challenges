# -*- coding: utf-8 -*-
# https://exercism.io/my/solutions/60113f4a467146fe86acfdc7b61f6522
from datetime import datetime
from decimal import Decimal


class LedgerEntry:
    def __init__(self, date=None, description=None, change=None):
        self.date = date
        self.description = description
        self.change = change

    def __lt__(self, other):
        if self.date < other.date:
            return True
        elif self.date == other.date:
            if self.change < other.change:
                return True
            elif self.change == other.change:
                return self.description < other.description
        return False


# Stupid function, but necessary because it is used in the tests.
def create_entry(date, description, change):
    return LedgerEntry(datetime.strptime(date, '%Y-%m-%d'), description, change)


I18N = {
    "date": {"en_US": "Date", "nl_NL": "Datum"},
    "description": {"en_US": "Description", "nl_NL": "Omschrijving"},
    "change": {"en_US": "Change", "nl_NL": "Verandering"},
    "date_format": {"en_US": "%m/%d/%Y", "nl_NL": "%d-%m-%Y"},
    "USD": {"en_US": "$", "nl_NL": "$ "},
    "EUR": {"en_US": u"€", "nl_NL": u"€ "},
    "group_sep": {"en_US": ",", "nl_NL": "."},
    "dec_point": {"en_US": ".", "nl_NL": ","},
    "neg_sign": {"en_US": "(", "nl_NL": "-"},
    "neg_trail_sign": {"en_US": ")", "nl_NL": " "},
}


def format_currency(currency, locale, value):
    num = Decimal(value / 100)
    sign, digits, exp = num.quantize(Decimal('0.01')).as_tuple()

    def group(s_digits):
        if len(s_digits) < 3:
            s_digits = ['0'] * (abs(exp) + 1 - len(s_digits)) + s_digits
        rev_groups = [s_digits[::-1][i:i+3] for i in range(2, len(s_digits), 3)][::-1]
        before_coma = group_sep.join(map(lambda g: ''.join(reversed(g)), rev_groups))
        after_coma = ''.join(s_digits[-2:])
        return f"{before_coma}{dec_sep}{after_coma}"

    group_sep = I18N["group_sep"][locale]
    dec_sep = I18N['dec_point'][locale]
    s_amount = group(list(map(str, digits)))
    s_sign = I18N["neg_sign"][locale] if sign == 1 else ''
    s_trail_sign = I18N["neg_trail_sign"][locale] if sign == 1 else ' '
    s_curr = I18N[currency][locale]
    if locale == 'en_US':
        return f'{s_sign}{s_curr}{s_amount}{s_trail_sign}'
    elif locale == 'nl_NL':
        return f'{s_curr}{s_sign}{s_amount}{s_trail_sign}'


def format_entries(currency, locale, entries):
    SEP = " | "
    table = (
        f'{I18N["date"][locale]:10}{SEP}'
        f'{I18N["description"][locale]:25}{SEP}'
        f'{I18N["change"][locale]:13}'
    )

    for entry in sorted(entries):
        date = entry.date.strftime(I18N["date_format"][locale])
        descr = entry.description[:22] + '...' if len(entry.description) > 25 else entry.description
        change = format_currency(currency, locale, entry.change)
        table += f'\n{date:10}{SEP}{descr:25}{SEP}{change:>13}'
    return table
