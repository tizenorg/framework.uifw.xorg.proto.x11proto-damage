
Name:       xorg-x11-proto-damageproto
Summary:    X.Org X11 Protocol damageproto
Version:    1.2.1
Release:    1.5
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/damageproto-%{version}.tar.gz
Provides:   damageproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n damageproto-%{version}


%build

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 







%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/damageproto.h
%{_includedir}/X11/extensions/damagewire.h
%{_datadir}/pkgconfig/damageproto.pc
%doc %{_datadir}/doc/damageproto


