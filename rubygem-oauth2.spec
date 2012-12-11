%define oname oauth2

Name:       rubygem-%{oname}
Version:    0.0.13
Release:    %mkrel 1
Summary:    A Ruby wrapper for the OAuth 2.0 protocol
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/intridea/oauth2
Source0:    %{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(faraday) >= 0.4.1
Requires:   rubygem(multi_json) >= 0.0.4
Requires:   rubygem(rspec)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A Ruby wrapper for the OAuth 2.0 protocol built with a similar style to the
original OAuth gem.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.document
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/specs.watchr
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGELOG.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 0.0.13-1mdv2011.0
+ Revision: 623512
- import rubygem-oauth2

