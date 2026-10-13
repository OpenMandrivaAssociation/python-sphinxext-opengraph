Name:		python-sphinxext-opengraph
Version:	0.13.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxext-opengraph/sphinxext_opengraph-%{version}.tar.gz
Summary:	Sphinx Extension to enable OGP support
URL:		https://pypi.org/project/sphinxext-opengraph/
License:	BSD-3-Clause
Group:		Development/Python

BuildRequires:	python
BuildRequires:  python%{pyver}dist(sphinx)
BuildRequires:  python%{pyver}dist(matplotlib)

BuildSystem:	python
BuildArch:	noarch

Requires:   python%{pyver}dist(sphinx)
Requires:   python%{pyver}dist(sphinx-design)
Requires:   python%{pyver}dist(furo)

%description
Sphinx Extension to enable OGP support

%files
%{py_sitedir}/sphinxext/opengraph
%{py_sitedir}/sphinxext_opengraph-*.*-info
