---

libvirt_name: "vm-2"
libvirt_title: "VM 2"
libvirt_description: "VM used for: XYZ"
libvirt_memory: "2048"
libvirt_vcpus: "2"
libvirt_disk_size: "5"
libvirt_os_variant: "f25"
libvirt_iso: "/tmp/Fedora-Server-dvd-x86_64-25-1.3.iso"
libvirt_ksfile: "{{ inventory_dir }}/../files/vm-2.ks"
libvirt_network_hostif: "eth0"
libvirt_http_host: '192.168.1.12'

eth0_ip: 192.168.1.22
eth0_mask: 255.255.255.0
eth0_gw: 192.168.1.1
