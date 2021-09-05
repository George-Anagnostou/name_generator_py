# Name Generator

import random

first_names = ["John", "Paul", "Michael", "George", "Sam", "Harry"]
last_names = ["Jacobson", "Peterson", "Papadopolous", "Spineli", "Greenbaum"]
titles = ["Mr.", "Mrs.", "Dr.", "H.M."]

name = ""

fn = random.choice(first_names)
ln = random.choice(last_names)
tl = random.choice(titles)

print(fn)
print(ln)
print(tl)
