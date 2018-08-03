#platform=x86, AMD64, or Intel EM64T
#version=DEVEL
# Keyboard layouts
keyboard 'us'
# Root password is redhat
rootpw --iscrypted $1$UIw76XGR$Y0zGLekqa9PR60TZV1O1l/
# System language
lang en_US
# System timezone
timezone America/New_York --isUtc
# Use graphical install
graphical
# Network information
network  --bootproto=dhcp --device=eth0
# System authorization information
auth  --useshadow  --passalgo=sha512
# Firewall configuration
firewall --disabled
# Use CDROM installation media
cdrom
firstboot --disable
# SELinux configuration
selinux --disabled

# System bootloader configuration
bootloader --location=mbr
# Partition clearing information
clearpart --all
# Disk partitioning information
part /boot --fstype="ext4" --size=500
part /tmp --fstype="ext4" --size=1000
part / --fstype="ext4" --size=8000
part swap --fstype="swap" --size=1024

%packages
@^gnome-desktop-environment
@base
@core
@desktop-debugging
@dial-up
@directory-client
@fonts
@gnome-desktop
@guest-agents
@guest-desktop-agents
@input-methods
@internet-browser
@java-platform
@multimedia
@network-file-system-client
@networkmanager-submodules
@print-client
@x11
chrony
kexec-tools

%end

%post
useradd test -c "Test"
echo redhat | passwd --stdin test
%end
