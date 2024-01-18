class myclass():
  def __len__(self):
    return 0

# return 0     Result - False
# return 1     Result - True

myobj = myclass()
print(bool(myobj))