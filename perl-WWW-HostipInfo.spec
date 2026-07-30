%define upstream_name	 WWW-HostipInfo
%define upstream_version 0.14
Name:		perl-%{upstream_name}
Version:	0.14
Release:	2

Summary:	Get a country and city information from ip address
License:	GPL
Group:		Development/Perl
Url:		https://github.com/makamaka/WWW-HostipInfo
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MAKAMAKA/WWW-HostipInfo-0.14.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildArch:	noarch

%description
Get a country and city information from ip address via www.hostip.info API.

%prep
%setup -q -n WWW-HostipInfo-0.14

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
# Of course network test don't work on cluster...
# %%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/WWW
%{_mandir}/*/*


