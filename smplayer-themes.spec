Summary:	Themes for SMPlayer
Name:		smplayer-themes
Version:	18.6.0
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
Requires:	smplayer
Buildarch:	noarch
Obsoletes:	%{name}-0.1.20

%description
A set of themes for SMPlayer.

%prep
%setup -q

%build

%install
#%makeinstall_std DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_datadir}/smplayer/themes
cp -a themes/* %{buildroot}%{_datadir}/smplayer/themes

%files
%doc README.txt Changelog
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/*
