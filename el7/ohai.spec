# Generated from ohai-6.24.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ohai

Name: rubygem-%{gem_name}
Version: 6.24.2
Release: 1%{?dist}
Summary: Ohai profiles your system and emits JSON
Group: Development/Languages
License: Apache-2.0
URL: http://wiki.opscode.com/display/chef/Ohai
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(systemu) => 2.6.4
Requires: rubygem(systemu) < 2.7
Requires: rubygem(yajl-ruby) 
Requires: rubygem(mixlib-cli) 
Requires: rubygem(mixlib-config) 
Requires: rubygem(mixlib-log) 
Requires: rubygem(mixlib-shellout) 
Requires: rubygem(ipaddress) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
# BuildRequires: rubygem(rspec-core) => 2.14
# BuildRequires: rubygem(rspec-core) < 3
# BuildRequires: rubygem(rspec-expectations) => 2.14
# BuildRequires: rubygem(rspec-expectations) < 3
# BuildRequires: rubygem(rspec-mocks) => 2.14
# BuildRequires: rubygem(rspec-mocks) < 3
# BuildRequires: rubygem(rspec_junit_formatter) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ohai profiles your system and emits JSON.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}
cp -a ./docs/man/* \
        %{buildroot}%{_mandir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/ohai
%{gem_instdir}/bin
%{gem_instdir}/Rakefile
%{gem_instdir}/docs/man/man1/ohai.1
%{gem_instdir}/LICENSE
%{gem_instdir}/README.rdoc
%{gem_instdir}/spec
%{gem_libdir}
%{_mandir}/man1/ohai.1.gz
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Mar 16 2016 Pierre Riteau <priteau@uchicago.edu> - 6.24.2-1
- Initial package
