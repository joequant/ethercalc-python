#!/usr/bin/env python3
import ethercalc
import argparse
import pprint
import sys
parser = argparse.ArgumentParser(description="Dump ethercalc sheet")
parser.add_argument("sheet", metavar='sheet', help="sheet name")
parser.add_argument("-f", "--format", dest="format",
                    help="format", default="socialcalc")
args = parser.parse_args()
data = sys.stdin.buffer.read()

e = ethercalc.EtherCalc("http://localhost:8000")
a = e.update(data, format=args.format, id=args.sheet)


