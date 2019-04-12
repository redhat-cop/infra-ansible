acme-host-cert
==============

This ansible role is used to create host certificates, using Let's Encrypt / ACME protocol

A certificate is created by submitting a request to Let's Encrypt with the FQDN for the requested certificate. Let's Encrypt will then return a challenge that is used to update the DNS servers with a TXT record for validation. Once this is done, the validation will be performed by a 2nd call to Let's Encrypt. Once validated, the certificates are returned and this role writes them to files for further consumption.

Requirements
------------

- If using DNS to validate the TXT record, need to have the `python2-dns` and/or `python3-dns` package installed (Fedora/RHEL)

Role Variables
--------------
| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|host_name| The hostname/FQDN of the host | yes | |
|csr| The CSR (Certificate Signing Request) info - see the (generate-csr)[../generate-csr/README.md] for more details | yes | |
|dns_data| The DNS configuration used to update the DNS server(s) with TXT records - see example below for more details. | yes | '' |
|target_cert_files| The certificate files to be written by this role - see example below for more details. | yes | |
|acme.account_key_content| See Ansible (acme_certificate_module documentation)[https://docs.ansible.com/ansible/latest/modules/acme_certificate_module.html#parameters]| no | N/A |
|acme.account_key_src| See Ansible (acme_certificate_module documentation)[https://docs.ansible.com/ansible/latest/modules/acme_certificate_module.html#parameters]| no | N/A |
|acme.account_email| See Ansible (acme_certificate_module documentation)[https://docs.ansible.com/ansible/latest/modules/acme_certificate_module.html#parameters]| no | N/A |
|acme.challenge| See Ansible (acme_certificate_module documentation)[https://docs.ansible.com/ansible/latest/modules/acme_certificate_module.html#parameters]| no | 'dns-01' |
|acme.directory| See Ansible (acme_certificate_module documentation)[https://docs.ansible.com/ansible/latest/modules/acme_certificate_module.html#parameters]| no | 'https://acme-v02.api.letsencrypt.org/directory' |
|acme.version| See Ansible (acme_certificate_module documentation)[https://docs.ansible.com/ansible/latest/modules/acme_certificate_module.html#parameters]| no | '2' |
|acme.terms_agreed| See Ansible (acme_certificate_module documentation)[https://docs.ansible.com/ansible/latest/modules/acme_certificate_module.html#parameters]| no | 'yes' |
|acme.remaining_days| See Ansible (acme_certificate_module documentation)[https://docs.ansible.com/ansible/latest/modules/acme_certificate_module.html#parameters]| no | N/A |
|acme.force| See Ansible (acme_certificate_module documentation)[https://docs.ansible.com/ansible/latest/modules/acme_certificate_module.html#parameters]| no | N/A |


Dependencies
------------
This role depends on a CSR being available for consumption. The CSR can be genreated with the (generate-csr)[../generate-csr] role, as shown by the example playbook and inventory below.

Example Playbooks
----------------

```
- hosts: cert-host
  roles:
  - certs/generate-csr
  - certs/acme-host-cert
```

Example Inventory
----------------

**inventory/hosts**
```
[cert-host]
localhost
```

**inventory/cert-host**
```
host_name: "*.h2.example.com"

csr:
  hostname: "{{ host_name }}"
  country: "US"
  state: "North Carolina"
  location: "Raleigh"
  org_name: "Red Hat, Inc."
  org_unit: "Open Innovation Labs"
  email: "myemail@example.com"


dns_data:
  views:
    - name: external
      zones:
        - dns_domain: example.com
          nsupdate:
            - server: 192.168.48.38
              key_name: "external-example.com"
              key_secret: "oQSq7yGN1/X+xjgrSoWJJ0xhHkhRHtXzumripORlm0+/LSENKFK7JMTuauWr0Dw77OxwOWCXTnVIP+MWQxSHDA=="
              key_algorithm: "hmac-sha256"
          entries: "{{ certificate_dns_entries }}" # The 'certificate_dns_entries' is populated by the role - is not required to be set before running this role

# The 'file_host_name' is here just to make file names for wildcard domain names be changed to "wildcard."
file_host_name: "{{ host_name | regex_replace('^\\*\\.', 'wildcard.') }}"

target_cert_files:
  key: "/tmp/{{ file_host_name }}/{{ file_host_name }}.key"
  csr: "/tmp/{{ file_host_name}}/{{ file_host_name }}.csr"
  host_cert: "/tmp/{{ file_host_name }}/{{ file_host_name }}.pem"
  intermediate_ca: "/tmp/{{ file_host_name }}/intermediate-ca.pem"
  fullchain: "/tmp/{{ file_host_name }}/{{ file_host_name }}-fullchain.pem"

# Fill in the 'acme' dictionary per the above docs - in the example below the 'account_key_content' is the unique
# identifier for the user running the role. See the Ansible docs for details on how to generate one.
acme:
  account_key_content: |
    -----BEGIN PRIVATE KEY-----
    MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDZAXwEdau/mRLT
     :
     :
    -----END PRIVATE KEY-----
```

License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
