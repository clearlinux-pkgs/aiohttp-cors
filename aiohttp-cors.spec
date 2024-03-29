#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aiohttp-cors
Version  : 0.7.0
Release  : 29
URL      : https://files.pythonhosted.org/packages/44/9e/6cdce7c3f346d8fd487adf68761728ad8cd5fbc296a7b07b92518350d31f/aiohttp-cors-0.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/9e/6cdce7c3f346d8fd487adf68761728ad8cd5fbc296a7b07b92518350d31f/aiohttp-cors-0.7.0.tar.gz
Summary  : CORS support for aiohttp
Group    : Development/Tools
License  : Apache-2.0
Requires: aiohttp-cors-license = %{version}-%{release}
Requires: aiohttp-cors-python = %{version}-%{release}
Requires: aiohttp-cors-python3 = %{version}-%{release}
Requires: aiohttp
BuildRequires : aiohttp
BuildRequires : buildreq-distutils3
BuildRequires : pytest-runner
BuildRequires : setuptools

%description
CORS support for aiohttp
        ========================
        
        ``aiohttp_cors`` library implements
        `Cross Origin Resource Sharing (CORS) <cors_>`__
        support for `aiohttp <aiohttp_>`__
        asyncio-powered asynchronous HTTP server.
        
        Jump directly to `Usage`_ part to see how to use ``aiohttp_cors``.
        
        Same-origin policy
        ==================
        
        Web security model is tightly connected to
        `Same-origin policy (SOP) <sop_>`__.

%package license
Summary: license components for the aiohttp-cors package.
Group: Default

%description license
license components for the aiohttp-cors package.


%package python
Summary: python components for the aiohttp-cors package.
Group: Default
Requires: aiohttp-cors-python3 = %{version}-%{release}

%description python
python components for the aiohttp-cors package.


%package python3
Summary: python3 components for the aiohttp-cors package.
Group: Default
Requires: python3-core
Provides: pypi(aiohttp_cors)
Requires: pypi(aiohttp)

%description python3
python3 components for the aiohttp-cors package.


%prep
%setup -q -n aiohttp-cors-0.7.0
cd %{_builddir}/aiohttp-cors-0.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635701780
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aiohttp-cors
cp %{_builddir}/aiohttp-cors-0.7.0/LICENSE %{buildroot}/usr/share/package-licenses/aiohttp-cors/25d1ec1e682bcde600e2e1e0a043ea705de7f30d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aiohttp-cors/25d1ec1e682bcde600e2e1e0a043ea705de7f30d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
