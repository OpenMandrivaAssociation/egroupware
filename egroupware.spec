# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

%define	name	egroupware
%define	Name	eGroupware
%define	version	1.8.004.20120423
%define	Version	1.8.004.20120423
%define	release 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Web-based groupware suite written in php
License:	GPL+
Group:		System/Servers
URL:		http://www.egroupware.org/
Source0:	http://downloads.sourceforge.net/%{name}/%{Name}-%{Version}.tar.bz2
Source1:	http://downloads.sourceforge.net/%{name}/%{Name}-egw-pear-%{Version}.tar.bz2
Source2:	http://downloads.sourceforge.net/%{name}/%{Name}-gallery-%{Version}.tar.bz2
Patch0:		eGroupware-1.6.002-preferred_php_binary.patch

%if %mdkversion < 201010
Requires(post):   rpm-helper
Requires(postun):   rpm-helper
%endif
Requires:	apache-mod_php
Requires:	php-xml
Requires:	php-gd
Requires:	php-cli
Requires:	php-dom
Requires:	php-zip
Requires:   php-pear-XML_Parser
Requires:	%{name}-calendar
Requires:	%{name}-etemplate
Requires:	%{name}-emailadmin
Suggests:	php-pdo_mysql
Suggests:	php-mcrypt
Suggests:	php-imap
Provides:	egroupware-addressbook = %{version}-%{release}
Provides:	egroupware-etemplate = %{version}-%{release}
Provides:	egroupware-contrib-icalsrv = %{version}-%{release}
Provides:	egroupware-contrib-egwical = %{version}-%{release}
Provides:	egroupware-icalsrv = %{version}-%{release}
Provides:	egroupware-mydms = %{version}-%{release}
Obsoletes:	egroupware-addressbook < 1.8.001.2010111-1
Obsoletes:	egroupware-etemplate < 1.8.001.2010111-1
Obsoletes:	egroupware-icalsrv < 1.8.001.2010111-1
Obsoletes:	egroupware-mydms < 1.8.001.2010111-1
Obsoletes:	egroupware-contrib-icalsrv < 1.2.107-5
Obsoletes:	egroupware-contrib-egwical < 1.2.107-5
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
eGroupWare is a web-based groupware suite written in PHP. 
The core package provides the admin, setup, phpgwapi and preferences
packages. It also provides an API for developing additional applications. 
See the egroupware apps project for add-on apps.

%package bookmarks
Summary:	The eGroupWare bookmarks application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description bookmarks
Manage your bookmarks with eGroupWare. Has Netscape plugin.

%package calendar
Summary:	The eGroupWare calendar application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description calendar
Powerful calendar with meeting request system, Alarms, CalDAV and E-Mail 
support, and ACL security.

%package developer_tools
Summary:	The eGroupWare developer_tools application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description developer_tools
The TranslationTools allow to create and extend translations-files for
eGroupWare. They can search the sources for new / added phrases and show you
the ones missing in your language. 

%package egw-pear
Summary:	php-pear classes for eGroupWare
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description egw-pear
egw-pear contains modified pear classes necessary for eGroupware.

%package emailadmin
Summary:	The eGroupWare emailadmin application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}
Requires:	%{name}-egw-pear >= %{version}-%{release}
Suggests:	php-pear-Auth_SASL

%description emailadmin
EmailAdmin enables user email account maintenance in eGroupWare.

%package felamimail
Summary:	The eGroupWare felamimail application
Group:		System/Servers
Requires:	%{name}-emailadmin = %{version}-%{release}
Requires:	%{name}-egw-pear = %{version}-%{release}

%description felamimail
The felamimail Email Reader is an alternative email application for eGroupWare.

%package filemanager
Summary:	The eGroupWare filemanager application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}
Requires:	%{name}-egw-pear >= %{version}-%{release}

%description filemanager
This is the filemanager app for eGroupWare.

%package gallery
Summary:	The eGroupWare gallery application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}
Requires:	%{name}-egw-pear >= %{version}-%{release}

%description gallery
A gallery application for eGroupWare (a port of gallery2).

%package importexport
Summary:	The eGroupWare import/export function
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description importexport
This package provides a general import/export function for the 
eGroupware suite.

%package infolog
Summary:	The eGroupWare infolog application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description infolog
This is the infolog app for eGroupWare.

%package manual
Summary:	The eGroupWare messenger application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description manual
This is the manual app for eGroupWare.

%package news_admin
Summary:	The eGroupWare news_admin application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description news_admin
This is the news_admin app for eGroupWare.

%package notifications
Summary:	User notifications for eGroupWare
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description notifications
This package provides pop-up user notifications for the eGroupWare 
suite.

