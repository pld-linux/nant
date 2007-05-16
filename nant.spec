%include	/usr/lib/rpm/macros.mono
Summary:	A .NET based build tool
Summary(pl.UTF-8):	Narzędzie do budowania pod .NET
Name:		nant
Version:	0.85
Release:	1
License:	GPL v2+
Group:		Development/Building
Source0:	http://dl.sourceforge.net/nant/nant-%{version}-src.tar.gz
# Source0-md5:	45ae065439b6cbc0e02051b855843f50
Patch0:		%{name}-fix.patch
URL:		http://nant.sourceforge.net/
BuildRequires:	mono-compat-links >= 1.1.4
BuildRequires:	mono-csharp >= 1.1.4
BuildRequires:	pkgconfig
Requires:	mono-devel >= 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NAnt is a .NET based build tool. In theory it is kind of like make
without make's wrinkles. In practice it's a lot like Ant.

%description -l pl.UTF-8
NAnt jest narzędziem wspomagającym budowanie oprogramowania w
środowisku .NET. Teoretycznie jest to lepsze ,,make''. W praktyce
działa jak Ant.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

mono bootstrap/NAnt.exe -f:NAnt.build install-linux -D:install.prefix=$RPM_BUILD_ROOT%{_prefix}

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/nant
echo 'exec mono %{_datadir}/NAnt/bin/NAnt.exe "$@"' >> $RPM_BUILD_ROOT%{_bindir}/nant

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/NAnt
