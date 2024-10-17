%define upstream_name	 Linux-CDROM
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

Summary:	An interface to Linux CDROM device
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Linux/%{upstream_name}-%{upstream_version}.tar.gz

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.20.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 555996
- rebuild for perl 5.12

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 474665
- using %%perl_convert_version
- update to 0.02

* Mon Dec 07 2009 Bruno Cornec <bcornec@mandriva.org> 0.02-1mdv2010.1
+ Revision: 474571
- Add Linux:CDROM perl module
- create perl-Linux-CDROM

