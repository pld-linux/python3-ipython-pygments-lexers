Summary:	A Pygments plugin for IPython code & console sessions
Summary(pl.UTF-8):	Wtyczka Pygments dla kodu IPythona i sesji konsoli
Name:		python3-ipython-pygments-lexers
Version:	1.1.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ipython-pygments-lexers/
Source0:	https://files.pythonhosted.org/packages/source/i/ipython_pygments_lexers/ipython_pygments_lexers-%{version}.tar.gz
# Source0-md5:	a8d51d899ed01e1cb6773657cf88f734
URL:		https://ipython.org/
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-build
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Pygments plugin for IPython code & console sessions.

%description -l pl.UTF-8
Wtyczka Pygments dla kodu IPythona i sesji konsoli.

%prep
%setup -q -n ipython_pygments_lexers-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/ipython_pygments_lexers.py
%{py3_sitescriptdir}/__pycache__/ipython_pygments_lexers.cpython-*.py[co]
%{py3_sitescriptdir}/ipython_pygments_lexers-%{version}.dist-info
