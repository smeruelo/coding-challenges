#!/usr/bin/python2
# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

class Node:
    def __init__(self, freq, data, left = None, right = None):
        self.freq = freq
        self.data = data
        self.left = left
        self.right = right

def decode_huffman(root, s):
    output = ''
    index = 0
    while index < len(s):
        current = root
        while current.left or current.right:
            if s[index] == '0':
                current = current.left
            else:
                current = current.right
            index += 1
        output += current.data
    print output


if __name__ == '__main__':
    ht = Node(5, None, Node(2, None, Node(1, 'B'), Node(1, 'C')), Node(3, 'A'))
    decode_huffman(ht, '1001011'), 'ABACA'
    decode_huffman(ht, '')
    decode_huffman(ht, '11')
    decode_huffman(ht, '000000')
