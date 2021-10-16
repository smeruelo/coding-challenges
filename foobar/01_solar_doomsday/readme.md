Solar Doomsday
==============

Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum antimatter reactor core with solar arrays, and you've been tasked with setting up the solar panels.

Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately, you have one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would leave 3 square yards, so you can turn those into three 1x1 square solar panels.

Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first. So, following the example above, solution(12) would return [9, 1, 1, 1].

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

|Input|Output|
|-|-|
|solution.solution(15324)|15129,169,25,1|
|solution.solution(12)|9,1,1,1|

Constraints
===========
- Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.
- Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.
- Input/output operations are not allowed.
- Your solution must be under 32000 characters in length including new lines and and other non-printing characters.
