#列表到字典的函数，针对好玩游戏物品清单
things = {'rope': 1,
         'touch': 6,
         'gold coin': 42,
         'dagger': 1,
         'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory, addItems):
    #inventory是一个字典，代表玩家的物品清单，addItems是一个列表
    #返回一个字典，表示更新过的物品清单
    for i in addItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] =  1
    return inventory
def displayInventory(stuff):
    print('Inventory:')
    totalNum = 0
    for k ,v in stuff.items():
        print(str(v) + ' ' + k)
        totalNum += v
    print('Total number of items: ' + str(totalNum))
displayInventory(addToInventory(things, dragonLoot))
