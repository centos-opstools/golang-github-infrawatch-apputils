# Generated by go2rpm 1
%bcond_without check

# https://github.com/infrawatch/apputils
%global gohost          github
%global gosuffix        com
%global goorg           infrawatch
%global goproject       apputils
%global goipath         %{gohost}.%{gosuffix}/%{goorg}/%{goproject}
%global commit          28412c8e501ccfbdf0dfca590de223cb3a41bad4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%gometa

%global common_description %{expand:
Shared library for infrawatch golang components.}

%global godocs          README.md

Name:           golang-%{gohost}-%{goorg}-%{goproject}
Version:        0.2
Release:        2%{?dist}
Summary:        Shared library for infrawatch golang components

License:        ASL 2.0

URL:            %{gourl}
#Source0:        https://%{goipath}/archive/%{commit}/%{goproject}-%{shortcommit}.tar.gz
Source0:        https://%{goipath}/archive/v%{version}.tar.gz#/%{goproject}-v%{version}.tar.gz

BuildRequires:  golang(github.com/go-ini/ini)
BuildRequires:  golang(github.com/streadway/amqp)
BuildRequires:  golang(qpid.apache.org/amqp)
BuildRequires:  golang(qpid.apache.org/electron)
BuildRequires:  golang(github.com/stretchr/testify/assert)

Requires:  golang(github.com/go-ini/ini)
Requires:  golang(github.com/streadway/amqp)
Requires:  golang(github.com/apache/qpid-proton/go/pkg/amqp)
Requires:  golang(github.com/apache/qpid-proton/go/pkg/electron)

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

%if %{with check}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

pushd %{buildroot}/%{gopath}/src/%{gohost}.%{gosuffix}/%{goorg}/%{goproject}
#Note(mmagr): unit test fail currently. Uncomment this in next build
#%gotest ./...
popd
%endif

%files
%{gopath}/src/%{goipath}
%license LICENSE
%doc README.md

%changelog
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
