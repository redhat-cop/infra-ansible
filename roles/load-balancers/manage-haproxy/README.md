# manage-haproxy

This role has 3 features:

 1) installs HAproxy and configures the host to run it ( *install.yml* )
 2) generates a `haproxy.cfg` file ( *generate-config.yml* )
 3) activates the haproxy.cfg file on the host ( *activate-config.yml* )

## Example

The following is an example of an inventory definition and the resulting haproxy.cfg file

### Inventory

```
lb_config:
  stats_page:
    enabled: True
    host_vip: '192.168.1.10'
    host_port: 8080
    username: admin
    password: admin
  frontends:
  - lb_name: my-web-server
    lb_host_vip: '192.168.1.10'
    lb_host_port: 80
  - lb_name: my-secure-web-server
    lb_host_vip: '192.168.1.10'
    lb_host_port: 443
    lb_ssl_enabled: True [optional for port 443]
  - lb_name: my-secure-web-server-8443
    lb_host_vip: '192.168.1.10'
    lb_host_port: 8443
    lb_ssl_enabled: True
  lb_entries:
  - lb_match_fqdn: master.env1.example.com
    lb_match_port: 8443
    lb_ssl_enabled: True
    backends:
    - host: master.env1.example.com
      port: 8443
  - lb_match_fqdn: .apps.env1.example.com
    lb_match_port: 443
    backends:
    - host: router1.env1.example.com
      port: 443
    - host: router2.env1.example.com
      port: 443
  - lb_match_fqdn: apps.env1.example.com
    lb_match_port: 80
    backends:
    - host: router1.env1.example.com
      port: 80
    - host: router2.env1.example.com
      port: 80
```


### haproxy.cfg file

```
#---------------------------------------------------------------------
# Global settings
#---------------------------------------------------------------------
global
    log         127.0.0.1 local2

    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4000
    user        haproxy
    group       haproxy
    daemon

    # turn on stats unix socket
    stats socket /var/lib/haproxy/stats

    # utilize system-wide crypto-policies
    ssl-default-bind-ciphers PROFILE=SYSTEM
    ssl-default-server-ciphers PROFILE=SYSTEM

#---------------------------------------------------------------------
# common defaults that all the 'listen' and 'backend' sections will
# use if not designated in their block
#---------------------------------------------------------------------
defaults
    mode                    http
    log                     global
    # option                  httplog
    option                  dontlognull
    option http-server-close
    option forwardfor       except 127.0.0.0/8
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 3000



frontend my-secure-web-server-8443
    bind 192.168.1.10:8443
    mode tcp

    tcp-request inspect-delay 5s
    tcp-request content accept if { req_ssl_hello_type 1 }

    acl master1.env1.example.com req_ssl_sni -m end master1.env1.example.com

    use_backend https_8443-master1.env1.example.com if master1.env1.example.com



frontend my-secure-web-server
    bind 192.168.1.10:443
    mode tcp

    tcp-request inspect-delay 5s
    tcp-request content accept if { req_ssl_hello_type 1 }

    acl router.env1.example.com req_ssl_sni -m end .apps.env1.example.com

    use_backend https_443-router.env1.example.com if router.env1.example.com

backend https_443-router.env1.example.com
    mode tcp
    balance roundrobin

    server router1.env1.example.com router1.env1.example.com:443 check
    server router2.env1.example.com router2.env1.example.com:443 check


backend https_8443-master1.env1.example.com
    mode tcp
    balance roundrobin

    server master1.env1.example.com master1.env1.example.com:8443 check

frontend my-web-server
    bind 192.168.1.10:80

    acl router.env1.example.com hdr_sub(host) -i apps.env1.example.com

    use_backend http_80-router.env1.example.com if router.env1.example.com

    default_backend lb_http_default

backend http_80-router.env1.example.com
    balance roundrobin
    option httpclose
    option forwardfor
    cookie JSESSIONID prefix

    server router1.env1.example.com router1.env1.example.com:80 cookie A check
    server router2.env1.example.com router2.env1.example.com:80 cookie A check

backend lb_http_default
    mode http
    stats enable
    stats uri /stats
    stats realm Haproxy\ Statistics
    stats auth admin:admin

```
