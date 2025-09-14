#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	File
Summary:	Test::File - test file attributes
Summary(pl.UTF-8):	Test::File - testowanie atrybutów plików
Name:		perl-Test-File
Version:	1.995
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	865b7e00fa68431596e1933d523506ab
Patch0:		%{name}-foreign-tests.patch
URL:		https://metacpan.org/dist/Test-File
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.64
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Test::Builder) >= 1.001006
BuildRequires:	perl-Test-Builder-Tester >= 1.04
BuildRequires:	perl-Test-Simple >= 1
BuildRequires:	perl-version >= 0.86
%endif
Requires:	perl(Test::Builder) >= 1.001006
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules provides a collection of test utilities for file
attributes.

%description -l pl.UTF-8
Ten moduł udostępnia zestaw narzędzi testowych dla atrybutów plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes SECURITY.md
%{perl_vendorlib}/Test/File.pm
%{_mandir}/man3/Test::File.3pm*
%{_examplesdir}/%{name}-%{version}
