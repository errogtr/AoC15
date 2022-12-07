with open(__file__.replace(".py", "_data")) as f:
    data = f.read()

# PART 1
print(sum(1 if c == '(' else -1 for c in data))

# PART 2
count = 0
for i, c in enumerate(data, 1):
    count += 1 if c == "(" else -1
    if count == -1:
        print(i)
        break
