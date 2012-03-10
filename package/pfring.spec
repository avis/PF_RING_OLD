Summary: PF_RING network probe
Name: pfring
Version: 5.3.1
Release: 0
License: GPL
Group: Networking/Utilities
URL: http://www.ntop.org/nProbe.html
Packager: Luca Deri <deri@ntop.org>
# Temporary location where the RPM will be built
BuildRoot:  %{_tmppath}/%{name}-%{version}-root
# 

%description
PF_RING kernel module and drivers for high-speed RX/TX package processing

%install
PATH=/usr/bin:/bin:/usr/sbin:/sbin
if [ -d $RPM_BUILD_ROOT ]; then
	\rm -rf $RPM_BUILD_ROOT
fi
mkdir -p $RPM_BUILD_ROOT/usr/local/PF_RING
mkdir -p $RPM_BUILD_ROOT/usr/local/PF_RING/kernel
mkdir -p $RPM_BUILD_ROOT/usr/local/include/linux
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/PF_RING/drivers/DNA
mkdir -p $RPM_BUILD_ROOT/usr/local/PF_RING/bin
# Kernel module
cp $HOME/PF_RING/kernel/pf_ring.ko $RPM_BUILD_ROOT/usr/local/PF_RING/kernel
cp $HOME/PF_RING/kernel/linux/pf_ring.h $RPM_BUILD_ROOT/usr/local/include/linux/
# Userland
cp $HOME/PF_RING/userland/lib/libpfring.a   $RPM_BUILD_ROOT/usr/local/lib
cp $HOME/PF_RING/userland/lib/libpfring.so  $RPM_BUILD_ROOT/usr/local/lib
cp $HOME/PF_RING/userland/lib/pfring.h      $RPM_BUILD_ROOT/usr/local/include
cp $HOME/PF_RING/userland/libpcap/libpcap.a $RPM_BUILD_ROOT/usr/local/lib
cp $HOME/PF_RING/userland/examples/pfcount  $RPM_BUILD_ROOT/usr/local/PF_RING/bin
cp $HOME/PF_RING/userland/examples/pfsend   $RPM_BUILD_ROOT/usr/local/PF_RING/bin
cp $HOME/PF_RING/userland/examples/pfdnabounce $RPM_BUILD_ROOT/usr/local/PF_RING/bin
cp $HOME/PF_RING/README.FIRST                  $RPM_BUILD_ROOT/usr/local/PF_RING/
# DNA Drivers
cp $HOME/PF_RING/drivers/DNA/ixgbe-3.7.17-DNA/src/ixgbe.ko $RPM_BUILD_ROOT/usr/local/PF_RING/drivers/DNA
cp $HOME/PF_RING/drivers/DNA/igb-3.2.10-DNA/src/igb.ko $RPM_BUILD_ROOT/usr/local/PF_RING/drivers/DNA
cp $HOME/PF_RING/drivers/DNA/e1000e-1.6.3-DNA/src/e1000e.ko $RPM_BUILD_ROOT/usr/local/PF_RING/drivers/DNA
cp $HOME/PF_RING/drivers/DNA/README.DNA $RPM_BUILD_ROOT/usr/local/PF_RING/drivers/DNA


# Clean out our build directory
%clean
rm -fr $RPM_BUILD_ROOT

%files
/usr/local/PF_RING/kernel/pf_ring.ko
/usr/local/include/linux/pf_ring.h
/usr/local/lib/libpfring.a
/usr/local/lib/libpfring.so
/usr/local/lib/libpcap.a
/usr/local/include/pfring.h
/usr/local/PF_RING/drivers/DNA/README.DNA
/usr/local/PF_RING/drivers/DNA/ixgbe.ko
/usr/local/PF_RING/drivers/DNA/igb.ko
/usr/local/PF_RING/drivers/DNA/e1000e.ko
/usr/local/PF_RING/bin/pfcount
/usr/local/PF_RING/bin/pfsend
/usr/local/PF_RING/bin/pfdnabounce
/usr/local/PF_RING/README.FIRST

# Set the default attributes of all of the files specified to have an
# owner and group of root and to inherit the permissions of the file
# itself.
%defattr(-, root, root)

%changelog
* Sat Mar 10 2012 Luca Deri <deri@ntop.org>
- Original upstream version


