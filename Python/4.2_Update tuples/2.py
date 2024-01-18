thistuple = ("apple", "banana", "cherry")
y = list(thistuple)

y.append("orange")
thistuple = tuple(y)

# Converted the tuple into a list, added "orange", and converted it back into a tuple.