%define module	WWW-HostipInfo
%define name	perl-%{module}
%define version	0.08
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	get a country and city information from ip address
License:	GPL
Group:		Development/Perl
Source:		%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/RPM4/
Buildroot:	%{_tmppath}/%{name}-root
BuildArch: noarch
BuildRequires: perl(LWP::UserAgent)


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
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/*/*


