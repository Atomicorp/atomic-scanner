
Summary:        Atomic Secured Linux anti-spam/anti-virus module
Name:           atomic-scanner
Version:        0.3
Release:        1
URL:            http://www.atomicorp.com/
Packager:	Scott R. Shinn <scott@atomicrocketturtle.com>
Vendor:		Atomic Corporate Industries
Source0:        %{name}-%{version}.tar.gz
Source1:	atomic-scanner.conf
License:        Commercial
Group:          System/Servers
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires:       psa asl 
Requires:	qmail-scanner >= 2.04-2 clamd



%description
Atomic Scanner is an anti-virus, and anti-spam module for Plesk.
Atomic Scanner is a component of Atomic Secured Linux.


%prep
	
%setup 


%build
find . -name .\*swp -exec rm -f {} \;
find . -name \*bak -exec rm -f {} \;
find . -name \*old -exec rm -f {} \;

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/var/asl/bin
%{__mkdir_p} %{buildroot}/var/asl/data
%{__mkdir_p} %{buildroot}/usr/local/psa/admin/htdocs/%{name}
%{__mkdir_p} %{buildroot}/usr/local/psa/admin/htdocs/images/custom_buttons
%{__mkdir_p} %{buildroot}/etc/cron.daily
%{__mkdir_p} %{buildroot}/etc/asl/

%{__cp} -r www/* %{buildroot}/usr/local/psa/admin/htdocs/%{name}
%{__install} -m 0644 turtleyellow.gif %{buildroot}/usr/local/psa/admin/htdocs/images/custom_buttons/atomic-scanner-button.gif

%{__install} -m 0700 bin/atomic-scanner %{buildroot}/var/asl/bin/atomic-scanner
%{__install} -m 0700 bin/data-generate.php %{buildroot}/var/asl/bin/data-generate.php
%{__install} -m 0700 cron/atomic-scanner.cron %{buildroot}/etc/cron.daily/atomic-scanner
%{__install} -m 0644 sql/tortix.sql %{buildroot}/var/asl/data/tortix.sql
%{__install} -m 0640 %{SOURCE1} %{buildroot}/etc/asl/atomic-scanner.conf


%clean
%{__rm} -rf %{buildroot}

%post 

# Set up the button in PSA
MYSQL="mysql -u admin -p`cat /etc/psa/.psa.shadow` psa "
ATOMIC_VERSION=`echo "select text from custom_buttons where text = 'Atomic Scanner' " | $MYSQL`


if [ ! "$ATOMIC_VERSION" ]; then
  echo "insert into custom_buttons (sort_key,level,place,text,url,conhelp,options,file) values ('1','1','navigation','Atomic Scanner','/atomic-scanner/index.php','Anti-Spam/Anti-Virus Control Panel','256', 'atomic-scanner-button.gif'); " | $MYSQL
fi

# Install the DB

$MYSQL < /var/asl/data/tortix.sql


# Add atomic-scanner to sudoers
if !  grep -q ^psaadm.*atomic-scanner /etc/sudoers ; then
  echo "psaadm  ALL = NOPASSWD: /var/asl/bin/atomic-scanner" >> /etc/sudoers
fi

%postun
MYSQL="mysql -u admin -p`cat /etc/psa/.psa.shadow` psa "
echo "delete from custom_buttons where text = 'Anti-Spam/Anti-Virus Control Panel';" | $MYSQL



%files
%defattr(-,root,root)
%attr(0640, psaadm, psaadm) %config(noreplace,) /etc/asl/atomic-scanner.conf
%dir /usr/local/psa/admin/htdocs/atomic-scanner
/usr/local/psa/admin/htdocs/atomic-scanner
/usr/local/psa/admin/htdocs/images/custom_buttons/atomic-scanner-button.gif
/var/asl/bin/atomic-scanner
/var/asl/bin/data-generate.php
/var/asl/data/tortix.sql
/etc/cron.daily/atomic-scanner
%attr(0600,psaadm,psaadm) %config(noreplace) /etc/asl/atomic-scanner.conf


%changelog
* Tue Mar 31 2009 Scott R. Shinn <scott@atomicrocketturtle.com> - 0.3
- Removed encoding for plesk 9 support

* Tue Aug 5 2008 Scott R. Shinn <scott@atomicrocketturtle.com> - 0.2
- added /etc/asl/atomic-scanner.conf

* Tue Jul 14 2008 Scott R. Shinn <scott@atomicrocketturtle.com> - 0.1
- initial alpha release
