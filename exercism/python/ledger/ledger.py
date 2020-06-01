# -*- coding: utf-8 -*-
from datetime import datetime
from decimal import Decimal


class LedgerEntry:
    def __init__(self, date=None, description=None, change=None):
        self.date = date
        self.description = description
        self.change = change


def create_entry(date, description, change):
    return LedgerEntry(datetime.strptime(date, '%Y-%m-%d'), description, change)


TEXTS = {
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
#    "": {"en_US": "", "nl_NL": ""},
}


def format_currency(value, currency, locale):
    num = Decimal(value / 100)
    sign, digits, exp = num.quantize(Decimal('0.01')).as_tuple()

    sep = TEXTS["group_sep"][locale]
    def group(s_digits):
        if len(s_digits) < 3:
            s_digits = ['0'] * (abs(exp) + 1 - len(s_digits)) + s_digits
        rev_groups = [s_digits[::-1][i:i+3] for i in range(2, len(s_digits), 3)][::-1]
        before_coma = sep.join(map(lambda g: ''.join(reversed(g)), rev_groups))
        after_coma = ''.join(s_digits[-2:])
        return f"{before_coma}{TEXTS['dec_point'][locale]}{after_coma}"

    s_amount = group(list(map(str, digits)))
    s_sign = TEXTS["neg_sign"][locale] if sign == 1 else ''
    s_trail_sign = TEXTS["neg_trail_sign"][locale] if sign == 1 else ' '
    s_curr = TEXTS[currency][locale]
    if locale == 'en_US':
        return f'{s_sign}{s_curr}{s_amount}{s_trail_sign}'
    elif locale == 'nl_NL':
        return f'{s_curr}{s_sign}{s_amount}{s_trail_sign}'


def format_entries(currency, locale, entries):
    SEP = " | "
    # Generate Header Row
    table = (
        f'{TEXTS["date"][locale]:10}{SEP}'
        f'{TEXTS["description"][locale]:25}{SEP}'
        f'{TEXTS["change"][locale]:13}'
    )

    while len(entries) > 0:
        table += '\n'

        # Find next entry in order
        min_entry_index = -1
        for i in range(len(entries)):
            entry = entries[i]
            if min_entry_index < 0:
                min_entry_index = i
                continue
            min_entry = entries[min_entry_index]
            if entry.date < min_entry.date:
                min_entry_index = i
                continue
            if (
                entry.date == min_entry.date and
                entry.change < min_entry.change
            ):
                min_entry_index = i
                continue
            if (
                entry.date == min_entry.date and
                entry.change == min_entry.change and
                entry.description < min_entry.description
            ):
                min_entry_index = i
                continue
        entry = entries[min_entry_index]
        entries.pop(min_entry_index)

        # Write entry date to table
        table += entry.date.strftime(TEXTS["date_format"][locale])
        table += SEP

        # Write entry description to table
        # Truncate if necessary
        if len(entry.description) > 25:
            for i in range(22):
                table += entry.description[i]
            table += '...'
        else:
            for i in range(25):
                if len(entry.description) > i:
                    table += entry.description[i]
                else:
                    table += ' '
        table += SEP

        # Write entry change to table
        change = format_currency(entry.change, currency, locale)
        table += f'{change:>13}'
    return table
