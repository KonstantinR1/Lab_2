x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# .symmetric_difference_update() method will keep only the elements that are NOT present in both sets.