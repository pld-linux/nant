#
# TODO: make backward compatibility for mono-1.0 and mono-1.1 or drop these frameworks
# note: mono 2.8 doesn't support .NET 1.0/1.1 any longer
#
Summary:	A .NET based build tool
Summary(pl.UTF-8):	Narzędzie do budowania pod .NET
Name:		nant
Version:	0.91
Release:	1
License:	GPL v2+
Group:		Development/Building
Source0:	http://downloads.sourceforge.net/nant/nant-%{version}-src.tar.gz
# Source0-md5:	571e72813bdb3f0e8362403025445a61
URL:		http://nant.sourceforge.net/
BuildRequires:	mono-compat-links >= 2.8
BuildRequires:	mono-csharp >= 2.8
BuildRequires:	pkgconfig
Requires:	mono-devel >= 2.8
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

cat <<'EOF' > %{name}.sh
#!/bin/sh
exec mono %{_datadir}/NAnt/bin/NAnt.exe "$@"
EOF

%build
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
mono bootstrap/NAnt.exe \
	-f:NAnt.build install-linux \
	-D:install.prefix=$RPM_BUILD_ROOT%{_prefix}

install %{name}.sh $RPM_BUILD_ROOT%{_bindir}/nant

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/NAnt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/nant
%{_datadir}/NAnt
%{_pkgconfigdir}/nant.pc
