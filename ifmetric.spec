Summary:	Tool to change the priority of IPv4 routes
Name:		ifmetric
Version:	0.3
Release:	20
License:	GPLv2
Group: 		System/Configuration/Networking
Url: 		http://0pointer.de/lennart/projects/ifmetric/
Source0:	http://0pointer.de/lennart/projects/ifmetric/%{name}-%{version}.tar.bz2
BuildRequires:	lynx

%description
ifmetric is a Linux tool for setting the metrics of all IPv4 routes
attached to a given network interface at once. This may be used to
change the priority of routing IPv4 traffic over the interface.
Lower metrics correlate with higher priorities.

%prep
%setup -q

%build
%configure2_5x --disable-xmltoman
%make

%install
%makeinstall

%files
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.*

