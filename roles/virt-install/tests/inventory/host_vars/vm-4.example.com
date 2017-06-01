---

libvirt_name: "vm-4"
libvirt_title: "VM 4"
libvirt_description: "VM used for: XYZ"
libvirt_memory: "4096"
libvirt_vcpus: "4"
libvirt_disk_size: "15"
libvirt_os_variant: "f25"
libvirt_iso: "/tmp/Fedora-Server-dvd-x86_64-25-1.3.iso"
libvirt_ksfile: "{{ inventory_dir }}/../files/vm-4.ks"
libvirt_network_hostif: "eth0"
libvirt_http_host: '192.168.1.12'

eth0_ip: 192.168.1.24
eth0_mask: 255.255.255.0
eth0_gw: 192.168.1.1
