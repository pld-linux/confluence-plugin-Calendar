# NOTE:
# - Please, do not send it to builders. It depends on confluence which is not
#   distributable.

%include	/usr/lib/rpm/macros.java

%define		confluence_libdir	%{_datadir}/confluence/WEB-INF/lib
%define		srcname			calendar-plugin

Summary:	Calendar plugin for Confluence
Name:		confluence-plugin-Calendar
Version:	2.7.2
Release:	0.1
License:	BSD
Group:		Development/Languages/Java
Source0:	http://svn.atlassian.com/svn/public/contrib/confluence/calendar-plugin/jars/%{srcname}-%{version}.jar
# Source0-md5:	16a8b34a2b805143058ce4169cfa1924
URL:		http://www.adaptavist.com/display/Builder/Home
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-ical4j
Requires:	java-randombits-source
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calendar plugin for Confluence.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{confluence_libdir}

install %{SOURCE0} $RPM_BUILD_ROOT%{confluence_libdir}/%{srcname}-%{version}.jar
ln -s %{_javadir}/ical4j.jar $RPM_BUILD_ROOT%{confluence_libdir}/ical4j.jar
ln -s %{_javadir}/randombits-source.jar $RPM_BUILD_ROOT%{confluence_libdir}/randombits-source.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{confluence_libdir}/%{srcname}-%{version}.jar
%{confluence_libdir}/ical4j.jar
%{confluence_libdir}/randombits-source.jar
