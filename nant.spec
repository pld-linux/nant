%define _snap rc2
Summary:	A .NET based build tool 
Summary(pl):	Narzêdzie do budowania pod .NET
Name:		nant
Version:	0.85
Release:	0.%{_snap}.1
License:	GPL v2+
Group:		Development/Building
Source0:	http://dl.sourceforge.net/nant/nant-%{version}-%{_snap}-src.tar.gz
# Source0-md5:	b1df647ea1f1fcf6c6f176a73ec2b760
Patch0:		%{name}-xml_syntax.patch
Patch1:		%{name}-PlatformID.patch
URL:		http://nant.sourceforge.net/
BuildRequires:	mono-csharp >= 1.1.4
Requires:	mono-devel >= 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NAnt is a .NET based build tool. In theory it is kind of like make
without make's wrinkles. In practice it's a lot like Ant.


%description -l pl
NAnt jest narzêdziem wspomagaj±cym budowanie oprogramowania w ¶rodowisku
.NET.  Teoretycznie jest to lepsze ,,make''. W praktyce dzia³a jak Ant.

%prep
%setup -q -n %{name}-%{version}-%{_snap}
%patch0 -p1
%patch1 -p1

%build
%{__make}
		
%install
rm -rf $RPM_BUILD_ROOT

bootstrap/NAnt.exe -f:NAnt.build install-linux -D:install.prefix=$RPM_BUILD_ROOT%{_prefix}

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/nant
echo 'exec mono %{_datadir}/NAnt/bin/NAnt.exe "$@"' >> $RPM_BUILD_ROOT%{_bindir}/nant

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/NAnt
