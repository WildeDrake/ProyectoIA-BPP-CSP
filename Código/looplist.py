class looplist(list):
    def __init__(self, r=[]):
        list.__init__(self, r)

    def __getitem__(self, n):
        n %= len(self)
        return super(looplist, self).__getitem__(n)

    def __setitem__(self, n, v):
        n %= len(self)
        return super(looplist, self).__setitem__(n, v)