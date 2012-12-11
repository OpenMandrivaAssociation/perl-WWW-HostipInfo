%define upstream_name	 WWW-HostipInfo
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Get a country and city information from ip address
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildArch:	noarch

%description
Get a country and city information from ip address via www.hostip.info API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Of course network test don't work on cluster...
# %%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/WWW
%{_mandir}/*/*


%changelog
* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 523957
- update to 0.12

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.1
+ Revision: 463975
- update to 0.1

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 408098
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.08-8mdv2009.0
+ Revision: 258788
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.08-7mdv2009.0
+ Revision: 246708
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-5mdv2008.1
+ Revision: 137219
- spec cleanup

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-4mdv2008.1
+ Revision: 137107
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Nov 13 2006 Olivier Thauvin <nanardon@mandriva.org> 0.08-3mdv2007.0
+ Revision: 83895
- disable test to please to iurt
- fix buildrequires
- first mdv package
- Create perl-WWW-HostipInfo

