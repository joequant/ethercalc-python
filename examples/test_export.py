#!/usr/bin/env python3
import ethercalc
import pprint
pp = pprint.PrettyPrinter(indent=4)
e = ethercalc.EtherCalc("http://localhost/calc")
pp.pprint(e.cells("daily"))
pp.pprint(e.export("daily"))

