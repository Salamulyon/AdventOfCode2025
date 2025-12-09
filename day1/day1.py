"""
Docstring for day1
It's basically splitting the inputs into two,the first is a letter and the second is a number
if the letter is L,we subract the number from the current value
if the letter is R,we add the number to the current value
the value is supposed to be from 0 - 99 and cyclic
so if the number goes below 0,it's supposed to count down from 99 instead and vice versa
count how many times the value reaches 0 and return that count
"""


dir = []
numbers = []
with open ("day1/day1_input.txt") as f:
    for line in f:
        dir.append(line[0])
        numbers.append(int(line[1:]))


val = 50
res = 0

i = 0
while i < len(dir):
    if dir[i] == "L":
        val -= numbers[i]
        if val < 0:
            val += 100
    else:
        val = (val + numbers[i]) % 100

    if val == 0:
        res += 1

    i += 1

print(res)