%package phpbrain
Summary:	The eGroupWare phpbrain application
Group:		System/Servers

%description phpbrain
This is the phpbrain app for eGroupWare.

%package phpsysinfo
Summary:	The eGroupWare phpsysinfo application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description phpsysinfo
This is the cire phpsysinfo of eGroupWare.

%package polls
Summary:	The eGroupWare polls application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description polls
This is the polls app for eGroupWare.

%package projectmanager
Summary:	The eGroupWare projects application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description projectmanager
This is the projects app for eGroupWare.

%package registration
Summary:	The eGroupWare registration application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description registration
This is the registration app for eGroupWare.

%package sambaadmin
Summary:	The eGroupWare sambaadmin application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description sambaadmin
Manage Samba resources with egroupware.

%package sitemgr
Summary:	The eGroupWare sitemgr application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description sitemgr
This is the sitemgr app for eGroupWare.

%package syncml
Summary:	The eGroupWare syncml application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description syncml
Synchronisation for agenda, contacts and todo list.

%package timesheet
Summary:	The eGroupWare timesheet application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description timesheet
Free time management.

%package tracker
Summary:	The eGroupWare tracker application
Group:		System/Servers
Requires:	%{name} = %{version}-%{release}

%description tracker
This is the tracker app for eGroupWare.

%package wiki
Summary:	The eGroupWare wiki application
Group:		System/Servers

%description wiki
This is the wiki app for eGroupWare.

%prep
%setup -q -n %{name}
%setup -q -T -D -b 1 -n %{name}
%setup -q -T -D -b 2 -n %{name}
%patch0 -p1

# cleanup
find . -type d -name CVS | xargs rm -rf
find . -type f -name *.old -o -name *.backup | xargs rm -f
find . -type f -empty | xargs rm -f
find . -type f | xargs chmod 644
find . -name .htaccess |xargs rm -f
find . -name .svn | xargs rm -rf

%build

%install
rm -rf %{buildroot}

# apache configuration
install -d -m 755 %{buildroot}%{_webappconfdir}
sed 's,\/usr\/share\/egroupware,\/var\/www\/egroupware,' doc/rpm-build/apache.conf > %{buildroot}%{_webappconfdir}/%{name}.conf

# install files
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/default/files
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/default/backup
install -d -m 755 %{buildroot}%{_var}/www/%{name}
cp -aRf * %{buildroot}%{_var}/www/%{name}

# setup the config file: this dummy content triggers the setup process 
# (from upstream's package)
cp doc/rpm-build/header.inc.php %{buildroot}%{_localstatedir}/lib/%{name}/header.inc.php
ln -s %{_localstatedir}/lib/%{name}/header.inc.php %{buildroot}%{_var}/www/%{name}/header.inc.php

