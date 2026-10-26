def Legthword(s):


    s.strip()

    # s.split()

    words =s.split()

    last = words[-1]

    return len(last)

s = "ram ramesh"
print(Legthword(s))