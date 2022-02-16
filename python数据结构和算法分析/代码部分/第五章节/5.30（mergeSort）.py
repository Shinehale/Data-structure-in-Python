import random


def mergeSort(L, R, Lis):
    if L != R:
        mid = (L + R) // 2
        mergeSort(L, mid, alist)
        mergeSort(mid + 1, R, alist)

        i = L
        j = mid + 1
        s = []
        while i <= mid and j <= R:
            if Lis[i] < Lis[j]:
                s.append(Lis[i])
                i = i + 1
            else:
                s.append(Lis[j])
                j = j + 1
        while i <= mid:
            s.append(Lis[i])
            i = i + 1
        while j <= R:
            s.append(Lis[j])
            j = j + 1
        for i in range(len(s)):
            Lis[L + i] = s[i]


def generate(List):
    for i in range(20):
        newValue = random.randint(1, 5000)
        List.append(newValue)


alist = []
generate(alist)
mergeSort(0, len(alist) - 1, alist)
print(alist)
