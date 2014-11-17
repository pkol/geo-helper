#!/usr/bin/python
# coding=utf8
#
# (C) Paweł Kołodziej <p.kolodziej@gmail.com>
#

import urllib
import json
import pickle
import csv
import time
import logging
import os
import re

from addr2geo import Addr2Geo

class Addr2GeoStraz(Addr2Geo):
	def filter(self, addr):
		addr = re.sub("WILLIAMA  SZEKSPIRA", "WILIAMA  SZEKSPIRA", addr)
		addr = re.sub("STEFANA BATOREGO,OCHOTA", "STEFANA BATOREGO,MOKOTÓW", addr)
		addr = re.sub("1920 R.", "1920 ROKU", addr)
		addr = re.sub("^GEN.", "GENERAŁA", addr)
		addr = re.sub("^MJR.", "MAJORA", addr)
		addr = re.sub("SOSNKOWSKIEGO KAZIMIERZA, GEN.", "GENERAŁA SOSNKOWSKIEGO KAZIMIERZA", addr)

		addr = re.sub("AL. ARMII KRAJOWEJ,BIELANY", "AL. ARMII KRAJOWEJ,ŻOLIBORZ", addr)
		addr = re.sub("JULIANA KONSTANTEGO  ORDONA", "JULIUSZA KONSTANTEGO ORDONA", addr)
		addr = re.sub("PAWLIKOWSKIEJ-", "", addr)
		return addr



def main():
	a=Addr2GeoStraz()

	writer = csv.writer(open("straz_2013.csv","w"))
	reader = csv.reader(open("example_data/straz2013.csv"), delimiter=";")
	row = reader.next()
	row.extend(["lat", "lon"])
	writer.writerow(row)

	for row in reader:
		row = [ unicode(c, 'utf-8') for c in row]
		addr= ",".join( (row[4],row[3],"Warsaw","Poland"))
		try:
			geo = a.addr2Geo(addr)
		except Exception:
			#logging.exception("haha")
			continue
		row.extend(geo)
		writer.writerow([s.encode("utf-8") for s in row])
	a.save()
	


main()
