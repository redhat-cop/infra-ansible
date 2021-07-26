# Keyboard layouts
keyboard 'us'

# Root password 
rootpw --plaintext redhat 

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
firewall --enabled

# Use CDROM installation media
cdrom
firstboot --disable

# SELinux configuration
selinux --enabled

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
net-tools
wget
%end

%post
useradd test -c "Test"
echo redhat | passwd --stdin test
%end
