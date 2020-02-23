# https://exercism.io/my/solutions/b6a75144d4564342a627fabf078658c9

import re


BOLD_REGEX = r'__(.*?)__'
ITALIC_REGEX = r'_(.*?)_'
HEADER_REGEX = r'(#{1,}) (.*)'
LIST_REGEX = r'(\*) (.*)'


def parse_text(text):
    """Process the actual content of lines, regarless its type."""

    def replace(s, regex, tag):
        return re.sub(regex, fr'<{tag}>\1</{tag}>', s)

    def parse_bold(s):
        return replace(s, BOLD_REGEX, 'strong')

    def parse_italic(s):
        return replace(s, ITALIC_REGEX, 'em')

    return parse_italic(parse_bold(text))


def parse_line(line):
    """Process every line according its type: header / list item / paragraph."""

    # List item
    if m := re.match(LIST_REGEX, line):
        text = parse_text(line[2:])
        return f'<li>{text}</li>'

    # Header
    if m := re.match(HEADER_REGEX, line):
        k = len(m.group(1))
        text = parse_text(line[k+1:])
        return f'<h{str(k)}>{text}</h{str(k)}>'

    # Paragraph
    text = parse_text(line)
    return f'<p>{text}</p>'


def parse(markdown):
    lines = markdown.split('\n')
    html = []
    in_list = False
    for line in lines:
        list_item = bool(re.match(LIST_REGEX, line))
        list_tag = ''
        if not in_list and list_item:
            list_tag = '<ul>'
        elif in_list and not list_item:
            list_tag = '</ul>'
        parsed = parse_line(line)
        html.append(f'{list_tag}{parsed}')
        in_list = list_item
    if in_list:
        html.append("</ul>")
    return "".join(html)
