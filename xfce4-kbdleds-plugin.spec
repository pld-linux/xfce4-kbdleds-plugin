Summary:	Show the state of keyboard LEDs
Name:		xfce4-kbdleds-plugin
Version:	0.0.6
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-kbdleds-plugin/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	db6ad8e3502f3373f087ba2034141552
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-kbdleds-plugin
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	libxfce4ui-devel >= 4.10.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.10.0
BuildRequires:	xfce4-panel-devel >= 4.10.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin shows the state of your keyboard LEDs:
Caps, Scroll and Num Lock in Xfce panel. 

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-kbdleds-plugin
%{_datadir}/xfce4/panel-plugins/kbdleds.desktop
%{_iconsdir}/hicolor/*/apps/*
