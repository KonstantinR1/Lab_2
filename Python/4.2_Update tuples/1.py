x = ("apple", "banana", "cherry")
y = list(x)

y[1] = "kiwi"
x = tuple(y)

print(x) # It is worked due to this is list, no tuple.

"""
Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. 
You can convert the tuple into a list, change the list, 
and convert the list back into a tuple.
"""