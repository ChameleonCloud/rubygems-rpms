# Generated from Platform-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name Platform

Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Summary: Hopefully robust platform sensing
Group: Development/Languages
License: MIT
URL: http://rubyforge.org/projects/platform/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Hopefully robust platform sensing.



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




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_docdir}
%doc %{gem_instdir}/README
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Wed Mar 16 2016 Pierre Riteau <priteau@uchicago.edu> - 0.4.0-1
- Initial package
