from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

import csv
import json
import os

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        ret = []

        cwd = os.getcwd()

        for term in terms:

            params = term.split()

            paramvals = {
                'file' : 'users.csv',
                'var' : 'users'
            }

            # parameters specified?
            try:
                for param in params:
                    name, value = param.split('=')
                    assert(name in paramvals)
                    paramvals[name] = value
                    display.vvvv(u"Param: %s : %s" % (name, value))
            except (ValueError, AssertionError) as e:
                raise AnsibleError(e)

            if os.path.isabs(paramvals['file']):
              lookupfile = paramvals['file']
            else:
              lookupfile = cwd + '/' + paramvals['file']

            display.vvvv(u"File lookup using %s as file" % paramvals['file'])
            try:
                if lookupfile:
                    #read csv into rows
                    with open(lookupfile) as f:
                        reader = csv.DictReader(f)
                        rows = list(reader)

                    # do output for users or groups
                    if(paramvals['var'] == 'user_groups'):
                        ret.append(self.get_user_groups(rows))
                    else:
                        ret.append(self.get_users(rows))

                else:
                    raise AnsibleParserError()
            except AnsibleParserError:
                raise AnsibleError("could not locate file in lookup: %s" % paramvals['file'])

        return ret

    # get json for users - file should already support this format
    def get_users(self, rows):

        display.vvvv(u"Getting users")

        return json.dumps(rows)

    # get json for groups - need to maniuplate the rows a bit.
    # take username, group and transfrom to { name: mygroup, members: [ user_name: user1 }, { user_name: user2 } ]}
    def get_user_groups(self, rows):

        display.vvvv(u"Getting user groups")

        userGroupsDict = {}

        userGroupList = []

        for row in rows:
            if row['group'] not in userGroupsDict :
                userGroupsDict[row['group']] = []

            userGroupsDict[row['group']].append(row['user_name'])

        for key in userGroupsDict :
            userGroupList.append({ "name": key, "members": userGroupsDict[key]})

        return json.dumps(userGroupList)
