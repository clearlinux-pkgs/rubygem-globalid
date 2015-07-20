#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-globalid
Version  : 0.3.5
Release  : 1
URL      : https://rubygems.org/downloads/globalid-0.3.5.gem
Source0  : https://rubygems.org/downloads/globalid-0.3.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
No detailed description available

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n globalid-0.3.5
gem spec %{SOURCE0} -l --ruby > rubygem-globalid.gemspec

%build
gem build rubygem-globalid.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
globalid-0.3.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/globalid-0.3.5.gem
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Identification/cdesc-Identification.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Identification/to_gid-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Identification/to_gid_param-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Identification/to_global_id-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Identification/to_sgid-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Identification/to_sgid_param-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Identification/to_signed_global_id-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/ActiveRecordFinder/cdesc-ActiveRecordFinder.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/ActiveRecordFinder/locate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/BlockLocator/cdesc-BlockLocator.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/BlockLocator/locate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/BlockLocator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/cdesc-Locator.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/find_allowed%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/find_records-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/locate-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/locate_many-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/locate_many_signed-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/locate_signed-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/locator_for-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/normalize_app-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/parse_allowed-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Locator/use-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Railtie/ActiveSupport/cdesc-ActiveSupport.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/Railtie/cdesc-Railtie.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/app%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/app-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/cdesc-GlobalID.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/create-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/find-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/find-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/model_class-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/parse-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/parse_encoded_gid-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/repad_gid-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/to_param-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/GlobalID/uri-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/ExpiredMessage/cdesc-ExpiredMessage.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/cdesc-SignedGlobalID.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/encoded_expiration-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/expires_at-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/expires_in-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/parse-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/pick_expiration-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/pick_purpose-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/pick_verifier-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/purpose-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/raise_if_expired-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/to_h-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/to_param-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/verifier-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/verifier-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/SignedGlobalID/verify-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/build-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/cdesc-GID.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/check_host-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/check_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/check_scheme-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/create-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/model_id-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/model_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/parse-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/parse_query_params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/query%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/set_model_components-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/set_params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/set_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/set_query-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/validate_app-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/GID/validate_component-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/URI/cdesc-URI.ri
/usr/lib64/ruby/gems/2.2.0/doc/globalid-0.3.5/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/globalid-0.3.5/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/globalid-0.3.5/lib/global_id.rb
/usr/lib64/ruby/gems/2.2.0/gems/globalid-0.3.5/lib/global_id/global_id.rb
/usr/lib64/ruby/gems/2.2.0/gems/globalid-0.3.5/lib/global_id/identification.rb
/usr/lib64/ruby/gems/2.2.0/gems/globalid-0.3.5/lib/global_id/locator.rb
/usr/lib64/ruby/gems/2.2.0/gems/globalid-0.3.5/lib/global_id/railtie.rb
/usr/lib64/ruby/gems/2.2.0/gems/globalid-0.3.5/lib/global_id/signed_global_id.rb
/usr/lib64/ruby/gems/2.2.0/gems/globalid-0.3.5/lib/global_id/uri/gid.rb
/usr/lib64/ruby/gems/2.2.0/gems/globalid-0.3.5/lib/globalid.rb
/usr/lib64/ruby/gems/2.2.0/specifications/globalid-0.3.5.gemspec
