#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2017 Øystein Bedin <oybed@hotmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

''' generate_csr ansible module '''

from ansible.module_utils.basic import * # noqa: F403
from OpenSSL import crypto, SSL

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
---
module: generate_csr
short_description: Generate Certificate Signing Request (CSR)
author: "Øystein Bedin (@oybed)"
requirements: []
options:
  country:
    description:
    - Country Name for the Certificate Signing Request
    required: true
  state:
    description:
    - State or Province Name (full name) for the Certificate Signing Request
    required: true
  location:
    description:
    - Locality Name (eg, city) for the Certificate Signing Request
    required: true
  org_name:
    description:
    - Organization Name (eg, company) the Certificate Signing Request
    required: true
  org_unit:
    description:
    - Organization Unit Name (eg, section) the Certificate Signing Request
    required: true
  common_name:
    description:
    - Common Name (eg, your name or your server's hostname) for the Certificate Signing Request
    required: true
  email:
    description:
    - Email Address for the Certificate Signing Request
    required: true
  subject_alt_names:
    description:
    - List of Subject Alternative Name(s) for the Certificate Signing Request
    required: false
"""

EXAMPLES = """
- generate_csr:
    country: US
    state: CO
    location: Denver
    org_name: My Company
    org_unit: My Org
    common_name: myserver.example.com
    email: myemail@example.com
    subject_alt_names:
    - www.example.com
"""


def generateCSR(cn, c, st, l, o, ou, email, sans):
    # TODO: support different kind/size keys???
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    csr = crypto.X509Req()
    csr.get_subject().CN = cn
    csr.get_subject().countryName = c
    csr.get_subject().stateOrProvinceName = st
    csr.get_subject().localityName = l
    csr.get_subject().organizationName = o
    csr.get_subject().organizationalUnitName = ou
    csr.get_subject().emailAddress = email
    # csr.get_subject().subjectAltName = 'test.example.com'

    x509_extensions = ([])

    # TODO: support "IP:" in addition to "DNS:" below
    sans_list = []
    for san in sans:
        sans_list.append("DNS: {0}".format(san))

    sans_list = ", ".join(sans_list).encode()

    if sans_list:
        x509_extensions.append(crypto.X509Extension("subjectAltName".encode(), False, sans_list))

    csr.add_extensions(x509_extensions)

    csr.set_pubkey(key)
    csr.sign(key, "sha256")

    csr_out = crypto.dump_certificate_request(crypto.FILETYPE_PEM, csr)
    key_out = crypto.dump_privatekey(crypto.FILETYPE_PEM, key)

    return key_out,csr_out


def main():
    '''
    Generates a key and a CSR
    '''

    module = AnsibleModule(
        argument_spec = dict(
            country           = dict(required=True),
            state             = dict(required=True),
            location          = dict(required=True),
            org_name          = dict(required=True),
            org_unit          = dict(required=True),
            common_name       = dict(required=True),
            email             = dict(required=True),
            subject_alt_names = dict(required=False, type='list')
        )
    )

    sans = []
    if module.params['subject_alt_names']:
        sans = module.params['subject_alt_names']

    key, csr = generateCSR(module.params['common_name'],
                           module.params['country'],
                           module.params['state'],
                           module.params['location'],
                           module.params['org_name'],
                           module.params['org_unit'],
                           module.params['email'],
                           sans)

    module.exit_json(changed=True, key=key, csr=csr)


if __name__ == '__main__':
    main()
