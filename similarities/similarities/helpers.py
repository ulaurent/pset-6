def lines(a, b):
    """Return lines in both a and b"""
    asplit = a.splitlines()
    bsplit = b.splitlines()
    compareLines = []

    for i in range (len(asplit)):
            if asplit[i] == bsplit[i]:
                compareLines.append(asplit[i])

    # TODO
    return compareLines


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    return []


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
