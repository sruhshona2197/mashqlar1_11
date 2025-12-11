# 1-mashq
tuple(i*i for i in range(1, 21) if i % 2 == 0)

# 2-mashq
tuple(i for i in range(1, 51) if i % 3 == 0)

# 3-mashq
words = ["python", "tuple", "set", "loop"]
tuple(len(w) for w in words)

# 4-mashq
tuple(i for i in range(1, 101) if sum(map(int, str(i))) % 2 == 0)

# 5-mashq
words = ["python", "tuple", "set", "loop"]
tuple(w[0] for w in words)
