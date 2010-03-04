# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

%define	name	egroupware
%define	Name	eGroupware
%define	version	1.6.002
%define	Version	1.6.002
%define	release	%mkrel 10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Web-based groupware suite written in php
License:	GPL+
Group:		System/Servers
URL:		http://www.egroupware.org/
Source0:	http://downloads.sourceforge.net/%{name}/%{Name}-%{Version}.tar.bz2
Source1:	http://downloads.sourceforge.net/%{name}/%{Name}-egw-pear-%{Version}.tar.bz2
Source2:	http://downloads.sourceforge.net/%{name}/%{Name}-mydms-%{Version}.tar.bz2
Source3:	http://downloads.sourceforge.net/%{name}/%{Name}-icalsrv-%{Version}.tar.bz2
Source4:	http://downloads.sourceforge.net/%{name}/%{Name}-gallery-%{Version}.tar.bz2
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
Requires:	%{name}-calendar
Requires:	%{name}-etemplate
Requires:	%{name}-emailadmin
Suggests:	php-pdo_mysql
Suggests:	php-mcrypt
Suggests:	php-imap
Suggests:	php-pear-HTTP_WebDAV_Server
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%package etemplate
Summary:	The eGroupWare %{etemplate} application
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

%package icalsrv
Summary:        The eGroupWare iCal server
Group:   	System/Servers
Requires:       %{name} >= %{version}-%{release}
Obsoletes:	egroupware-contrib-icalsrv < 1.2.107-5
Obsoletes:	egroupware-contrib-egwical < 1.2.107-5
Provides:	egroupware-contrib-icalsrv = %{version}-%{release}
Provides:	egroupware-contrib-egwical = %{version}-%{release}

%description icalsrv
This package provides an iCal server for the eGroupware suite. NOTE that 
this function is deprecated from eGroupWare 1.6 onwards: it is 
recommended that you instead use GroupDAV, which is implemented in 
various eGroupWare components.

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

%package mydms 	 
Summary:        Advanced tool for shared files 	 
Group:          System/Servers 	 
Requires:       %{name} >= %{version}-%{release} 	 
Requires:	%{name}-egw-pear >= %{version}-%{release}
	  	 
%description mydms 	 
Advanced tool for shared files.

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
Requires:	%{name}-addressbook = %{version}-%{release}

%description wiki
This is the wiki app for eGroupWare.

%prep
%setup -q -n %{name}
%setup -q -T -D -b 1 -n %{name}
%setup -q -T -D -b 2 -n %{name}
%setup -q -T -D -b 3 -n %{name}
%setup -q -T -D -b 4 -n %{name}
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
cat >  %{buildroot}%{_webappconfdir}/%{name}.conf <<EOF
Alias /egroupware /var/www/egroupware

<Directory /var/www/egroupware>
  Options FollowSymLinks ExecCGI
  AllowOverride None
  Order allow,deny
  Allow from all
  DirectoryIndex index.html index.php
  AddHandler cgi-script .cgi
  AddDefaultCharset Off
  php_flag file_uploads on
  php_flag log_errors on
  php_flag magic_quotes_gpc off
  php_flag magic_quotes_runtime off
  php_flag register_globals off
  php_flag short_open_tag on
  php_flag track_vars on
  php_flag display_errors off
  php_value error_reporting 'E_ALL & ~E_NOTICE'
  php_value max_execution_time 90
  php_admin_value mbstring.func_overload 7
  php_value memory_limit 48M
  php_value session.gc_maxlifetime 14400
  php_value include_path .:/usr/share/pear
  php_value open_basedir /var/www/egroupware:/tmp:/usr/share/pear
  php_value upload_max_filesize 8M
  <Files ~ "\.inc\.php$">
    Order allow,deny
    Deny from all
  </Files>
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/sql>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/src>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/thm>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/cache>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/scripts>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/www_root>

	php_admin_value output_buffering 16000
	php_admin_value variables_order GPCS
	php_admin_value implicit_flush 0
	php_admin_value register_globals 0
	php_admin_value register_argc_argv 0
	php_admin_value magic_quotes_gpc 0
	php_admin_value session.use_trans_sid 0

</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/include>
    Deny from all
</Directory>

<Directory /var/www/egroupware/phpsysinfo>
  php_value open_basedir /
</Directory>

<Location /egroupware/icalsrv/icalsrv.php>
    Script PUT /var/www/egroupware/icalsrv/icalsrv.php
    AddHandler ical/ics .ics
    Action ical/ics /var/www/egroupware/icalsrv/icalsrv.php
    Order allow,deny
    Allow from all
</Location>

<Location /egroupware/rpc.php>
    php_admin_value mbstring.func_overload 0
    Order allow,deny
    Allow from all
</Location>
EOF

# install files
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/default/files
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/default/backup
install -d -m 755 %{buildroot}%{_var}/www/%{name}
cp -aRf * %{buildroot}%{_var}/www/%{name}

# setup the config file: this dummy content triggers the setup process 
# (from upstream's package)
cat > %{buildroot}%{_localstatedir}/lib/%{name}/header.inc.php << EOF
<?php
// dummy setup file
if (strpos(\$_SERVER['PHP_SELF'],'/setup/') === false)
{
        header('Location: /egroupware/setup/');
        exit;
}
EOF
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

%files egw-pear
%defattr(-,root,root)
%{_var}/www/%{name}/egw-pear

%files emailadmin
%defattr(-,root,root)
%{_var}/www/%{name}/emailadmin

%files etemplate
%defattr(-,root,root)
%doc etemplate/doc/*
%{_var}/www/%{name}/etemplate

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

%files icalsrv
%defattr(-,root,root)
%doc icalsrv/doc/*
%{_var}/www/%{name}/icalsrv

%files importexport
%defattr(-,root,root)
%{_var}/www/%{name}/importexport

%files infolog
%defattr(-,root,root)
%{_var}/www/%{name}/infolog

%files manual
%defattr(-,root,root)
%{_var}/www/%{name}/manual

%files mydms 	 
%defattr(-,root,root) 	 
%doc mydms/{Changelog,README}
%{_var}/www/%{name}/mydms

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
