def swap(inlist, item):
    a = inlist[item]
    b = inlist[item + 1]
    inlist[item] = a
    inlist[item+1] = a
    return (inlist)

def sort(sortList):
    swapped = True
    while swapped:
        swapped = False
        for item in range(len(sortList)-1):
            if sortList[item]>sortlist[item +1]:
                sortList = swap(sortlist, item)
                swapped = True
    return(sortList)
