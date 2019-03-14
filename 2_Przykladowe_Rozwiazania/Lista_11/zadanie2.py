class Frob(object):

    def __init__(self):
        self.bab = 1

    def __getattribute__(self, name):
        print "getting `{}`".format(str(name))

class Frob2(object):

    def __init__(self):
        self.bab = 1

    def __getattr__(self, name):
        print "no such attribute".format(str(name))

f = Frob()

f.bab

f = Frob2()

f.bab2