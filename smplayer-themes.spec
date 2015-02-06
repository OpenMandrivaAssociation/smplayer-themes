Summary:	Themes for SMPlayer
Name:		smplayer-themes
Version:	20120919
Release:	3
Epoch:		1
License:	GPLv2+
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/smplayer/SMPlayer-themes/%{version}/%{name}-%{version}.tar.bz2
%if %mdkversion > 200800
Requires:	smplayer
%endif
Buildarch:	noarch
Obsoletes:	%{name}-0.1.20

%description
A set of themes for SMPlayer.

%prep
%setup -q

%build

%install
%makeinstall_std DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%doc README.txt Changelog
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/*


%changelog
* Sat Sep 22 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:20120919-1
+ Revision: 817334
- update to new version 20120919

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.20-2mdv2011.0
+ Revision: 614929
- the mass rebuild of 2010.1 packages

* Sun Jan 17 2010 Funda Wang <fwang@mandriva.org> 0.1.20-1mdv2010.1
+ Revision: 492771
- new version 0.1.20

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.1.19-2mdv2010.0
+ Revision: 445134
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.19-1mdv2009.1
+ Revision: 349358
- update to new version 0.1.19
- fix source url

* Thu Nov 13 2008 Funda Wang <fwang@mandriva.org> 0.1.18-1mdv2009.1
+ Revision: 302606
- New version 0.1.18

* Sat Sep 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.17-1mdv2009.1
+ Revision: 288898
- update to new version 0.1.17

* Fri Jun 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.16-1mdv2009.0
+ Revision: 227623
- update to new version 0.1.16

* Mon Feb 04 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.15-1mdv2008.1
+ Revision: 162024
- new version
- requires smplayer for mdv > 2008.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.14-1mdv2008.1
+ Revision: 105746
- new version

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.13-2mdv2008.1
+ Revision: 102383
- drop requires on smplayer, since whe have both qt3 and qt4 version

* Fri Oct 12 2007 Funda Wang <fwang@mandriva.org> 0.1.13-1mdv2008.1
+ Revision: 97374
- New version 0.1.13

* Sun Sep 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.12-1mdv2008.0
+ Revision: 93928
- new version (new Breathless theme)
- package Changelog

* Tue Sep 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.9-1mdv2008.0
+ Revision: 79557
- new version

* Mon Sep 03 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.8-1mdv2008.0
+ Revision: 78757
- new version

* Thu Jul 19 2007 Funda Wang <fwang@mandriva.org> 0.1.3-1mdv2008.0
+ Revision: 53634
- New version

* Mon Jun 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-1mdv2008.0
+ Revision: 44177
- new version

* Fri May 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 31197
- new version
- some minor tweaks in spec file

* Sun May 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1-2mdv2008.0
+ Revision: 28847
- own themes directory

* Sun May 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1-1mdv2008.0
+ Revision: 28834
- themes are standalone package now
- Import smplayer-themes

