# Run tests in check section
%bcond_without check

%global goipath         github.com/tambet/go-asana
%global commit          6c0cb7090a14aaf5861c43a10e6db9d32c1fe555

%global common_description %{expand:
Golang library for accessing the Asana API.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Golang library for accessing the Asana API
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/google/go-querystring/query)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git6c0cb70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420git6c0cb70
- First package for Fedora

