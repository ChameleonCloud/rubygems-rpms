# Generated from mixlib-config-2.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-config

Name: rubygem-%{gem_name}
Version: 2.2.1
Release: 1%{?dist}
Summary: A class based configuration library
Group: Development/Languages
License: Apache-2.0
URL: http://www.chef.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
# BuildRequires: rubygem(rspec) => 2.99
# BuildRequires: rubygem(rspec) < 3
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A class based configuration library.



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

rm -f %{buildroot}%{gem_instdir}/Rakefile
rm -rf %{buildroot}%{gem_instdir}/spec/

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NOTICE
%doc %{gem_instdir}/README.md
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Wed Mar 16 2016 Pierre Riteau <priteau@uchicago.edu> - 2.2.1-1
- Initial package
