#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kanagram
Summary:	kanagram
Name:		ka5-%{kaname}
Version:	22.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	cb56921d41937dd8924b61fc11c9b913
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
gdy litery szukanego słowa są ustawione z powrotem w poprawnej
kolejności. Nie ma ograniczeń na wykorzystany czas ani na liczbę prób.

Właściwości

• Wiele list słów wbudowanych • System podpowiedzi • Edytor listy słów
• Dystrybucja listy słów przez KNewStuff • Skalowalny interfejs
użytkownika odpowiedni dla dzieci

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
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
%{_datadir}/knsrcfiles/kanagram.knsrc
