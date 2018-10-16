---
libvirt_name: "vm-3"
libvirt_title: "VM 3"
libvirt_description: "VM used for: Testing"
libvirt_memory: "2048"
libvirt_vcpus: "1"
libvirt_disk_size: "20"
libvirt_os_variant: "f28"
libvirt_iso: "/tmp/Fedora-Server-dvd-x86_64-28-1.1.iso"
libvirt_ksfile: "{{ inventory_dir }}/../files/vm-3.ks"
libvirt_network_hostif: "virbr0"
libvirt_http_host: '192.168.1.11'
libvirt_network_type: "bridge"

eth0_ip: 192.168.1.23
eth0_mask: 255.255.255.0
eth0_gw: 192.168.1.1
