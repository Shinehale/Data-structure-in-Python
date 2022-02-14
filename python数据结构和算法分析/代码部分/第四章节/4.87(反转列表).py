def reverse(ansList, tarList, pos):
    if pos == len(ansList):
        return
    reverse(ansList, tarList, pos + 1)
    tarList.append(ansList[pos])


new_ = [i * i for i in range(15) if i != 0]
after = []
reverse(new_, after, 0)
print(new_)
print(after)
