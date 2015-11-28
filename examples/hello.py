#!/usr/bin/env python3
import ethercalc
import pprint
pp = pprint.PrettyPrinter(indent=4)
e = ethercalc.EtherCalc("http://localhost:8000")
e.command("test", ["set C1 value n 2"])
pp.pprint(e.cells("test"))
pp.pprint(e.cells("test", "A1"))
e.command("test", [ ethercalc.set("C1", 2),
                    ethercalc.set("C2", 2),
                    ethercalc.set("C3", "=C1+C2") ])
pp.pprint(e.export("test"))
