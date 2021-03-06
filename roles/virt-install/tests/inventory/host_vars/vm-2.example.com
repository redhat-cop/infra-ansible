---
libvirt_name: "vm-2"
libvirt_title: "VM 2"
libvirt_description: "VM used for: Testing"
libvirt_memory: "2048"
libvirt_vcpus: "1"
libvirt_os_variant: "f28"
libvirt_iso: "/tmp/Fedora-Server-dvd-x86_64-28-1.1.iso"
libvirt_ksfile: "{{ inventory_dir }}/../files/vm-2.ks"
libvirt_http_host: '192.168.1.12'

libvirt_networks:
  - name: "eth0"
    type: "bridge"
    hostif: "virbr0"
    ip: 192.168.1.22
    netmask: 255.255.255.0
    gateway: 192.168.1.1

libvirt_disks:
  - name: "disk1"
    size: "20"

