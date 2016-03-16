# Generated from popen4-0.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name popen4

Name: rubygem-%{gem_name}
Version: 0.1.2
Release: 1%{?dist}
Summary: Open4 cross-platform
Group: Development/Languages
License: Ruby
URL: http://github.com/shairontoledo/popen4
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(Platform) >= 0.4.0
Requires: rubygem(open4) >= 0.4.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
POpen4 provides the Rubyist a single API across platforms for executing a
command in a child process with handles on stdout, stderr, stdin streams as
well as access to the process ID and exit status.



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
rm -rf %{buildroot}%{gem_instdir}/tests

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Wed Mar 16 2016 Pierre Riteau <priteau@uchicago.edu> - 0.1.2-1
- Initial package
