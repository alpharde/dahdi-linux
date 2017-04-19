#Workaround for 64 bit CPUs
%define _lib lib

# The next time this is touched, merge it with dahdi-linux-kmod, because it's
# crazy to have two different ones.

Summary: The DAHDI project
Name: dahdi-linux
Version: 2.11.1
Release: 1%{dist}
License: GPL
Group: Utilities/System
Source0: https://downloads.asterisk.org/pub/telephony/dahdi-linux/dahdi-linux-2.11.1.tar.gz
Patch0: 0001-Add-version.h.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.asterisk.org/
Vendor: Digium, Inc.
Packager: Nethesis <info@nethesis.it>
Requires: kmod
Requires: dahdi-firmware
Requires: kmod-dahdi-linux
Requires: libwat
BuildRequires: vim
%description
The open source DAHDI project

%package devel
Summary: DAHDI libraries and header files for development
Group: Development/Libraries

%description devel
The static libraries and header files needed for building additional plugins/modules

%prep
%setup -n %{name}-%{version}
%patch0 -p1

%build
echo %{version} > .version

%install
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d/
make include/dahdi/version.h
make DESTDIR=$RPM_BUILD_ROOT install-include install-xpp-firm #install-devices

%post
ldconfig

%clean
cd $RPM_BUILD_DIR
%{__rm} -rf %{name}-%{version}
%{__rm} -rf /var/log/%{name}-sources-%{version}-%{release}.make.err
%{__rm} -rf $RPM_BUILD_ROOT

%files
%config %{_sysconfdir}/udev/rules.d/
%{_datarootdir}/dahdi/*

%files devel
%defattr(-, root, root)
%{_includedir}/dahdi/
