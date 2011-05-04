Summary:	Tool to change the priority of IPv4 routes
Name:		ifmetric
Version:	0.3
Release:	%manbo_mkrel 9
License:	GPL
Group: 		System/Configuration/Networking
Url: 		http://0pointer.de/lennart/projects/ifmetric/
Source0:	http://0pointer.de/lennart/projects/ifmetric/%{name}-%{version}.tar.bz2
BuildRequires:	lynx
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man8/%{name}.*


