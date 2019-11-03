# Create dictionary containing current inventory
currInv = {
    'Bowling Ball': 21,
    'Dirty Sock': 2,
    'Hair Pin': 1,
    'Microphone': 5
}


# Create dictionary containing new stock
newInv = {
    'Hair Pin': 2,
    'Half-Eaten Apple': 3,
    'Bowling Ball': 67,
    'Toothpaste': 7
}


# Add new stock to current inventory
def mrgInv():
    updInv = {x: currInv.get(x, 0) + newInv.get(x, 0) for x in set(currInv).union(newInv)}
    return(updInv)

# Sort alphabetically by the product name of each item
def updateInventory():
    values = mrgInv().items()
    print(sorted(values))


# Invoke updateInventory() function to print new stock
updateInventory()