with open(__file__.replace(".py", "_data")) as f:
    data = f.read()

# PART 1
print(sum(1 if c == '(' else -1 for c in data))

# PART 2
print(next(i for i in range(len(data)) if sum(1 if c == '(' else -1 for c in data[:i]) == -1))
