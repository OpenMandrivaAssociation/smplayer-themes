Summary:	Themes for SMplayer
Name:		smplayer-themes
Version:	0.1
Release:	%mkrel 2
License:	GPL
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://smplayer.sourceforge.net/linux/download/%{name}-%{version}.tar.bz2
Requires:	smplayer	>= 0.4.24
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A set of themes for SMplayer.

%prep
%setup -q
%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/smplayer/themes
cp -r themes/* %{buildroot}%{_datadir}/smplayer/themes

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/*