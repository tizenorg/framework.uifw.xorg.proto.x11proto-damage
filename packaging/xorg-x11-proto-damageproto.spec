
Name:       xorg-x11-proto-damageproto
Summary:    X.Org X11 Protocol damageproto
Version:    1.2.1
Release:    1.5
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-damageproto.manifest 
Provides:   damageproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 







%files
%manifest xorg-x11-proto-damageproto.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/damageproto.h
%{_includedir}/X11/extensions/damagewire.h
%{_datadir}/pkgconfig/damageproto.pc
%doc %{_datadir}/doc/damageproto


