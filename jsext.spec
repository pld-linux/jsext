#
# Conditional build:
%bcond_without	threads	# thread-safe library (requires nspr)
#
Summary:	JavaScript Implementation
Summary(pl.UTF-8):	Implementacja JavaScriptu
Name:		jsext
Version:	0.12
Release:	1
License:	LGPL or GPL or Mozilla Public License 1.1, part BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/jsext/%{name}-%{version}.tar.gz
# Source0-md5:	9980d5bdcec8d4a2b5455f3264b42184
URL:		http://www.jsext.net/
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.294
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JavaScript Reference Implementation (codename SpiderMonkey). The
package contains JavaScript runtime (compiler, interpreter,
decompiler, garbage collector, atom manager, standard classes) and
small "shell" program that can be used interactively and with .js
files to run scripts. This version extends the interpreter with the
ability to access libraries written in C.

%package devel
Summary:	Header files for JavaScript library
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki JavaScript
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?with_threads:Provides:	js-devel(threads)}
Conflicts:	njs-devel

%description devel
Header files for JavaScript library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki JavaScript.

%package static
Summary:	Static JavaScript library
Summary(pl.UTF-8):	Statyczna biblioteka JavaScript
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
%{?with_threads:Provides:	js-static(threads)}
Conflicts:	njs-static

%description static
Static version of JavaScript library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/js}
%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsext*
%attr(755,root,root) %{_libdir}/libjsext.so.*.*
%dir %{_libdir}/%{name}-%{version}
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*.so


%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libjs.so
#%dir %{_includedir}/js
#%{_includedir}/js/js.msg
#%{_includedir}/js/jsopcode.tbl
#%{_includedir}/js/js[!j]*.h

%files static
%defattr(644,root,root,755)
#%{_libdir}/libjs.a
