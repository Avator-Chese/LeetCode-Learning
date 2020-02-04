def romanToint(x: str) -> int:
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    va = 0
    for i, n in enumerate(x):
        if i+1<=len(x)-1:
            if d.get(x[i]) < d.get(x[i + 1]):
                va = va - d.get(x[i])
            else:
                va = va + d.get(x[i])
        else:
            va=va+d.get(x[i])
    print(va)

romanToint("MCMXCIV")
