# Generated by go2rpm 1
%bcond_without check

# https://github.com/infrawatch/apputils
%global gohost          github
%global gosuffix        com
%global goorg           infrawatch
%global goproject       apputils
%global goipath         %{gohost}.%{gosuffix}/%{goorg}/%{goproject}
%global commit          2f2621b85fa17b422e76994caf523b5112b3061c
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%gometa

%global common_description %{expand:
Shared library for infrawatch golang components.}

%global godocs          README.md

Name:           golang-%{gohost}-%{goorg}-%{goproject}
Version:        0.7
Release:        1%{?dist}
Summary:        Shared library for infrawatch golang components
License:        ASL 2.0

URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}.tar.gz#/%{goproject}-v%{version}.tar.gz

BuildRequires:  golang(github.com/go-ini/ini)
BuildRequires:  golang(github.com/streadway/amqp)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/Azure/go-amqp)

Requires:  golang(github.com/go-ini/ini)
Requires:  golang(github.com/streadway/amqp)
Requires:  golang(github.com/Azure/go-amqp)

Provides:       golang(%{goipath})

%description
%{common_description}

%gopkg

%prep
%autosetup -n %{goproject}-%{version}

%install
# copy packages
install -d -p %{buildroot}/%{gopath}/src/%{goipath}/
for file in ./* ; do
    if [ -d $file ]; then
        cp -rpav $file %{buildroot}%{gopath}/src/%{goipath}/
    fi
done

%check
#%if %{with check}
#export GOPATH=%{buildroot}/%{gopath}:%{gopath}

#%if ! 0%{?gotest:1}
#%global gotest go test
#%endif

#pushd %{buildroot}/%{gopath}/src/%{gohost}.%{gosuffix}/%{goorg}/%{goproject}
#Note(mmagr): unit test fail currently because of the need for 3rd party services
#%gotest ./...
#popd
#%endif

%files
%{gopath}/src/%{goipath}
%license LICENSE
%doc README.md

%changelog
* Fri May 3 2024 Martin Magr <mmagr@redhat.com> - 0.7-1.git2f2621b
- Refactor of AMQP-1.0 connector (issue #27)
- Fix concurrent deadlock

* Thu Jun 08 2023 Martin Magr <mmagr@redhat.com> - 0.6-1.git0c90918
- Additional reconnect case (rhbz#2158781)
- Don't attempt to close Sender on error (rhbz#2179924)

* Tue Feb 28 2023 Martin Magr <mmagr@redhat.com> - 0.5-1.git4ffa970
- Add interval to duration converter
- Improve AMQP-1.0 transport

* Fri Oct 29 2021 Martin Magr <mmagr@redhat.com> - 0.4-1.git4f0bf95
- Add system.GetOpenedFiles
- Add possibility to get process limits
- Enhance error message returned from Loki
- Explicitly init http client in Loki connector
- Add ability to choose tenant to Loki connector
- Split connector package into separate packages

* Thu Apr 08 2021 Martin Magr <mmagr@redhat.com> - 0.3-1.git482adc4
- Added task scheduler (scheduler module)
- Fixed spawning SensuConnector when not all subscription channels are available
- Added map operations (misc module)

* Thu Feb 25 2021 Martin Magr <mmagr@redhat.com> - 0.2-2.git28412c8
- Update of qpid-proton dependency

* Wed Feb 24 2021 Martin Magr <mmagr@redhat.com> - 0.2-1.git28412c8
- Updated to latest upstream release

* Mon Jan 18 2021 Yatin Karel <ykarel@redhat.com> - 0.1-2.git8439bdc
- Fix License

* Tue Oct 13 2020 Martin Magr <mmagr@redhat.com> - 0.1-1.git8439bdc
- Updated to latest upstream release
- Fixed issue #1

* Wed Sep 02 2020 Martin Magr <mmagr@redhat.com> - 0-0.1.20200810git9a73d9
- Initial package
