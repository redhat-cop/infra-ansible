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

def get_remaining_items(list_a, list_b, key_a, key_b):
    for b in list_b:
        if len(list_a) == 0:
            break
        for a in list_a[:]:
            if a[key_a] == b[key_b]:
                list_a.remove(a)

    return list_a

class FilterModule(object):
    ''' A set of filters to support diff'ing lists of dicts'''
    def filters(self):
        return {
            'get_remaining_items': get_remaining_items
        }
