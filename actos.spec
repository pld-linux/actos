Summary:	ACTOS - Asterisk Configuration Tool Open Source
Summary(pl.UTF-8):   ACTOS - Narzędzie do konfiguracji Asteriska
Name:		actos
Version:	2.25
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.derrier.com/pierre/code/%{name}-%{version}.tar.gz
# Source0-md5:	c449a769bc527210f7dae98cef5b1666
URL:		http://www.derrier.com/pierre/code/actos.html
BuildRequires:	python >= 1:2.3
BuildRequires:	python-pygtk-glade >= 2.0
BuildRequires:	python-pygtk-gtk >= 2.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACTOS is a GUI tool with an intuitive interface for configuring
Asterisk, the Linux Open Source PBX. Asterisk is a very powerful tool,
and that means a bit complex... ACTOS helps the user through the
choice of the options and generate the text configuration files needed
by Asterisk.

%description -l pl.UTF-8
ACTOS to graficzne narzędzie z intuicyjnym interfejsem do
konfigurowania Asteriska - linuksowej centralki telefonicznej (PBX) o
otwartych źródłach. Asterisk jest bardzo potężnym narzędziem, a przy
tym dość złożonym... ACTOS pomaga użytkownikowi w wyborze opcji i
wygenerowaniu tekstowych plików konfiguracyjnych wymaganych przez
Asteriska.

%prep
%setup -q -n %{name}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root $RPM_BUILD_ROOT

%py_postclean

mv -f $RPM_BUILD_ROOT%{_bindir}/{actos.py,actos}
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,CHANGELOG,COPYING,INSTALL,KNOWN_BUGS,README,TODO}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG KNOWN_BUGS README TODO
%attr(755,root,root) %{_bindir}/actos
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.def
%{_datadir}/%{name}/actos.conf
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/en.help
%lang(fr) %{_datadir}/%{name}/fr.help
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/actos_en.glade
%lang(fr) %{_datadir}/%{name}/glade/actos_fr.glade
%{py_sitescriptdir}/actos_modules
