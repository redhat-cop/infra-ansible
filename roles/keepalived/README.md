# keepalived

This roles generates a `keepalived.conf` file and copies it to the target HAproxy servers. 

## Example
The following is an example of an inventory definition and the resulting keepalived.conf file

### Inventory

```
lb_host_vip: 10.9.55.80

keepalived_nic: eth0
keepalived_priority: 101
keepalived_peer: 10.9.55.82

```


### keepalived.conf file

```
vrrp_script chk_haproxy {         
        script "killall -0 haproxy"
        interval 2                
        weight 2                 
}

vrrp_instance VI_1 {
        interface eth0
        state MASTER
        virtual_router_id 51
        priority 101
        unicast_peer {
            10.9.55.82
        }
        virtual_ipaddress {
            10.9.55.80
        }
        track_script {
            chk_haproxy
        }
}

```
