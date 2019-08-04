import operator
import lxml.html
import requests
import requests.cookies

URL_REQ = 'http://challenge01.root-me.org/programmation/ch1/'
URL_ANS = 'http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result='
OPS = {'+': operator.add, '-': operator.sub}


def series(n, u0, op, addend, multiplicand):
    def ui(i, prev):
        return op(addend + prev, ((i - 1) * multiplicand))

    term = u0
    for i in range(1, n+1):
        term = ui(i, term)
    return term


if __name__ == '__main__':
    web = requests.get(URL_REQ)
    cookies = web.cookies
    tree = lxml.html.fromstring(web.content)
    n = int(tree.xpath('/html/body/sub[4]/text()')[0])
    u0 = int(tree.xpath('/html/body/text()[5]')[0].split('=')[1])
    op = OPS[tree.xpath('/html/body/text()[3]')[0].split(' ] ')[1][0]]
    addend = int(tree.xpath('/html/body/text()[2]')[0].split('[')[1].split('+')[0])
    multiplicand = int(tree.xpath('/html/body/text()[3]')[0].split('*')[1].split(']')[0])
    result = series(n, u0, op, addend, multiplicand)
    web = requests.get(f'{URL_ANS}{result}', cookies=cookies)
    print(web.text)
