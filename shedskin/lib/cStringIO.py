# Copyright 2005-2011 Mark Dufour and contributors; License MIT (See LICENSE)


class StringI(file):
    pass

def StringIO(s=''):
    return StringI(s)

