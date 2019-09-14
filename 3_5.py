print('Test1:')
def spam():
    eggs = 'spam local'
    print(eggs) # spam local
def bacon():
    eggs = 'bacon local'
    print(eggs) # bacon local
    spam() # spam local
    print(eggs) # bacon local
eggs = 'global'
bacon() # bacon local spam local bacon local
print(eggs) #global
print('=' * 10)
print('Test2:')
def spam():
    eggs = 'spam local'
    print(eggs) # spam local
def bacon():
    global eggs
    eggs = 'bacon local'
    print(eggs) # bacon local
    spam() # spam local
    print(eggs) # bacon local
eggs = 'global'
bacon() # bacon local spam local bacon local
print(eggs) #bacon global

