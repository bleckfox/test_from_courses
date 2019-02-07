#page number 159
#inventory.py
# дописать (сложить количество стафа в двух словарях)
stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
    }

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

displayInventory(stuff)    
print('')
dragonLoot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby'
    ]
def add_to_inventory(inventory, addedItems):
    print('Added inventory:')
    AddItem = {}
    for item in addedItems:
        AddItem.setdefault(item,0)
        AddItem[item] = AddItem[item] + 1
        
    totalAdd = 0
    for k,v in AddItem.items():
        print(str(v) + ' ' + k)
        totalAdd += 1
    print('Total number of add items: ' + str(totalAdd))
    print('')
    
add_to_inventory(stuff, dragonLoot)
