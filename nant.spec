%define _snap 2004.09.10
Summary:	A .NET based build tool 
Summary(pl):	Narzêdzie do budowania pod .NET
Name:		nant
Version:	0.85
Release:	0.%{_snap}.1
License:	GPL v2+
Group:		Development/Building
Source0:	http://nant.sourceforge.net/builds/%(echo %{_snap} | tr . -)-%{version}/%{name}-src.zip
# Source0-md5:	f15f7c93275abeb9a377f3ab0432336c
URL:		http://nant.sourceforge.net/
BuildRequires:	mono-csharp >= 1.0.1
BuildRequires:	p7zip
Requires:	mono-devel >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NAnt is a .NET based build tool. In theory it is kind of like make
without make's wrinkles. In practice it's a lot like Ant.


%description -l pl
NAnt jest narzêdziem wspomagaj±cym budowanie oprogramowania w ¶rodowisku
.NET.  Teoretycznie jest to lepsze ,,make''. W praktyce dzia³a jak Ant.

%prep
# unzip cannot handle the \ characters used there to sepearate paths
%setup -T -c
7z x %{SOURCE0} >/dev/null
mv %{name}-%{version}-nightly/* .

%build
%{__make}
		
%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/nant
echo 'exec mono %{_datadir}/NAnt/bin/NAnt.exe "$@"' >> $RPM_BUILD_ROOT%{_bindir}/nant

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/NAnt
