%global __os_install_post %{nil}
%define debug_package %{nil}
%undefine _missing_build_ids_terminate_build

%define _go_rel_major_minor 1.21
%define _go_rel_bugfix 4
%define _go_rel %{_go_rel_major_minor}.%{_go_rel_bugfix}
%define _go_patch 0

%if (0%{?suse_version} > 0)
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
Release:	2.daos%{?dist}
Summary:	The Go Programming Language

License:	BSD and Public Domain
URL:		http://golang.org/
Source0:	https://go.dev/dl/go%{version}.linux-amd64.tar.gz

%define _fullver %{version}-%{release}

ExclusiveArch: x86_64
AutoReqProv: no

%if (0%{?suse_version} > 0)
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif

%if (0%{?rhel} > 0)
Provides: go = %{_fullver} golang-src = %{_fullver} golang-bin = %{_fullver}
Obsoletes: go < %{_fullver} golang-src < %{_fullver} golang-bin < %{_fullver}
%endif

%if (0%{?suse_version} > 0)
# Emulate the main go package
Provides: go = %{version} go-devel = go%{version} go-devel-static = go%{version} go%{_go_rel_major_minor} = %{_fullver} go%{_go_rel_major_minor}(x86-64) = %{_fullver} golang(API) = %{_go_rel_major_minor}
# Emulate the go-race sub-package
Provides: go-race = %{version} go-%{_go_rel_major_minor}-race = %{_fullver} go-%{_go_rel_major_minor}-race(x86_64) = %{_fullver}
# Emulate the go-doc sub-package
Provides: go-doc = %{version} go%{_go_rel_major_minor}-doc = %{_fullver} go%{_go_rel_major_minor}-doc(x86_64) = %{_fullver}
Obsoletes: go < %{version} go-race < %{version} go-doc < %{_fullver}
%endif

%description
Installs the precompiled Go toolchain provided at https://go.dev/dl/, replacing
any older distro-provided versions.

%prep
%setup -q -n go

%build

%install
%if (0%{?suse_version} > 0)
# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
mkdir -p %{buildroot}%{_bindir}
touch %{buildroot}%{_sysconfdir}/alternatives/{go,gofmt}
ln -sf %{_sysconfdir}/alternatives/go %{buildroot}%{_bindir}/go
ln -sf %{_sysconfdir}/alternatives/gofmt %{buildroot}%{_bindir}/gofmt
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
%{_bindir}/go
%{_bindir}/gofmt
%ghost %{_sysconfdir}/alternatives/go
%ghost %{_sysconfdir}/alternatives/gofmt

%else
%{_bindir}/*
%{_exec_prefix}/pkg/*
%{_exec_prefix}/src/*
%endif

%doc

%if (0%{?suse_version} > 0)
%post
update-alternatives \
  --install %{_bindir}/go go %{_libdir}/go/%{version}/bin/go $((20+$(echo %{version} | cut -d. -f2))) \
  --slave %{_bindir}/gofmt gofmt %{_libdir}/go/%{version}/bin/gofmt
%postun
if [ $1 -eq 0 ] ; then
	update-alternatives --remove go %{_libdir}/go/%{version}/bin/go
fi
%endif

%changelog
* Tue Nov 07 2023 Brian J. Murrell <brian.murrell@intel.com> - 1.21.3-2
- Fix Provides: to use only the major.minor of the go release

* Mon Oct 23 2023 Lei Huang <lei.huang@intel.com> - 1.21.3-1
- Update to 1.21.3
- Build for EL9

* Tue Oct 17 2023 Brian J. Murrell <brian.murrell@intel.com> - 1.20.3-2
- Add Obsoletes: for the EL subpackages

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
