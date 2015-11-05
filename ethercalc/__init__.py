import requests

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
         pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def set(coord, item):
    if isinstance(item, float):
        return ("set %s value n %f" % (coord, item))
    elif isinstance(item, int):
        return ("set %s value n %d" % (coord, item))
    elif isinstance(item, str) or isinstance(item, unicode):
        if item == "":
            return ("set %s empty" % coord)
        elif item[0] == "'":
            return ("set %s text t %s" % (coord, item[1:]))
        elif item[0] == "=":
            return ("set %s formula %s" % (coord, item[1:]))
        elif is_number(item):
            return("set %s value n %s" % (coord, item[1:]))
        return("set %s text t %s" %item)

class EtherCalc(object):
    def __init__(self, url_root):
        self.root = url_root
    def get(self, cmd):
        r = requests.get(self.root + "/_" +cmd)
        r.raise_for_status()
        return r.json()
    def cells(self, page, coord=None):
        api = ("/%s/cells" % page)
        if coord != None:
            api = api + "/" + coord
        return self.get(api)
    def command(self, page, command):
        r = requests.post(self.root + "/_/%s" % page,
                          json = {"command" : command})
        r.raise_for_status()
        return r.json()
    def export(self, page, format="json"):
        if format == "json":
            return self.get("/" + page + "/csv.json")
        else:
            raise ValueError

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    e = Ethercalc("http://localhost:8000")
    pp.pprint(e.cells("test"))
    pp.pprint(e.cells("test", "A1"))
    pp.pprint(e.export("test"))
    
