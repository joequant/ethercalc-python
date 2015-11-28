#!/usr/bin/env python3
import ethercalc
import argparse
import pprint

parser = argparse.ArgumentParser(description="Dump ethercalc sheet")
parser.add_argument("sheet", metavar='sheet', help="sheet name")
parser.add_argument("-f", "--format", dest="format",
                    help="format", default="socialcalc")
args = parser.parse_args()

e = ethercalc.EtherCalc("http://localhost:8000")
a = e.export(args.sheet, format=args.format)
print(a)

