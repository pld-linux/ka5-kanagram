%define		kdeappsver	21.04.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kanagram
Summary:	kanagram
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ea26678d98f1f4b6ffd274f9446a0ace
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Widgets-devel >= 5.11.1
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkeduvocdocument-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdeclarative-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-sonnet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5MultimediaQuick
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kanagram is a game based on anagrams of words: the puzzle is solved
when the letters of the scrambled word are put back in the correct
order. There is no limit on either time taken, or the amount of
attempts to solve the word.

Features

• Several word lists included • Hints and cheat help system • Word
list editor • Word lists distribution via KNewStuff • Scalable user
interface appropriate for children

%description -l pl.UTF-8
Kanagram jest grą bazującą na anagramach słów; zagadka jest rozwiązana
gdy litery szukanego słowa są ustawione z powrotem w poprawnej kolejności.
Nie ma ograniczeń na wykorzystany czas ani na liczbę prób.

Właściwości

• Wiele list słów wbudowanych
• System podpowiedzi
• Edytor listy słów
• Dystrybucja listy słów przez KNewStuff
• Skalowalny interfejs użytkownika odpowiedni dla dzieci

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
