#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.perl
%define	pdir	Curses
%define	pnam	Curses
Summary:	Curses perl module
Summary(pl):	Modu³ perla Curses
Name:		perl-Curses
Version:	1.06
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl-devel >= 5.6
BuildRequires:	ncurses-devel	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Curses modules.

%description -l pl
Modu³ perla Curses.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_sitelib}/Curses

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/*.pm
%dir %{perl_sitearch}/auto/Curses
%dir %{perl_sitelib}/Curses
%{perl_sitearch}/auto/Curses/Curses.bs
%attr(755,root,root) %{perl_sitearch}/auto/Curses/Curses.so
%{_mandir}/man3/*
