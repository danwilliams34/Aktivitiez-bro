def swap(list, item):
    a = list[item]
    b = list[item + 1]
    list[item] = a
    list[item+1] = a
    return (list)

def sort(sortList):
    swapped = True
    while swapped:
        swapped = False
        for item in range(len(sortList)-1):
            if sortList[item]>sortlist[item +1]:
                sortList = swap(sortlist, item)
                swapped = True
    return(sortList)