# post-install cleanup
rm -rf %{buildroot}%{_var}/www/%{name}/doc 
rm -rf %{buildroot}%{_var}/www/%{name}/*/doc 
rm -f %{buildroot}%{_var}/www/%{name}/felamimail/{COPYING,Changelog,README,TODO}
# doc cleanup
rm -f doc/Makefile
rm -rf doc/rpm-build


%post
%if %mdkversion < 201010
%_post_webapp
%endif
    
%postun
%if %mdkversion < 201010
%_postun_webapp
%endif
		    
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/* 
%doc phpgwapi/doc/*
# Apache configuration file
%config(noreplace) %{_webappconfdir}/%{name}.conf
# Header config file
%attr(640,apache,apache) %config(noreplace) %{_localstatedir}/lib/%{name}/header.inc.php
# top level dir and files
%dir %{_var}/www/%{name}
%{_var}/www/%{name}/*.php
%{_var}/www/%{name}/groupdav.htaccess
%{_var}/www/%{name}/header.inc.php.template
%{_var}/www/%{name}/phpgwapi
%{_var}/www/%{name}/addressbook
%{_var}/www/%{name}/admin
%{_var}/www/%{name}/etemplate
%{_var}/www/%{name}/preferences
%{_var}/www/%{name}/setup
%{_var}/www/%{name}/home
%{_var}/www/%{name}/resources
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}/default
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}/default/files
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}/default/backup

%files bookmarks
%defattr(-,root,root)
%{_var}/www/%{name}/bookmarks

%files calendar
%defattr(-,root,root)
%{_var}/www/%{name}/calendar

%files developer_tools
%defattr(-,root,root)
%doc developer_tools/doc/*
%{_var}/www/%{name}/developer_tools

%files egw-pear
%defattr(-,root,root)
%{_var}/www/%{name}/egw-pear

%files emailadmin
%defattr(-,root,root)
%{_var}/www/%{name}/emailadmin

%files felamimail
%defattr(-,root,root)
%doc felamimail/{Changelog,README,TODO}
%{_var}/www/%{name}/felamimail

%files filemanager
%defattr(-,root,root)
%{_var}/www/%{name}/filemanager

%files gallery
%defattr(-,root,root)
%{_var}/www/%{name}/gallery

%files importexport
%defattr(-,root,root)
%{_var}/www/%{name}/importexport

%files infolog
%defattr(-,root,root)
%{_var}/www/%{name}/infolog

%files manual
%defattr(-,root,root)
%{_var}/www/%{name}/manual

%files news_admin
%defattr(-,root,root)
%doc news_admin/doc/*
%{_var}/www/%{name}/news_admin

%files notifications
%defattr(-,root,root)
%{_var}/www/%{name}/notifications

%files phpbrain
%defattr(-,root,root)
%{_var}/www/%{name}/phpbrain

%files phpsysinfo
%defattr(-,root,root)
%{_var}/www/%{name}/phpsysinfo

%files polls
%defattr(-,root,root)
%doc polls/doc/*
%{_var}/www/%{name}/polls

%files projectmanager
%defattr(-,root,root)
%{_var}/www/%{name}/projectmanager

%files registration
%defattr(-,root,root)
%doc registration/doc/*
%{_var}/www/%{name}/registration

%files sambaadmin
%defattr(-,root,root)
%{_var}/www/%{name}/sambaadmin

%files sitemgr
%defattr(-,root,root)
%{_var}/www/%{name}/sitemgr

%files syncml
%defattr(-,root,root)
%{_var}/www/%{name}/syncml

%files timesheet
%defattr(-,root,root)
%{_var}/www/%{name}/timesheet

%files tracker
%defattr(-,root,root)
%{_var}/www/%{name}/tracker

%files wiki
%defattr(-,root,root)
%doc wiki/doc/*
%{_var}/www/%{name}/wiki


%changelog
* Fri Apr 27 2012 Zombie Ryushu <ryushu@mandriva.org> 1.8.004.20120423-1mdv2012.0
+ Revision: 794071
- Needed upgrade due to security issues

* Thu Jul 28 2011 Adam Williamson <awilliamson@mandriva.org> 1.8.001.20110421-2
+ Revision: 692112
- drop the pear webdav_server suggests: egw uses a modified internal copy

* Fri Jul 08 2011 Adam Williamson <awilliamson@mandriva.org> 1.8.001.20110421-1
+ Revision: 689351
- new release 1.8.001.20110421

* Wed Mar 02 2011 Adam Williamson <awilliamson@mandriva.org> 1.8.001.20110216-1
+ Revision: 641360
- new release 1.8.001.20110216
- bump rev to 2 to facilitate move from testing to updates

  + Alexandre Felipe Muller de Souza <alexandrefm@mandriva.com>
    - Updating eGroupware for newer community version

* Wed Dec 01 2010 Adam Williamson <awilliamson@mandriva.org> 1.8.001.20101201-1mdv2011.0
+ Revision: 604599
- new release 1.8 final (as announced on ml, though it's still date-versioned)

* Wed Mar 10 2010 Adam Williamson <awilliamson@mandriva.org> 1.6.003-1mdv2010.1
+ Revision: 517267
- new release 1.6.003

* Thu Mar 04 2010 Adam Williamson <awilliamson@mandriva.org> 1.6.002-10mdv2010.1
+ Revision: 514330
- revert a test patch i didn't mean to commit
- escape SERVER variable in apache config (thanks anne)

* Mon Mar 01 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.002-9mdv2010.1
+ Revision: 513133
- rely on filetrigger for reloading apache configuration begining with 2010.1, rpm-helper macros otherwise
- use herein documents instead of external source for apache configuration
- no need to prefix apache configuration file with an ordering number
- spec cleanup

* Wed Feb 10 2010 Adam Williamson <awilliamson@mandriva.org> 1.6.002-8mdv2010.1
+ Revision: 503986
- fix a path in apache config file (d'oh, thanks anne)

* Fri Jan 22 2010 Adam Williamson <awilliamson@mandriva.org> 1.6.002-7mdv2010.1
+ Revision: 494924
- ok, found the real fix for the config file issue upstream

* Fri Jan 22 2010 Adam Williamson <awilliamson@mandriva.org> 1.6.002-6mdv2010.1
+ Revision: 494918
- stop trying to hack around the config file issue, can't make it work
- (thanks to misc) a way of handling the config file problem that works
- actually, don't ghost it, just make it empty

* Fri Jan 22 2010 Adam Williamson <awilliamson@mandriva.org> 1.6.002-4mdv2010.1
+ Revision: 494895
- fix some of the apache config file changes
- update the apache configuration file from upstream's
- fix a typo (thanks anne)
- add some more dependencies
- it uses pdo_mysql, not just mysql - update the suggest

* Fri Jan 22 2010 Adam Williamson <awilliamson@mandriva.org> 1.6.002-3mdv2010.1
+ Revision: 494860
- add some obsoletes/provides to migrate icalsrv from contrib package

* Fri Jan 22 2010 Adam Williamson <awilliamson@mandriva.org> 1.6.002-2mdv2010.1
+ Revision: 494852
- add some hard and soft dependencies based on upstream spec + docs
- clean up a stray GPL copy
- clean some descriptions
- add modules that were moved to be separate tarballs since 1.2

* Fri Jan 22 2010 Adam Williamson <awilliamson@mandriva.org> 1.6.002-1mdv2010.1
+ Revision: 494803
- update package layout for new version
- correct license tag
- new release 1.6.002

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2.107-4mdv2010.0
+ Revision: 428531
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.2.107-3mdv2009.0
+ Revision: 240661
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Jun 25 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.107-1mdv2008.0
+ Revision: 43792
- 1.2.107-2 (security release)
- fix deps


* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.106-2mdv2007.1
+ Revision: 144969
- 1.2.106-2 (bugfix and maintainance release)
- bunzipped the apache config file
- the changelog was present in the spec file for some reason

* Tue Jan 02 2007 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.106-1mdv2007.1
+ Revision: 103032
- New version for security and bugs fixes
- New version bug and security fixes
- Import egroupware

* Mon Sep 11 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.105-1mdk
- new version bug and security fixes

* Fri Jul 21 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.104-1mdk
- bug fix

* Mon Jun 12 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.102-1mdk
- new version with lots of bug fix

* Mon Jun 05 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.2-3mdk
- add doc dir from phpgwapi (ldap schemas)

* Mon May 22 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.2-2mdk
- delete .svn directories
- fix archive permission

* Mon May 22 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.2-1mdk
- new version for bug fix

* Sat May 20 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.1-3mdk
- fix require

* Sun May 14 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2mdk
- fix default directories and their permissions
- make it use the default php-cli and fix deps

* Fri Apr 21 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.1-1mdk
- new major version
- improve apache configuration (thanks Oden)
- split main and contrib modules for egroupware

* Wed Oct 26 2005 Anne Nicolas <anne.nicolas@mandriva.com> 1.0-9.3mdk
- security and bugfix release

* Thu Aug 25 2005 Anne Nicolas <anne.nicolas@mandriva.com> 1.0-9.1mdk
- fix security bug with xmlrpc

* Wed Jul 13 2005 Anne Nicolas <anne.nicolas@mandriva.com> 1.0-8.3mdk
- fix security bug

* Tue Jun 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-8.2mdk
- fix deps

* Mon Jun 06 2005 Anne Nicolas <anne.nicolas@mandriva.com> 1.0-8.1mdk
- fix missing documentation (ldap schemas)

* Mon Apr 18 2005 Anne Nicolas <anne.nicolas@mandriva.com> 1.0-8mdk
- new version
- fix permissions

* Fri Feb 18 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-7mdk
- spec file cleanups, remove the ADVX-build stuff
- speed up the build
- fix some rpmlint errors...

* Sun Nov 07 2004 Anne Nicolas <anne@mandrake.org> 1.0-6mdk
- new version, security release for JiNN module

* Sun Oct 10 2004 Anne Nicolas <anne@mandrake.org> 1.0-5mdk
- fix permissions to apache user
- add php-gd require

* Tue Sep 28 2004 Anne Nicolas <anne@mandrake.org> 1.0-4mdk
- new version, fix bugs

* Sat Aug 28 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-3mdk
- re-define %%{_sysconfdir}/httpd/conf.d to %%{_sysconfdir}/httpd/webapps.d

* Wed Aug 25 2004 Anne Nicolas <anne@mandrake.org> 1.0-1.1mdk
- fix security issues

* Tue Aug 17 2004 Anne Nicolas <anne@mandrake.org> 1.0-1mdk
- first stable release
- add manual package for egroupware
- drop doc for phpldapadmin and phpbrain

* Sun May 02 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0-0.RC5.1mdk
- new version
- drop .htaccess files, use apache configuration files instead
- standard perms on %%{_sysconfdir}/httpd/conf.d/* files

