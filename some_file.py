def f1(l, t):
    l[0] = l[0] + t[0]
    l[1][0] = l[1][0] + t[1][0]
    l[1][1] = l[1][1] + t[1][1]
    t = (l[0], ((l[1][1]), l[1][0]))
    print(l)
    print(t)
def main():
    a, b, c = 1, 2, 3
    li = [a, [b, c]]
    tu = (a, (b, c))
    print(li)
    print(tu)
    f1(li,tu)
    print(li)
    print(tu)
    li[0] = li[0] + tu[0]
    li[1][0] = li[1][0] + tu[1][0]
    li[1][1] = li[1][1] + tu[1][1]
    tu = (li[0], ((li[1][1]), li[1][0]))
    print(li)
    print(tu)
    f1(li, li)
    print(li)
    print(tu)
    print(li)
main()