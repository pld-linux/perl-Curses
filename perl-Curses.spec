%include	/usr/lib/rpm/macros.perl
Summary:	C-Scan perl module
Summary(pl):	Modu� perla C-Scan
Name:		perl-Curses
Version:	1.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/C/Curses-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Curses modules

%description -l pl
Modu� perla Curses.

%prep
%setup -q -n Curses-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/*.pm
%dir %{perl_sitearch}/auto/Curses
%{perl_sitearch}/auto/Curses/Curses.bs
%attr(755,root,root) %{perl_sitearch}/auto/Curses/Curses.so
%{_mandir}/man3/*
