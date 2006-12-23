Summary:	ACTOS - Asterisk Configuration Tool Open Source
Summary(pl):	ACTOS - Narzêdzie do konfiguracji Asterisk'a
Name:		actos
Version:	2.1
Release:	0.1
License:	GPLv2
Group:		Applications/Communications
Source0:	http://www.derrier.com/pierre/code/%{name}-%{version}.tar.gz
Patch0:         %{name}-dont_use_X_server.patch
URL:		http://www.derrier.com/pierre/code/
BuildRequires:	python >= 2.3
BuildRequires:	gtk+
BuildRequires:	libglade >= 2.0
BuildRequires:	glib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACTOS is a GUI tool with an intuitive interface for configuring
Asterisk, the Linux Open Source PBX. Asterisk is a very powerful tool,
and that means a bit complex... ACTOS helps the user through the
choice of the options and generate the text configuration files needed
by Asterisk.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
python setup.py clean
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
python setup.py install \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KNOWN_BUGS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
/usr/share/python2.4/site-packages/actos_modules
