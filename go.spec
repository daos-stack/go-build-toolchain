%global __os_install_post %{nil}
%define debug_package %{nil}
%undefine _missing_build_ids_terminate_build

%define _go_rel 1.17
%define _go_patch 7

Name:		go
Version:	%{_go_rel}.%{_go_patch}
Release:	1.daos%{?dist}
Summary:	The Go Programming Language.

License:	BSD and Public Domain
URL:		http://golang.org/
Source0:	https://go.dev/dl/go%{version}.linux-amd64.tar.gz

%define _fullver %{version}-%{release}

ExclusiveArch: x86_64
AutoReqProv: no

# el7/8
Provides: golang-%{_fullver} = %{version} golang-src-%{_fullver} = %{version}  golang-bin-%{_fullver}  = %{version}
Obsoletes: golang <= %{version} golang-src <= %{version} golang-bin <= %{version}
# sles/leap
Provides: go%{_go_rel} = %{version} go%{_go_rel}-race = %{version} go%{_go_rel}-doc = %{version}
Provides: go-race-%{_fullver} = %{version} go-doc-%{_fullver} = %{version}
Obsoletes: go-race < %{version} go-doc < %{version}
Obsoletes: go%{_go_rel} <= %{version} go%{_go_rel}-race <= %{version} go%{_go_rel}-doc <= %{version}
Obsoletes: go1.16 < %{version} go1.16-race < %{version} go1.16-doc < %{version}
Obsoletes: go1.15 < %{version} go1.15-race < %{version} go1.15-doc < %{version}
Obsoletes: go1.14 < %{version} go1.14-race < %{version} go1.14-doc < %{version}
Obsoletes: go1.13 < %{version} go1.13-race < %{version} go1.13-doc < %{version}
Obsoletes: go1.12 < %{version} go1.12-race < %{version} go1.12-doc < %{version}
Obsoletes: go1.11 < %{version} go1.11-race < %{version} go1.11-doc < %{version}
Obsoletes: go1.10 < %{version} go1.10-race < %{version} go1.10-doc < %{version}

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
* Fri Feb 11 2022 Michael J. MacDonald <mjmac.macdonald@intel.com>
- initial packaging for internal builders
