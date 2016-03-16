# Generated from mixlib-shellout-2.2.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-shellout

Name: rubygem-%{gem_name}
Version: 2.2.6
Release: 1%{?dist}
Summary: Run external commands on Unix or Windows
Group: Development/Languages
License: Apache-2.0
URL: http://wiki.opscode.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.9.3
# BuildRequires: rubygem(rspec) => 3.0
# BuildRequires: rubygem(rspec) < 4
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Run external commands on Unix or Windows.



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

rm -f %{buildroot}%{gem_instdir}/Gemfile
rm -f %{buildroot}%{gem_instdir}/Rakefile
rm -f %{buildroot}%{gem_instdir}/mixlib-shellout-windows.gemspec
rm -f %{buildroot}%{gem_instdir}/mixlib-shellout.gemspec

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Wed Mar 16 2016 Pierre Riteau <priteau@uchicago.edu> - 2.2.6-1
- Initial package
