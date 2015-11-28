import requests
import json

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
        return r
    def post(self, id, data, content_type):
        r = requests.post(self.root + "/_" + id,
                          data=data,
                          headers={"Content-Type" : content_type})
        r.raise_for_status()
        return r
    def put(self, id, data, content_type):
        r = requests.put(self.root + "/_" + id,
                          data=data,
                          headers={"Content-Type" : content_type})
        r.raise_for_status()
        return r
    def cells(self, page, coord=None):
        api = ("/%s/cells" % page)
        if coord != None:
            api = api + "/" + coord
        return self.get(api).json()
    def command(self, page, command):
        r = requests.post(self.root + "/_/%s" % page,
                          json = {"command" : command})
        r.raise_for_status()
        return r.json()
    def create(self, data, format="python", id=None):
        if id == None:
            id = ""
        else:
            id = "/" + id
        if format == "python":
            return self.post(id, json.dumps({"snapshot": data}),
                             "application/json")
        elif format == "json":
            return self.post(id, data, "application/json")
        elif format == "csv":
            return self.post(id, data, "text/csv")
        elif format == "socialcalc":
            return self.post(id, data, "text/x-socialcalc")
        elif format == "excel":
            return self.post(id, data, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    def update(self, data, format="python", id=None):
        if id == None:
            sid = ""
        else:
            sid = "/" + id
        if format == "python":
            return self.put(sid, json.dumps({"snapshot": data}),
                             "application/json")
        elif format == "json":
            return self.put(sid, data, "application/json")
        elif format == "csv":
            return self.put(sid, data, "text/csv")
        elif format == "socialcalc":
            if id == None:
                upload = {"snapshot" : data}
            else:
                upload = {"room": id, "snapshot" : data}
            return self.post(id, json.dumps(upload),
                             "application/json")
        elif format == "excel":
            return self.put(sid, data, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    def export(self, page, format="python"):
        if format == "python":
            return self.get("/" + page + "/csv.json").json()
        elif format == "json":
            return self.get("/" + page + "/csv.json").text
        elif format == "socialcalc":
            return self.get("/" + page).text
        elif format == "html":
            return self.get("/" + page + "/html").text
        elif format == "csv":
            return self.get("/" + page + "/csv").text
        elif format == "xlsx":
            return self.get("/" + page + "/xlsx").text
        elif format == "md":
            return self.get("/" + page + "/md").text
        else:
            raise ValueError

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    e = Ethercalc("http://localhost:8000")
    pp.pprint(e.cells("test"))
    pp.pprint(e.cells("test", "A1"))
    pp.pprint(e.export("test"))
    
