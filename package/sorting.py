def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    sorted_items = items
    for x in range(len(sorted_items)):
        for y in range(len(sorted_items)-1-x):
            if sorted_items[y] > sorted_items[y+1]:
                sorted_items[y], sorted_items[y+1] = sorted_items[y+1] , sorted_items[y]
    return sorted_items

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items)>1:
        mid = len(items)//2
        lside = items[:mid]
        rside = items[mid:]
        merge_sort(lside)
        merge_sort(rside)

        z=0
        y=0
        x=0
        while z < len(lside) and y < len(rside):
            if lside[z] < rside[y]:
                items[x]=lside[z]
                z=z+1
            else:
                items[x]=rside[y]
                y=y+1
            x=x+1
        
        while z < len(lside):
            items[x]=lside[z]
            z=z+1
            x=x+1

        while y < len(rside):
            items[x]=rside[y]
            y=y+1
            x=x+1
    return items

def quick_sort(items, index=-1):
    '''Return array of items, sorted in ascending order'''
    if len(items) <= 1:
        return items

    pivot = items[index]
    lows, tops, mids = [],[],[]
    for x in items:
        if x < pivot:
            lows.append(x)
        elif x > pivot:
            tops.append(x)
        elif x == pivot:
            mids.append(x)

    lows = quick_sort(lows)
    tops = quick_sort(tops)

    return lows + mids + tops
