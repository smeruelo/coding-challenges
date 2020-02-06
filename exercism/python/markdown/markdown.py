import re


def parse_chunck(chunck):
    def parse_bold(s):
        if m := re.match(r'(.*)__(.*)__(.*)', s):
            return f'{m.group(1)}<strong>{m.group(2)}</strong>{m.group(3)}'
        return s

    def parse_italic(s):
        if m := re.match(r'(.*)_(.*)_(.*)', s):
            return f'{m.group(1)}<em>{m.group(2)}</em>{m.group(3)}'
        return s

    return parse_italic(parse_bold(chunck))


def parse_line(line, in_list):
    if m := re.match(r'(\*) (.*)', line):
        if in_list:
            return (f'<li>{parse_chunck(line[2:])}</li>'), True
        return (f'<ul><li>{parse_chunck(line[2:])}</li>'), True

    end_list = '</ul>' if in_list else ''
    if m := re.match(r'(#{1,}) (.*)', line):
        k = len(m.group(1))
        return (f'{end_list}<h{str(k)}>{parse_chunck(line[k+1:])}</h{str(k)}>'), False
    return (f'{end_list}<p>{parse_chunck(line)}</p>'), False


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
