# Generated from yajl-ruby-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name yajl-ruby

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 1%{?dist}
Summary: Ruby C bindings to the excellent Yajl JSON stream-based parser library
Group: Development/Languages
License: MIT
URL: http://github.com/brianmario/yajl-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel >= 1.8.6
# BuildRequires: rubygem(rake-compiler) >= 0.7.5
# BuildRequires: rubygem(rspec) => 2.14
# BuildRequires: rubygem(rspec) < 3
# BuildRequires: rubygem(activesupport) => 3.1.2
# BuildRequires: rubygem(activesupport) < 3.2
# BuildRequires: rubygem(json) 
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby C bindings to the excellent Yajl JSON stream-based parser library.



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

mkdir -p %{buildroot}%{gem_extdir_mri}/lib
# TODO: move the extensions
#mv %{buildroot}%{gem_instdir}/lib/shared_object.so %{buildroot}%{gem_extdir_mri}/lib/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.rspec
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -f %{buildroot}%{gem_instdir}/Gemfile
rm -f %{buildroot}%{gem_instdir}/Rakefile
rm -f %{buildroot}%{gem_instdir}/yajl-ruby.gemspec
rm -rf %{buildroot}%{gem_instdir}/benchmark
rm -rf %{buildroot}%{gem_instdir}/script
rm -rf %{buildroot}%{gem_instdir}/spec
rm -rf %{buildroot}%{gem_instdir}/tasks


# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/examples

%exclude %{gem_cache}
%{gem_spec}

%changelog
* Wed Mar 16 2016 Pierre Riteau <priteau@uchicago.edu> - 1.2.1-1
- Initial package
