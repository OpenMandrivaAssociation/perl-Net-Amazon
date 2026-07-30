%define upstream_name	 Net-Amazon
%define upstream_version 0.62
Name:		perl-%{upstream_name}
Version:	0.62
Release:	2

Summary:	Framework for accessing amazon.com via SOAP and XML/HTTP
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://github.com/boumenot/p5-Net-Amazon
Source0:	https://cpan.metacpan.org/authors/id/B/BO/BOUMENOT/Net-Amazon-0.62.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Amazon provides an object-oriented interface to amazon.com's
SOAP and XML/HTTP interfaces. This way it's possible to create applications
using Amazon's vast amount of data via a functional interface, without
having to worry about the underlying communication mechanism.

%prep
%setup -q -n Net-Amazon-0.62

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Net
%{_mandir}/man3/*

