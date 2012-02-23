Summary:	Tool to change the priority of IPv4 routes
Name:		ifmetric
Version:	0.3
Release:	10
License:	GPL
Group:		System/Configuration/Networking
Url:		http://0pointer.de/lennart/projects/ifmetric/
Source0:	http://0pointer.de/lennart/projects/ifmetric/%{name}-%{version}.tar.bz2
Patch0:		ifmetric-0.3-netlink-fix.patch
BuildRequires:	lynx

%description
ifmetric is a Linux tool for setting the metrics of all IPv4 routes
attached to a given network interface at once. This may be used to
change the priority of routing IPv4 traffic over the interface.
Lower metrics correlate with higher priorities.

%prep
%setup -q
%patch0 -p1 -b .netlink~

%build
%configure2_5x --disable-xmltoman
%make

%install
%makeinstall

%files
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.*
