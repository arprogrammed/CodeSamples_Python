def intestrip(list):
    inteonly = [int(init) for init in list]
    return sum(inteonly)

uglydata = ['21', '14', '27']

print(intestrip(uglydata))

def joinphrase(a, b):
    if isinstance(a, str) and isinstance(b, str):
        string = "{} {}".format(a, b)
        return string
    else:
        return 'Error strings only.'

print(joinphrase('boo', 'you'))

def aver(*args):
    av = sum(args) / len(args)
    return av

print(aver(10, 12, 14, 21))

def ss(*args):
    capa = [argis.upper() for argis in args]
    return sorted(capa)

print(ss('hoo', 'boo'))

def search(skey, path):
    with open(path) as sindex:
        content = sindex.read()
        count = content.count(skey)
        return count

print(search('p', 'fruit.txt'))

with open("data.txt", "a+") as newlines:
    newlines.seek(0)
    content = newlines.read()
    newlines.write(content)
    newlines.write(content)
