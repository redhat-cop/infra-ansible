---

libvirt_name: "vm-3"
libvirt_title: "VM 3"
libvirt_description: "VM used for: Testing"
libvirt_memory: "2048"
libvirt_vcpus: "1"
libvirt_os_variant: "f28"
libvirt_iso: "/tmp/Fedora-Server-dvd-x86_64-28-1.1.iso"
libvirt_ksfile: "{{ inventory_dir }}/../files/vm-3.ks"
libvirt_http_host: '192.168.1.11'

libvirt_networks:
  - name: "vm-eth0"
    type: "bridge"
    hostif: "virbr0"
  - name: "vm-eth1"
    hostif: "eth0"
    

libvirt_disks:
  - name: "disk1"
    size: "20"
  - name: "disk2"
    size: "60"

eth0_ip: 192.168.1.23
eth0_mask: 255.255.255.0
eth0_gw: 192.168.1.1
