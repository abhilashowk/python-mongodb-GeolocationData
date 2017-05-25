#!/usr/bin/python2.7
#
# Assignment3 Interface
# Name: ABHILASH OWK
#

from pymongo import MongoClient
import os
import sys
import json
import math
import codecs
reload(sys)
sys.setdefaultencoding("utf8")

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
	cur=collection.find({"city":cityToSearch})
	f=open(saveLocation1,'w')
	for row in cur:
		f.write(row["name"].upper()+'$'+row["full_address"].replace('\n',' ').upper() +'$'+row["city"].upper()+'$'+row["state"].upper()+'\n')
	
	f.close()
def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
	f = open(saveLocation2,'w')
	length = len(categoriesToSearch)
	for i in range(0,length):
		temp = collection.find({"categories": categoriesToSearch[i]})
		var = []
		#var.append("hello")
		
		for row in temp:
			if row["name"] not in var:
				var =[]
				lat1 = float(myLocation[0])
				lon1 = float(myLocation[1])
				lat2 = row["latitude"]
				lon2 = row["longitude"]
				R = 3959;
				rlat1 = math.radians(lat1);
				rlat2 = math.radians(lat2);
				dlat = math.radians(lat2-lat1);
				dlon = math.radians(lon2-lon1);
				

				a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(rlat1) * math.cos(rlat2) * math.sin(dlon/2) * math.sin(dlon/2);
				c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));

				d = R * c;
				if(d<=maxDistance):
					f.write(row["name"]+"\n")