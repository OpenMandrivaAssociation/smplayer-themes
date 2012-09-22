Summary:	Themes for SMPlayer
Name:		smplayer-themes
Version:	20120919
Release:	1
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
