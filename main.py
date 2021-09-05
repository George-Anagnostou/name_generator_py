# Name Generator

import random

first_names = ["John", "Marcus", "Giacommo", "Gordon", "Samuel", "Marvy"]
last_names = ["Jacobson", "Peterson", "Papadopolous", "Spineli", "Greenbaum"]
titles = ["Mr.", "Mrs.", "Dr.", "H.M."]

fn = random.choice(first_names)
ln = random.choice(last_names)
tl = random.choice(titles)

print(tl + " " + fn + " " + ln)
