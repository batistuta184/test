a = [32,12,34,-1,10,50]
def pao(lists):
    for i in xrange(len(lists)):
        for j in xrange(i,len(lists)):
            if lists[i] >= lists[j]:
                lists[i] , lists[j] = lists[j],lists[i]
    return lists
print pao(a)
def quick(lists,left,right):
    if left >= right:
        return lists
    low,high = left,right
    key = lists[low]
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left <  right  and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick(lists,low,left-1)
    quick(lists,left+1,high)
    return lists
print quick(a,0,len(a)-1)
def merge_sort(a,b):
    result = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def merge(lists):
    if len(lists) <= 1:
        return lists
    mid = int(len(lists)/2)
    left = merge(lists[:mid])
    right = merge(lists[mid:])
    return merge_sort(left,right)
print merge(a)
def insort(lists):
    for i in xrange(1,len(lists)):
        j = i
        key = lists[j]
        while lists[j-1] >= key and j >0 :
            j -= 1
        lists.insert(j,key)
        lists.pop(i+1)
    return lists
print insort(a)