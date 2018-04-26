#!/usr/bin/pypy3

# yaourt -S mgba-qt  (gameboy emulator)
# run file unknown.gb with mgba-qt --> see text
# open unknown.gb with hex editor --> look for text --> decode it (it's base64) --> pikalang
# translate pikalang into brainfuck:
# ".----->.------>..----<.+++++++++++<.----->.-------.++>.<.+>.+++<.----->.+++++++++++++++++++<.++++++++++>>>]-<<<<++++++++++>+++++++>+++>+>[++++++++++"
# Can't run it, syntax errors --> brackets the other way around!
# Pikachu picture is upside down, maybe brainfuck code too? yes!

print(".----->.------>..----<.+++++++++++<.----->.-------.++>.<.+>.+++<.----->.+++++++++++++++++++<.++++++++++>>>]-<<<<++++++++++>+++++++>+++>+>[++++++++++"[::-1])
