#!/usr/bin/env python
import json
import sys

json_path = sys.argv[1]
raw_json = open(json_path, "rb").read()
data = json.loads(raw_json)

order = []
dependency_graph = {}

for i in data:
	ancestors = []
	for j in i["ancestors"]:
		ancestors.append(j["id"])
	dependency_graph[i["id"]] = ancestors

while dependency_graph:
	for k in dependency_graph.keys():
		if dependency_graph[k] == []:
			order.append(k)
			dependency_graph.pop(k, None)
	for k in dependency_graph.keys():
		dependency_graph[k] = [v for v in dependency_graph[k] if v not in order]

processed_data = []
for i in order:
	processed_data += [x for x in data if x["id"] == i]

print json.dumps(processed_data)
