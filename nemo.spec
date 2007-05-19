Summary:	NEMO implementation based on the MIPL 2 architecture
Name:		nemo
Version:	0.2
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.mobile-ipv6.org/software/download/nemo-0.2.tar.gz
# Source0-md5:	33458738ee95ed351099d260f59bbea9
URL:		http://www.mobile-ipv6.org/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NEPL NEMO Platform for Linux is a NEMO implementation based on the MIPL 2 architecture. Version 0.2 is the second public release of NEPL. It aims to be fully RFC 3963 compliant supporting both implicit and explicit mode signalling.

%prep
%setup -q

%build
%configure \
	--enable-vt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS INSTALL* NEWS README* THANKS
