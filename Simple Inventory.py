

inventory = []

def add_item():
    item = input('Enter item: ')
    location = input('Enter Location: ')
    inventory.append(item.lower())
    inventory.append(location.lower())

def remove_item():
    item = input('Enter item to be removed: ')
    index = inventory.index(item)    
    inventory.pop(index)
    inventory.pop(index+1)



print(inventory)

add_item()

print(inventory)

remove_item()

print(inventory)