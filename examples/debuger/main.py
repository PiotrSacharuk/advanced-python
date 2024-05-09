class ItemListClass:
    def __init__(self, item_list=[]):
        self.item_list = item_list[:]

# import pdb; pdb.set_trace()

for item in range(4):
    obj = ItemListClass()
    obj.item_list.append(item)
    print(obj.item_list)
