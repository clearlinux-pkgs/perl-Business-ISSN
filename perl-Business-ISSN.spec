#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Business-ISSN
Version  : 1.004
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISSN-1.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISSN-1.004.tar.gz
Summary  : 'Perl extension for International Standard Serial Numbers'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Business-ISSN-license = %{version}-%{release}
Requires: perl-Business-ISSN-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
=pod
=encoding utf8
=for HTML <a href="https://travis-ci.org/briandfoy/business-issn"><img src="https://travis-ci.org/briandfoy/business-issn.svg?branch=master" /></a>

%package dev
Summary: dev components for the perl-Business-ISSN package.
Group: Development
Provides: perl-Business-ISSN-devel = %{version}-%{release}
Requires: perl-Business-ISSN = %{version}-%{release}

%description dev
dev components for the perl-Business-ISSN package.


%package license
Summary: license components for the perl-Business-ISSN package.
Group: Default

%description license
license components for the perl-Business-ISSN package.


%package perl
Summary: perl components for the perl-Business-ISSN package.
Group: Default
Requires: perl-Business-ISSN = %{version}-%{release}

%description perl
perl components for the perl-Business-ISSN package.


%prep
%setup -q -n Business-ISSN-1.004
cd %{_builddir}/Business-ISSN-1.004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Business-ISSN
cp %{_builddir}/Business-ISSN-1.004/LICENSE %{buildroot}/usr/share/package-licenses/perl-Business-ISSN/e70cdc8a8550ecaf70a1b64f088fbe41ce3ae9d8
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Business::ISSN.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Business-ISSN/e70cdc8a8550ecaf70a1b64f088fbe41ce3ae9d8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Business/ISSN.pm
