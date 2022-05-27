print("basic")
print(list("python"))

lst = list("python")
for i in lst:
    print(i, "*" * (ord(i) - ord("a")))