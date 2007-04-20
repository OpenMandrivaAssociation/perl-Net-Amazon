
%define module	Net-Amazon
%define name	perl-%{module}
%define version	0.40
%define rel	1

Summary:	Framework for accessing amazon.com via SOAP and XML/HTTP
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%description
Net::Amazon provides an object-oriented interface to amazon.com's
SOAP and XML/HTTP interfaces. This way it's possible to create applications
using Amazon's vast amount of data via a functional interface, without
having to worry about the underlying communication mechanism.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Net
%{_mandir}/man3/*


