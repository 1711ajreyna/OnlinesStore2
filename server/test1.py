name = "Andrew"
print(name)


def say_hello():
    print("Hello")
    print("I'm inside")

say_hello()

# data structures -> 114

# array js -> list python
prices =[3, 9, 5, 83, 79]

# add
prices.append(9)

print(prices)

# sum all the prices
total = 0 
for price in prices:
    total += price

print(total)

# dictionary

me = {
    "name": "Andrew",
    "Age": 33,
    "hobbies": [],
    "address": {
        "street": "5 palma vly",
        "city": "Coto De Caza"
    }
}

print(me)

# read
print(me["name"])

# warning: reading a key that does not exist
if "last" in me:
    print(me["last"])

# modify 
me["age"] = 99

# add keys
me["last"] = "Reyna"
    
print("THE END!!")