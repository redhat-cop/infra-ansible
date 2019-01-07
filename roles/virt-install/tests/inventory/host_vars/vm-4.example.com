---

libvirt_name: "vm-4"
libvirt_title: "VM 4"
libvirt_description: "VM used for: Testing"
libvirt_memory: "2048"
libvirt_vcpus: "1"
libvirt_os_variant: "f28"
libvirt_iso: "/tmp/Fedora-Server-dvd-x86_64-28-1.1.iso"
libvirt_ksfile: "{{ inventory_dir }}/../files/vm-4.ks"
libvirt_http_host: '192.168.1.12'

libvirt_networks:
  - type: "bridge"
    hostif: "virbr0"

libvirt_disks:
  - size: "20"

eth0_ip: 192.168.1.24
eth0_mask: 255.255.255.0
eth0_gw: 192.168.1.1
