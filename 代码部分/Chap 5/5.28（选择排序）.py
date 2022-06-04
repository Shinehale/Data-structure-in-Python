import random


def selectionSort(List):
    for fillSlot in range(len(List) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillSlot + 1):
            if List[location] > List[positionOfMax]:
                positionOfMax = location
        List[fillSlot], List[positionOfMax] = List[positionOfMax], List[fillSlot]


def generate(List):
    for i in range(30):
        newValue = random.randint(1, 5000)
        List.append(newValue)


alist = []
generate(alist)
print("排序前的数组：\n", alist)
selectionSort(alist)
print("排序后的数组：\n", alist)
