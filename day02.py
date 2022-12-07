import re

with open(__file__.replace(".py", "_data")) as f:
    data = [list(map(int, re.findall(r"\d+", line))) for line in f.readlines()]

# PART 1
print(sum(2*l*w + 2*w*h + 2*l*h + min(l*w, w*h, l*h) for l, h, w in data))

# PART 2
print(sum(l*w*h + min(2*(l+w), 2*(w+h), 2*(l+h)) for l, h, w in data))
