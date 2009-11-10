%define upstream_name	 WWW-HostipInfo
%define upstream_version 0.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Get a country and city information from ip address
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(LWP::UserAgent)
BuildArch:  noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}


%description
Get a country and city information from ip address via www.hostip.info API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check

# Of course network test don't work on cluster...
# %%make test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/WWW
%{_mandir}/*/*
