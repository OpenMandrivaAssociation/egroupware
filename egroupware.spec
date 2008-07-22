# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

%define	name	egroupware
%define	Name	eGroupWare
%define	version	1.2.107
%define	Version	1.2.107-2
%define	release	%mkrel 3
%define order	71

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Web-based groupware suite written in php
License:	GPL
Group:		System/Servers
URL:		http://www.egroupware.org/
Source0:	%{Name}-%{Version}.tar.bz2
Source1:	%{name}-apache.conf
Patch0:		eGroupWare-1.2-1-preferred_php_binary.diff
Requires(pre): rpm-helper
Requires (postun) : rpm-helper
Requires(pre):  apache-conf >= 2.0.54
Requires(pre):  apache-mpm >= 2.0.54
Requires:	apache-mod_php php-xml php-gd
Requires:	php-cli
Requires:	%{name}-calendar %{name}-etemplate
BuildArch:	noarch
BuildRequires:	file
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
eGroupWare is a web-based groupware suite written in PHP. 
The core package provides the admin, setup, phpgwapi and preferences
packages. It also provides an API for developing additional applications. 
See the egroupware apps project for add-on apps.

%package addressbook
Summary:	The eGroupWare addressbook application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description addressbook
Contact manager with Vcard support.
addressbook is the egroupware default contact application.
It makes use of the phpgroupware contacts class to store and retrieve 
contact information via SQL, LDAP or Active Directory.

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
Powerful calendar with meeting request system, Alarms, ICal and E-Mail support,
and ACL security.

%package developer_tools
Summary:	The eGroupWare developer_tools application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description developer_tools
The TranslationTools allow to create and extend translations-files for
eGroupWare. They can search the sources for new / added phrases and show you
the ones missing in your language. 

%package docs
Summary:	The eGroupWare docs
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description docs
This is the docs for eGroupWare.

%package emailadmin
Summary:	The eGroupWare emailadmin application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description emailadmin
EmailAdmin allow to maintain User email accounts 

%package etemplate
Summary:	The eGroupWare %{etempalte} application
Group:		System/Servers
Requires:	%{name}-addressbook = %{version}-%{release}

%description etemplate
eTemplates are a new widget-based template system for eGroupWare with an
interactive editor and a database table-editor (creates tables_current.inc.php
and updates automaticaly tables_update.inc.php)

%package felamimail
Summary:	The eGroupWare felamimail application
Group:		System/Servers
Requires:	%{name}-emailadmin = %{version}-%{release}

%description felamimail
The felamimail Email Reader is a other Email application for phpgw eGroupWare.

%package filemanager
Summary:	The eGroupWare filemanager application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description filemanager
This is the filemanager app for eGroupWare.

%package infolog
Summary:	The eGroupWare infolog application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description infolog
This is the infolog app for eGroupWare.

%package manual
Summary:        The eGroupWare messenger application
Group:          System/Servers
Requires:       %{name} >= %{version}-%{release}

%description manual
This is the manual app for eGroupWare.

%package mydms
Summary:        Advanced tool for shared files
Group:          System/Servers
Requires:       %{name} >= %{version}-%{release}

%description mydms
Advanced tool for shared files.

%package news_admin
Summary:	The eGroupWare news_admin application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description news_admin
This is the news_admin app for eGroupWare.

%package phpbrain
Summary:	The eGroupWare phpbrain application
Group:		System/Servers
Requires:	%{name}-addressbook = %{version}-%{release}

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
Summary:        The eGroupWare sambaadmin application
Group:          System/Servers
Requires:       %{name} >= %{version}-%{release}

%description sambaadmin
Manage Samba resources with egroupware.

%package sitemgr
Summary:	The eGroupWare sitemgr application
Group:		System/Servers
Requires:	%{name} >= %{version}-%{release}

%description sitemgr
This is the sitemgr app for eGroupWare.

%package syncml
Summary:        The eGroupWare syncml application
Group:          System/Servers
Requires:       %{name} >= %{version}-%{release}

%description syncml
Synchronisation for agenda, contacts and todo list.

%package timesheet
Summary:        The eGroupWare timesheet application
Group:          System/Servers
Requires:       %{name} >= %{version}-%{release}

