#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Curses
%define		pnam	Curses
Summary:	Curses - terminal screen handling and optimization
Summary(pl.UTF-8):	Curses - obsługa i optymalizacja ekranu terminala
Name:		perl-Curses
Version:	1.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tgz
# Source0-md5:	b8c1b4e9f810e8188825eba868a6843e
URL:		http://search.cpan.org/dist/Curses/
BuildRequires:	ncurses-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Curses" is the interface between Perl and your system's curses(3)
library.

%description -l pl.UTF-8
Curses to interfejs między Perlem a systemową biblioteką curses(3).

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Curses

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Curses/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/*.pm
%dir %{perl_vendorlib}/Curses
%dir %{perl_vendorarch}/auto/Curses
%attr(755,root,root) %{perl_vendorarch}/auto/Curses/Curses.so
%{perl_vendorarch}/auto/Curses/Curses.bs
%{_mandir}/man3/*
