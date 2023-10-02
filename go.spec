%global __os_install_post %{nil}
%define debug_package %{nil}
%undefine _missing_build_ids_terminate_build

%define _go_rel 1.21.1
%define _go_patch 0

%if (0%{?suse_version} > 0)
# Sigh. SuSE.
Epoch:		1
Name:		go%{_go_rel}
%else
%if (0%{?rhel} >= 7)
Name:		golang
%else
Name:		go
%endif
%endif
%if (0%{?_go_patch} > 0)
Version:	%{_go_rel}.%{_go_patch}
%else
Version:	%{_go_rel}
%endif
Release:	1.daos%{?dist}
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
%if (0%{?suse_version} > 0)
%{__mkdir_p} %{buildroot}/%{_exec_prefix}/lib64/go/%{_go_rel}
cp -a bin %{buildroot}/%{_exec_prefix}/lib64/go/%{_go_rel}/
cp -a pkg %{buildroot}/%{_exec_prefix}/lib64/go/%{_go_rel}/
cp -a src %{buildroot}/%{_exec_prefix}/lib64/go/%{_go_rel}/
%else
%{__mkdir_p} %{buildroot}/%{_exec_prefix}
cp -a bin %{buildroot}/%{_exec_prefix}
cp -a pkg %{buildroot}/%{_exec_prefix}
cp -a src %{buildroot}/%{_exec_prefix}
%endif

%files
%if (0%{?suse_version} > 0)
%{_exec_prefix}/lib64/go/%{_go_rel}/bin/*
%{_exec_prefix}/lib64/go/%{_go_rel}/pkg/*
%{_exec_prefix}/lib64/go/%{_go_rel}/src/*
%else
%{_bindir}/*
%{_exec_prefix}/pkg/*
%{_exec_prefix}/src/*
%endif

%doc

%if (0%{?suse_version} > 0)
%post
update-alternatives \
  --install /usr/bin/go go /usr/lib64/go/%{version}/bin/go $((20+$(echo %{version} | cut -d. -f2))) \
  --slave /usr/bin/gofmt gofmt /usr/lib64/go/%{version}/bin/gofmt
%postun
if [ $1 -eq 0 ] ; then
	update-alternatives --remove go /usr/lib64/go/%{version}/bin/go
fi
%endif

%changelog
* Wed Oct 02 2023 Lei Huang <lei.huang@intel.com> - 1.21.1-1
- Update to 1.21.1
- Build for EL9

* Thu Apr 13 2023 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.20.3-1
- Update to 1.20.3

* Thu Mar 16 2023 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.20.2-1
- Update to 1.20.2

* Fri Feb 17 2023 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.20.1-1
- Update to 1.20.1

* Fri Feb 03 2023 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.20-1
- Update to 1.20

* Wed Jan 25 2023 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.19.5-1
- Update to 1.19.5

* Tue Nov 01 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.19.3-1
- Update to 1.19.3

* Wed Oct 19 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.19.2-1
- Update to 1.19.2

* Thu Aug 11 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.19-1
- Update to 1.19

* Fri Jun 03 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.18.3-1
- Update to 1.18.3

* Fri May 13 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.18.2-1
- Update to 1.18.2

* Thu May 05 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.18.1-1
- Update to 1.18.1

* Thu Mar 17 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.18-1
- Update to 1.18

* Fri Mar 04 2022 David Quigley <david.quigley@intel.com> - 1.17.8-1
- Bump the patch version to apply fixes for new CVEs

* Thu Feb 17 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.17.7-2
- adjust names per distro

* Fri Feb 11 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.17.7-1
- initial packaging for internal builders
