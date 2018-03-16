#!/usr/bin/env python
# Copyright 2018 Red Hat, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
