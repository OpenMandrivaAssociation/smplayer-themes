Summary:	Themes for SMPlayer
Name:		smplayer-themes
Version:	0.1.9
Release:	%mkrel 1
License:	GPL
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://smplayer.sourceforge.net/linux/download/%{name}-%{version}.tar.bz2
Requires:	smplayer	>= 0.4.24
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A set of themes for SMPlayer.

%prep
%setup -q
%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std DESTDIR=%{buildroot} PREFIX=%{_prefix}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/*
