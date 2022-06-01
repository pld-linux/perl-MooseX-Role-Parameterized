#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	MooseX
%define		pnam	Role-Parameterized
Summary:	MooseX::Role::Parameterized - Moose roles with composition parameters
Summary(pl.UTF-8):	MooseX::Role::Parameterized - role Moose z parametrami składania
Name:		perl-MooseX-Role-Parameterized
Version:	1.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a326fd9fb065dafc75fc0211797968e8
URL:		https://metacpan.org/dist/MooseX-Role-Parameterized
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-Module-Build-Tiny >= 0.034
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-Check >= 0.011
BuildRequires:	perl-CPAN-Meta-Requirements
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Moose >= 2.0300
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-namespace-autoclean
BuildRequires:	perl-namespace-clean >= 0.19
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MooseX::Role::Parameterized - Moose roles with composition parameters.

%description -l pl.UTF-8
MooseX::Role::Parameterized - role Moose z parametrami składania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/MooseX/Role
%{perl_vendorlib}/MooseX/Role/Parameterised.pm
%{perl_vendorlib}/MooseX/Role/Parameterized.pm
%{perl_vendorlib}/MooseX/Role/Parameterized
%{_mandir}/man3/MooseX::Role::Parameterised.3pm*
%{_mandir}/man3/MooseX::Role::Parameterized*.3pm*
