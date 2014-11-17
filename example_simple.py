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

def main():
	a=Addr2Geo()

	print(a.addr2Geo(u"Lwa Tołstoja,Bielany,Warsaw,Poland"))
	print(a.addr2Geo(u"Ostrobramska,Warszawa,Poland"))
	print(a.addr2Geo(u"Legionowo,Poland"))
	
	a.save()
	


main()
