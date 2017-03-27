# HAproxy

This role generates a `haproxy.cfg` file (the haproxy role can be used to copy it to the target HAproxy servers). 

## Example
The following is an example of an inventory definition and the resulting haproxy.cfg file

### Inventory

```
lb_https_entries:
- fqdn: master-0.d1.casl.rht-labs.com
  port: 8443
  backends: 
  - fqdn: master-0.d1.casl.rht-labs.com
    port: 8443
- fqdn: .apps.d1.casl.rht-labs.com
  name: router.d1.casl.rht-labs.com
  port: 443
  backends: 
  - fqdn: router-0.d1.casl.rht-labs.com
    port: 443
  - fqdn: router-1.d1.casl.rht-labs.com
    port: 443
- fqdn: master-0.s3.core.rht-labs.com
  port: 8443
  backends: 
  - fqdn: master-0.s3.core.rht-labs.com
    port: 8443
- fqdn: .apps.s3.core.rht-labs.com
  name: router.s3.core.rht-labs.com
  port: 443
  backends: 
  - fqdn: router.s3.core.rht-labs.com
    port: 443

lb_http_entries:
- fqdn: apps.d1.casl.rht-labs.com
  name: router.d1.casl.rht-labs.com
  port: 80
  backends: 
  - fqdn: router-0.d1.casl.rht-labs.com
    port: 80
  - fqdn: router-1.d1.casl.rht-labs.com
    port: 80
- fqdn: apps.s3.core.rht-labs.com
  name: router.s3.core.rht-labs.com
  port: 80
  backends: 
  - fqdn: router.s3.core.rht-labs.com
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



frontend ocp_masters
    bind 10.9.55.80:8443
    mode tcp

    tcp-request inspect-delay 5s
    tcp-request content accept if { req_ssl_hello_type 1 }

    acl master-0.d1.casl.rht-labs.com req_ssl_sni -m end master-0.d1.casl.rht-labs.com
    acl master-0.s3.core.rht-labs.com req_ssl_sni -m end master-0.s3.core.rht-labs.com

    use_backend https_8443-master-0.d1.casl.rht-labs.com if master-0.d1.casl.rht-labs.com
    use_backend https_8443-master-0.s3.core.rht-labs.com if master-0.s3.core.rht-labs.com



frontend ocp_routers_https
    bind 10.9.55.80:443
    mode tcp

    tcp-request inspect-delay 5s
    tcp-request content accept if { req_ssl_hello_type 1 }

    acl router.d1.casl.rht-labs.com req_ssl_sni -m end .apps.d1.casl.rht-labs.com
    acl router.s3.core.rht-labs.com req_ssl_sni -m end .apps.s3.core.rht-labs.com

    use_backend https_443-router.d1.casl.rht-labs.com if router.d1.casl.rht-labs.com
    use_backend https_443-router.s3.core.rht-labs.com if router.s3.core.rht-labs.com

backend https_443-router.d1.casl.rht-labs.com
    mode tcp
    balance roundrobin

    server router-0.d1.casl.rht-labs.com router-0.d1.casl.rht-labs.com:443 check
    server router-1.d1.casl.rht-labs.com router-1.d1.casl.rht-labs.com:443 check

backend https_443-router.s3.core.rht-labs.com
    mode tcp
    balance roundrobin

    server router.s3.core.rht-labs.com router.s3.core.rht-labs.com:443 check

backend https_8443-master-0.d1.casl.rht-labs.com
    mode tcp
    balance roundrobin

    server master-0.d1.casl.rht-labs.com master-0.d1.casl.rht-labs.com:8443 check

backend https_8443-master-0.s3.core.rht-labs.com
    mode tcp
    balance roundrobin

    server master-0.s3.core.rht-labs.com master-0.s3.core.rht-labs.com:8443 check


frontend ocp_routers_http
    bind 10.9.55.80:80

    acl router.d1.casl.rht-labs.com hdr_sub(host) -i apps.d1.casl.rht-labs.com
    acl router.s3.core.rht-labs.com hdr_sub(host) -i apps.s3.core.rht-labs.com

    use_backend http_80-router.d1.casl.rht-labs.com if router.d1.casl.rht-labs.com
    use_backend http_80-router.s3.core.rht-labs.com if router.s3.core.rht-labs.com

    default_backend lb_http_default

backend http_80-router.d1.casl.rht-labs.com
    balance roundrobin
    option httpclose
    option forwardfor
    cookie JSESSIONID prefix

    server router-0.d1.casl.rht-labs.com router-0.d1.casl.rht-labs.com:80 cookie A check
    server router-1.d1.casl.rht-labs.com router-1.d1.casl.rht-labs.com:80 cookie A check

backend http_80-router.s3.core.rht-labs.com
    balance roundrobin
    option httpclose
    option forwardfor
    cookie JSESSIONID prefix

    server router.s3.core.rht-labs.com router.s3.core.rht-labs.com:80 cookie A check

# Default backend - used for the 'stats' page
backend lb_http_default
    mode http
    stats enable
    stats uri /stats
    stats realm Haproxy\ Statistics
    stats auth admin:admin

```

