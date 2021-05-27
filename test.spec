Name: test
Version: 1
Release: 1%{?dist}
Summary: Test
License: Public Domain
URL: https://github.com/junaruga/report-build-env-dns
BuildRequires: %{?_root_bindir}%{!?_root_bindir:%{_bindir}}/nslookup

%description

%prep
nslookup rubygems.org

cat > test <<EOF
#!/bin/bash
echo "test"
EOF

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 test %{buildroot}/%{_bindir}/test

%files
%{_bindir}/test

%changelog
* Thu May 27 2021 Jun Aruga <jaruga@redhat.com> - 1-1
- Init.
