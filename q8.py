"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t,, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""
start = ["c", "t", "b"]
middle = ["a", "o"]
end = ["p", "t", "n"]
for index in range(0,3):
    for index2 in range(0,3):
        for index3 in (0,1):
            print(start[index2] + middle[index3] + end[index])

"""
import random
for i in range (18):
    start = ["c", "t", "b"]
    start_r = random.choice(start)
    middle = ["a", "o"]
    middle_r = random.choice(middle)
    end = ["p", "t", "n"]
    end_r = random.choice(end)
    print(start_r, middle_r, end_r)
"""