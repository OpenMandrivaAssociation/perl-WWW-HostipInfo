%define module	WWW-HostipInfo
%define name	perl-%{module}
%define version	0.08
%define release %mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Get a country and city information from ip address
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/modules/by-module/WWW/%{module}-%{version}.tar.bz2
BuildRequires: perl(LWP::UserAgent)
BuildArch:  noarch
Buildroot:	%{_tmppath}/%{name}-%{version}


%description
Get a country and city information from ip address via www.hostip.info API.

%prep
%setup -q -n %{module}-%{version}

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
