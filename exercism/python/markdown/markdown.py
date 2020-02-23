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


def parse_line(line, in_list):
    """Process every line according its type: header / list item / paragraph."""

    # List item
    if m := re.match(LIST_REGEX, line):
        begin_list = '' if in_list else '<ul>'
        text = parse_text(line[2:])
        return (f'{begin_list}<li>{text}</li>'), True

    # If it's not a list item, it could be the end of one.
    end_list = '</ul>' if in_list else ''

    # Header
    if m := re.match(HEADER_REGEX, line):
        k = len(m.group(1))
        text = parse_text(line[k+1:])
        return (f'{end_list}<h{str(k)}>{text}</h{str(k)}>'), False

    # Paragraph
    text = parse_text(line)
    return (f'{end_list}<p>{text}</p>'), False


def parse(markdown):
    lines = markdown.split('\n')
    html = []
    in_list = False
    for line in lines:
        parsed, in_list = parse_line(line, in_list)
        html.append(parsed)
    if in_list:
        html.append("</ul>")
    return "".join(html)
