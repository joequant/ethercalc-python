#!/usr/bin/env python3
import ethercalc
import pprint
pp = pprint.PrettyPrinter(indent=4)
e = ethercalc.EtherCalc("http://localhost:8000")
pp.pprint(e.cells("test"))
pp.pprint(e.export("test"))

