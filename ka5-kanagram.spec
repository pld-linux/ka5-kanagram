%define		kdeappsver	18.04.0
%define		qtver		5.3.2
%define		kaname		kanagram
Summary:	kanagram
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	91de0134bbbbc96992c332ba12214e76
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ka5-libkeduvocdocument-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kanagram.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kanagram.knsrc
%attr(755,root,root) %{_bindir}/kanagram
%{_desktopdir}/org.kde.kanagram.desktop
%{_datadir}/config.kcfg/kanagram.kcfg
%{_iconsdir}/hicolor/128x128/apps/kanagram.png
%{_iconsdir}/hicolor/16x16/apps/kanagram.png
%{_iconsdir}/hicolor/24x24/apps/kanagram.png
%{_iconsdir}/hicolor/32x32/apps/kanagram.png
%{_iconsdir}/hicolor/48x48/apps/kanagram.png
%{_iconsdir}/hicolor/64x64/apps/kanagram.png
%{_iconsdir}/hicolor/80x80/apps/kanagram-harmattan.png
%{_iconsdir}/hicolor/scalable/apps/kanagram.svgz
%{_datadir}/kanagram
%{_datadir}/metainfo/org.kde.kanagram.appdata.xml
