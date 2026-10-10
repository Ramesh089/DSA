def reverArr(l, r):
    if l >= r:
        return

    a[l], a[r] = a[r], a[l]

    reverArr(l + 1, r - 1)


a = [1, 2, 3, 4, 5]
reverArr(0, len(a) - 1)

print(a)