#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	MooseX
%define		pnam	Role-Parameterized
Summary:	MooseX::Role::Parameterized::Meta::Trait::Parameterized - trait for parameterized roles
Name:		perl-MooseX-Role-Parameterized
Version:	0.27
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff42187afa323a8fe7cba57ff78685de
URL:		http://search.cpan.org/dist/MooseX-Role-Parameterized/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Moose >= 0.78
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the trait for parameterized roles; that is, parameterizable
roles with their parameters bound. All this actually provides is a
place to store the MooseX::Role::Parameterized::Parameters object as
well as the MooseX::Role::Parameterized::Meta::Role::Parameterizable
object that generated this role object.

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
%doc Changes
%dir %{perl_vendorlib}/MooseX/Role
%{perl_vendorlib}/MooseX/Role/Parameterized.pm
%{perl_vendorlib}/MooseX/Role/Parameterized
%{_mandir}/man3/*
