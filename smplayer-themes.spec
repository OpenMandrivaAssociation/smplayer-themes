Summary:	Themes for SMPlayer
Name:		smplayer-themes
Version:	20.11.0
Release:	1
License:	GPLv2+
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
Requires:	smplayer
Buildarch:	noarch
Obsoletes:	%{name}-0.1.20
# For rcc
BuildRequires:	cmake(Qt5Core)
%(for theme in Breeze Breeze-dark Dark Faenza-Darkest Faenza-Silver Faenza Gartoon Gnome Masalla Monochrome Noia Numix-remix Numix-uTouch Nuvola Oxygen Oxygen-Air Oxygen-KDE Oxygen-Refit Papirus PapirusDark Silk Tango blackPanther-Light blackPanther-Real blackPanther-VistaLike ePapirus; do
	echo "Requires: smplayer-theme-$theme = %{EVRD}"
done)

%description
A set of themes for SMPlayer.

%prep
%setup -q

%build
export PATH=%{_libdir}/qt5/bin:$PATH
%make

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_datadir}/smplayer/themes
cp -a themes/* %{buildroot}%{_datadir}/smplayer/themes

rm -f %{buildroot}%{_datadir}/smplayer/themes/Windows.install \
	%{buildroot}%{_datadir}/smplayer/themes/Makefile \

%(for theme in Breeze Breeze-dark Dark Faenza-Darkest Faenza-Silver Faenza Gartoon Gnome Masalla Monochrome Noia Numix-remix Numix-uTouch Nuvola Oxygen Oxygen-Air Oxygen-KDE Oxygen-Refit Papirus PapirusDark Silk Tango blackPanther-Light blackPanther-Real blackPanther-VistaLike ePapirus; do
	cat <<EOF
%package -n smplayer-theme-$theme
Summary: The $theme theme for smplayer
Requires: smplayer
Group: Video

%description -n smplayer-theme-$theme
The $theme theme for smplayer

%files -n smplayer-theme-$theme
%{_datadir}/smplayer/themes/$theme
%{_datadir}/smplayer/themes/$theme.qrc
EOF

done)

%files
