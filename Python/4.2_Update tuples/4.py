thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")

thistuple = tuple(y)

# Converted the tuple into a list, removed "apple", and converted it back into a tuple.