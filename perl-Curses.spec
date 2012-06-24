#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.perl
%define	pdir	Curses
%define	pnam	Curses
Summary:	Curses - terminal screen handling and optimization
#Summary(pl):	
Name:		perl-Curses
Version:	1.06
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		%{name}-sv_isa.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	ncurses-devel	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Curses" is the interface between Perl and your system's curses(3)
library.

# %description -l pl
# TODO

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Curses
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
