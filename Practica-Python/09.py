#(Array Inverso)
#items[:] => Crea una copia del array
#items[::-1]=> Crea una copia inversa del array
def reverse_array(items):
    arrayReverso = items[::-1]
    return arrayReverso


def test(items):
    items_copy = items[:]
    reversed = reverse_array(items)
    print(f"{items_copy} reversed is: {reversed}")

test(["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"])
test(["Haste Potion", "Longsword", "Iron Bar", "Leather Scraps"])
test([1, 2, 300, 4, 5])
test(["now!", "order", "reverse", "in", "is", "Array", "This"])
test(["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"])
