%global __os_install_post %{nil}
%define debug_package %{nil}
%undefine _missing_build_ids_terminate_build

%define _go_rel 1.17
%define _go_patch 7

%if (0%{?suse_version} > 0)
Name:		go%{_go_rel}
%else
%if (0%{?rhel} >= 7)
Name:		golang
%else
Name:		go
%endif
%endif
Version:	%{_go_rel}.%{_go_patch}
Release:	2.daos%{?dist}
Summary:	The Go Programming Language

License:	BSD and Public Domain
URL:		http://golang.org/
Source0:	https://go.dev/dl/go%{version}.linux-amd64.tar.gz

%define _fullver %{version}-%{release}

ExclusiveArch: x86_64
AutoReqProv: no

%if (0%{?rhel} > 0)
Provides: go = %{_fullver} golang-src = %{_fullver} golang-bin = %{_fullver}
%endif

%if (0%{?suse_version} > 0)
Provides: go%{_go_rel} = %{_fullver} go%{_go_rel}-race = %{_fullver} go%{_go_rel}-doc = %{_fullver}
Provides: go = %{_fullver} go-race = %{_fullver} go-doc = %{_fullver}
%endif
Obsoletes: go < %{_fullver}

%description
Installs the precompiled Go toolchain provided at https://go.dev/dl/, replacing
any older distro-provided versions.

%prep
%setup -q -n go

%build

%install
%{__mkdir_p} %{buildroot}/%{_exec_prefix}
cp -a bin %{buildroot}/%{_exec_prefix}
cp -a pkg %{buildroot}/%{_exec_prefix}
cp -a src %{buildroot}/%{_exec_prefix}

%files
%{_bindir}/*
%{_exec_prefix}/pkg/*
%{_exec_prefix}/src/*
%doc

%changelog
* Thu Feb 17 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.17.7-2
- adjust names per distro

* Fri Feb 11 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.17.7-1
- initial packaging for internal builders
