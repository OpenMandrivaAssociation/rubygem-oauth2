%define rbname oauth2

Summary:	A Ruby wrapper for the OAuth 2.0 protocol
Name:		rubygem-%{rbname}
Version:	1.0.0
Release:	2
License:	MIT
Group:		Development/Ruby
Url:		https://rubygems.org/gems/%{rbname}
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
A Ruby wrapper for the OAuth 2.0 protocol built with a similar style to the
original OAuth gem.

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}/
%{gem_dir}/gems/%{rbname}-%{version}/lib/
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
Conflicts:	%{name} < 1.0.0

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{gem_dir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

