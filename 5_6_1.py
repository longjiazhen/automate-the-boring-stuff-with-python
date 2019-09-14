#好玩游戏的物品清单
things = {'rope': 1,
         'touch': 6,
         'gold coin': 42,
         'dagger': 1,
         'arrow': 12}
def displayInventory(things):
    print('Inventory:')
    totalNum = 0
    """
    for k in things.keys():
        print(str(things[k]) + ' ' + k)
        totalNum += things[k]
    """
    for k ,v in things.items():
        print(str(v) + ' ' + k)
        totalNum += v
    print('Total number of items: ' + str(totalNum))
displayInventory(things)
