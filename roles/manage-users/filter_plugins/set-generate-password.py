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

def set_generate_password(entry):

    data = {
        'generate_password': False
    }

    if 'has_password' in entry.keys() and entry['has_password'] == False:
        data['generate_password'] = True

    return data


class FilterModule(object):
    ''' A set of filters to support diff'ing lists of dicts'''
    def filters(self):
        return {
            'set_generate_password': set_generate_password
        }
