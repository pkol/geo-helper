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

class Addr2Geo:
	PACE = 1
	FNAME_CACHE="addr2geo-cache.pickle"
	def __init__(self):
		try:
			self.cache = pickle.load(open(self.FNAME_CACHE,"r"))
		except Exception:
			self.cache = {}
		self.opener = urllib.URLopener(version="mining public data")
		self.last = 0

	def filter(self, addr):
		return addr

	def addr2Geo(self, addr):
		addr = self.filter(addr)
		if addr in self.cache:
			resp = self.cache[addr]
		else:
			now = time.time()
			time.sleep( max(self.last + self.PACE - now, 0))
			self.last = now
			
			print "from server"
			base = "http://nominatim.openstreetmap.org/search/?"
			query = urllib.urlencode({"q":addr.encode('utf8'), "format":"json"})
			print query
			fd = self.opener.open(base+query)
			resp = json.loads(fd.read())
			self.cache[addr] = resp
			if len(self.cache) % 10 ==0:
				self.save()
		if len(resp) == 0:
			print "NIEZNANY %s " % (addr)
		resp = resp[0]
		return( resp["lat"] , resp["lon"])

	def save(self):
		pickle.dump(self.cache,open(self.FNAME_CACHE+".new","w"))
		try: os.unlink(self.FNAME_CACHE)
		except Exception: pass
		os.rename(self.FNAME_CACHE+".new", self.FNAME_CACHE)

