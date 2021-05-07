#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%define		pdir	Curses
%define		pnam	Curses
Summary:	Curses - terminal screen handling and optimization
Summary(pl.UTF-8):	Curses - obsługa i optymalizacja ekranu terminala
Name:		perl-Curses
Version:	1.36
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/G/GI/GIRAFFED/%{pnam}-%{version}.tar.gz
# Source0-md5:	389c70ee5530b887f8e5dc1303cb5294
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
%{_mandir}/man3/*
