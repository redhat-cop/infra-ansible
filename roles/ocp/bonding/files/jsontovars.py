#!/usr/bin/env python3

import os
import sys
import json
import argparse
import itertools

parser = argparse.ArgumentParser(
        description="Convert JSON to environment variables.")
parser.add_argument(
        'file',
        nargs='+'
        )
parser.add_argument(
        "--export",
        action='store_true',
        help="Print environment variables ready to be sourced.")
parser.add_argument(
        "--type",
        dest='ntype',
        help="Sets the node type so we can pull the correct config from json objects.")
parser.add_argument(
        "--ansible",
        action='store_true',
        help="Print environment variables in YAML format.")

args = parser.parse_args()

def flatten_json(y):
  out = {}
  def flatten(element, name =''):
    if type(element) is dict:
      for elem in element:
        flatten(element[elem], name + elem + '_')
    elif type(element) is list:
      for num, elem in enumerate(element):
        flatten(elem, name + str(num) + '_')
    else:
      out[name.upper().replace("-", "_")[:-1]] = element

  flatten(y)
  return out

def find_duplicates(fdict):
  keys = list(fdict.keys())
  for i, j in itertools.combinations(keys, 2):
    for key in fdict[i].keys():
      if key in fdict[j].keys():
        print("The variable {}='{}' in file {} was defined previously as {}='{}' in file {}.".format(key, fdict[j][key], j, key, fdict[i][key], i  ))
        sys.exit(1)

def main():
  jsonList = {}
  if args.file:
    for f in args.file:
      with open(f) as j:
        jsonList.update({ j.name: flatten_json(json.load(j)[args.ntype]) })

  find_duplicates(jsonList)

  for jdict in jsonList:
    for k, v in jsonList[jdict].items():
      if args.export:
        print("export {}='{}'".format(k, v))
      elif args.ansible:
        print("{}: {}".format(k, v))
      else:
        print("{}='{}'".format(k, v))


if __name__ == "__main__":
  main()
