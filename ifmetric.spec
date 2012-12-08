Summary:	Tool to change the priority of IPv4 routes
Name:		ifmetric
Version:	0.3
Release:	%manbo_mkrel 11
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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-9mnb2
+ Revision: 665504
- mass rebuild

* Sat Jan 30 2010 Funda Wang <fwang@mandriva.org> 0.3-8mnb2
+ Revision: 498407
- rebuild

* Tue Aug 05 2008 Thierry Vignaud <tv@mandriva.org> 0.3-7mnb2
+ Revision: 263682
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3-6mnb1
+ Revision: 170651
- replace %%mkrel with %%manbo_mkrel for Manbo Core 1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 0.3-6mdv2008.1
+ Revision: 134095
- rebuild

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2008.1
+ Revision: 126997
- kill re-definition of %%buildroot on Pixel's request
- fix man pages


* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3-5mdv2007.0
+ Revision: 119961
- Import ifmetric

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.3-4mdk
- Rebuild

* Wed Aug 04 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.3-3mdk
- fix buildrequires

* Thu Jul 01 2004 Olivier Blin <blino@mandrake.org> 0.3-2mdk
- rpmbuildupdate awareness

* Thu Jul 01 2004 Olivier Blin <blino@mandrake.org> 0.3-1mdk
- first Mandrakelinux release

