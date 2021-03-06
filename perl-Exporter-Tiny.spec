%define _buildid .2

Name:		perl-Exporter-Tiny
Version:	0.038
Release:	1%{?_buildid}%{?dist}
Summary:	An exporter with the features of Sub::Exporter but only core dependencies
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Exporter-Tiny/
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/Exporter-Tiny-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
# Module Build
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.17
# Module Runtime
BuildRequires:	perl(B)
BuildRequires:	perl(Carp)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.47
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(B)
Requires:	perl(Carp)

# Avoid doc-file dependency on perl(base)
%{?perl_default_filter}

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Exporter::Tiny supports many of Sub::Exporter's external-facing features
including renaming imported functions with the -as, -prefix and -suffix
options; explicit destinations with the into option; and alternative
installers with the installer option. But it's written in only about 40%%
as many lines of code and with zero non-core dependencies.

Its internal-facing interface is closer to Exporter.pm, with configuration
done through the @EXPORT, @EXPORT_OK and %%EXPORT_TAGS package variables.

Exporter::Tiny performs most of its internal duties (including resolution of
tag names to sub names, resolution of sub names to coderefs, and installation
of coderefs into the target package) as method calls, which means they can be
overridden to provide interesting behavior.

%prep
%setup -q -n Exporter-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
make test

%clean
rm -rf %{buildroot}

%files
%doc Changes CONTRIBUTING COPYRIGHT CREDITS LICENSE README
%doc examples/
%{perl_vendorlib}/Exporter/
%{_mandir}/man3/Exporter::Tiny.3pm*
%{_mandir}/man3/Exporter::Shiny.3pm*

%changelog
* Mon Dec 22 2014 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 0.038-1
- Adapt for AL/LL
- Add package support URL
- Import source package EPEL7/perl-Exporter-Tiny-0.038-1.el7

* Fri Apr  4 2014 Paul Howarth <paul@city-fan.org> - 0.038-1
- Update to 0.038
  - Added: Support Exporter.pm's import negation syntax qw( !foo )
  - Added: Support Exporter.pm's regexp import syntax qw( /foo/ )
  - Fix minor error in documentation of generators
  - Improved handling of hashrefs of options passed to tags, and hashrefs of
    options found within %%EXPORT_TAGS arrayrefs
  - Only attempt to merge hashes if we're sure they're both really hashes!

* Mon Mar 17 2014 Paul Howarth <paul@city-fan.org> - 0.036-2
- Sanitize for Fedora submission

* Thu Mar 13 2014 Paul Howarth <paul@city-fan.org> - 0.036-1
- Initial RPM version