%description timesheet
Free time management.

%package wiki
Summary:	The eGroupWare wiki application
Group:		System/Servers
Requires:	%{name}-addressbook = %{version}-%{release}

%description wiki
This is the wiki app for eGroupWare.

%package workflow
Summary:        The eGroupWare workflow application
Group:          System/Servers
Requires:       %{name}-addressbook = %{version}-%{release}

%description workflow
This is the workflow app for eGroupWare.

%prep

%setup -q -n %{name}
%patch0 -p0

# cleanup
find . -type d -name CVS | xargs rm -rf
find . -type f -name *.old -o -name *.backup | xargs rm -f
find . -type f -empty | xargs rm -f
find . -type f | xargs chmod 644
find . -name .htaccess |xargs rm -f
find . -name .svn | xargs rm -rf

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build

%install
rm -rf  %{buildroot}

# apache configuration
install -d -m 755 %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/%{order}_%{name}.conf

# install files
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/default/files
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/default/backup
install -d -m 755 %{buildroot}%{_var}/www/%{name}
cp -aRf * %{buildroot}%{_var}/www/%{name}

# post-install cleanup
rm -rf %{buildroot}%{_var}/www/%{name}/doc 
rm -rf %{buildroot}%{_var}/www/%{name}/*/doc 
rm -f %{buildroot}%{_var}/www/%{name}/felamimail/{COPYING,Changelog,README,TODO}
rm -rf %{buildroot}%{_var}/www/%{name}/infolog/debian
# doc cleanup
rm -f doc/Makefile
rm -rf doc/rpm-build


%post
if [ -f %{_var}/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi
    
%postun
if [ "$1" = "0" ]; then
    if [ -f %{_var}/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart 1>&2
    fi
fi
		    
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/* 
%doc phpgwapi/doc/*
# Apache configuration file
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/%{order}_%{name}.conf
# top level dir and files
%dir %{_var}/www/%{name}
%{_var}/www/%{name}/*.php
%{_var}/www/%{name}/header.inc.php.template
%{_var}/www/%{name}/phpgwapi
%{_var}/www/%{name}/admin
%{_var}/www/%{name}/preferences
%{_var}/www/%{name}/setup
%{_var}/www/%{name}/home
%{_var}/www/%{name}/resources
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}/default
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}/default/files
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}/default/backup

%files addressbook
%defattr(-,root,root)
%{_var}/www/%{name}/addressbook

%files bookmarks
%defattr(-,root,root)
%{_var}/www/%{name}/bookmarks

%files calendar
%defattr(-,root,root)
%doc calendar/doc/*
%{_var}/www/%{name}/calendar

%files developer_tools
%defattr(-,root,root)
%doc developer_tools/doc/*
%{_var}/www/%{name}/developer_tools

%files emailadmin
%defattr(-,root,root)
%{_var}/www/%{name}/emailadmin

%files etemplate
%defattr(-,root,root)
%doc etemplate/doc/*
%{_var}/www/%{name}/etemplate

%files felamimail
%defattr(-,root,root)
%doc felamimail/{COPYING,Changelog,README,TODO}
%{_var}/www/%{name}/felamimail

%files filemanager
%defattr(-,root,root)
%doc filemanager/doc/*
%{_var}/www/%{name}/filemanager

%files infolog
%defattr(-,root,root)
%{_var}/www/%{name}/infolog

%files manual
%defattr(-,root,root)
%{_var}/www/%{name}/manual

%files mydms
%defattr(-,root,root)
%{_var}/www/%{name}/mydms

%files news_admin
%defattr(-,root,root)
%doc news_admin/doc/*
%{_var}/www/%{name}/news_admin

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
%doc sitemgr/doc/*
%{_var}/www/%{name}/sitemgr

%files syncml
%defattr(-,root,root)
%{_var}/www/%{name}/syncml

%files timesheet
%defattr(-,root,root)
%{_var}/www/%{name}/timesheet

%files wiki
%defattr(-,root,root)
%doc wiki/doc/*
%{_var}/www/%{name}/wiki

%files workflow
%defattr(-,root,root)
%{_var}/www/%{name}/workflow
