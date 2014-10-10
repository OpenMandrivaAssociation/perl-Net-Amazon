%define upstream_name	 Net-Amazon
%define upstream_version 0.62

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.62
Release:	2

Summary:	Framework for accessing amazon.com via SOAP and XML/HTTP
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/Net-Amazon-0.62.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Amazon provides an object-oriented interface to amazon.com's
SOAP and XML/HTTP interfaces. This way it's possible to create applications
using Amazon's vast amount of data via a functional interface, without
having to worry about the underlying communication mechanism.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Net
%{_mandir}/man3/*

%changelog
* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.590.0-1mdv2010.1
+ Revision: 461334
- update to 0.59

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.570.0-1mdv2010.0
+ Revision: 435714
- update to 0.57

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.560.0-1mdv2010.0
+ Revision: 432824
- update to 0.56

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.550.0-1mdv2010.0
+ Revision: 399266
- update to 0.55
- using %%perl_convert_version
- fixed license field

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.54-1mdv2010.0
+ Revision: 387780
- update to new version 0.54

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.53-1mdv2010.0
+ Revision: 387015
- update to new version 0.53

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.51-1mdv2010.0
+ Revision: 383531
- update to new version 0.51

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-1mdv2009.0
+ Revision: 270393
- update to new version 0.50

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.49-2mdv2009.0
+ Revision: 268622
- rebuild early 2009.0 package (before pixel changes)

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.49

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.48-1mdv2008.1
+ Revision: 152911
- update to new version 0.48
- update to new version 0.48

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.47-1mdv2008.1
+ Revision: 133602
- update to new version 0.47

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.46-1mdv2008.1
+ Revision: 109580
- update to new version 0.46

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-1mdv2008.1
+ Revision: 105895
- update to new version 0.44

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-1mdv2008.0
+ Revision: 46655
- update to new version 0.43

* Fri Apr 20 2007 Anssi Hannula <anssi@mandriva.org> 0.40-1mdv
+ Revision: 16260
- 0.40


* Tue Feb 27 2007 Anssi Hannula <anssi@mandriva.org> 0.39-1mdv2007.0
+ Revision: 126272
- 0.39
- 0.38

* Sun Jan 21 2007 Anssi Hannula <anssi@mandriva.org> 0.36-1mdv2007.1
+ Revision: 111459
- 0.36
- Import perl-Net-Amazon

* Mon May 29 2006 Anssi Hannula <anssi@mandriva.org> 0.35-1mdv2007.0
- initial Mandriva package


