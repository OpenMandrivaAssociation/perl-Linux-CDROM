%define upstream_name	 Linux-CDROM
%define upstream_version 0.02

Name: 		perl-%{upstream_name}
Version: 	%{upstream_version}
Release:	%mkrel 1

Summary:	An interface to Linux CDROM device
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Linux/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
common recipes featuring your CDROM drive as its main ingredient

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*/Linux/CDROM*
%{perl_vendorlib}/*/*/Linux/CDROM/*
%{_mandir}/*/*

