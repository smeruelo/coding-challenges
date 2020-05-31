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
    "neg_trail_sign": {"en_US": ")", "nl_NL": ""},
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
    s_trail_sign = TEXTS["neg_trail_sign"][locale] if sign == 1 else ''
    s_curr = TEXTS[currency][locale]
    if locale == 'en_US':
        return f'{s_sign}{s_curr}{s_amount}{s_trail_sign}'
    elif locale == 'nl_NL':
        return f'{s_curr}{s_sign}{s_amount}'


def format_entries(currency, locale, entries):
    SEP = " | "
    if locale == 'en_US':
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
            if currency == 'USD':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += TEXTS[currency][locale]
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += TEXTS[currency][locale]
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        return table
    elif locale == 'nl_NL':
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
            if currency == 'USD':
                change_str = TEXTS[currency][locale]
                if entry.change < 0:
                    change_str += '-'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = TEXTS[currency][locale]
                if entry.change < 0:
                    change_str += '-'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        return table
