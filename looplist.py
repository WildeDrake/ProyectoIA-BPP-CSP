class llist(list):
    def __init__(self, r=[]):
        list.__init__(self, r)

    def __getitem__(self, n):
        n %= len(self)
        return super(llist, self).__getitem__(n)

    def __setitem__(self, n, v):
        n %= len(self)
        return super(llist, self).__setitem__(n, v)





def main():
    l = llist([1, 2, 3, 4])
    for i in l:
        print(i)
        if i % 2 == 1:
            l.append(len(l) + 1)

if __name__ == "__main__":
    main()