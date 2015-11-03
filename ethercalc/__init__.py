import requests

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
    
