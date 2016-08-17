#!/usr/bin/python
# -*- coding: utf-8 -*-

import ptcaccount2
import csv


import csv


import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile=",])
   except getopt.GetoptError:
      print 'make_from_csv.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile


with open(inputfile, 'r') as f:
    d_reader = csv.DictReader(f)

    #get fieldnames from DictReader object and store in list
    headers = d_reader.fieldnames

    for line in d_reader:
        #print value in MyCol1 for each row
		ptcaccount2.random_account(username=line['username'], password="goatfuck", email=line['emailfirst'] + '@' + line['emailsecond'])
       