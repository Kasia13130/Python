class MemoryClass:

    def __init__(self, list):
        self.list_of_items = list

    def __call__(self, items):
        self.list_of_items.append(items)


mem = MemoryClass([])
print("List of items in memory", mem.list_of_items)

mem.list_of_items.append("buy sugar")
print("List of items in memory", mem.list_of_items)

mem("buy milk")
print("List of items in memory", mem.list_of_items)

mem("buy coffee")
print("List of items in memory", mem.list_of_items)

print("This class is callable:", callable(MemoryClass))
print("This class is callable:", callable(mem))             