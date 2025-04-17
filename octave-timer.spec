%global octpkg timer

Summary:	A Matlab-compatible timer class to execute periodic actions
Name:		octave-timer
Version:	0.1.2
Release:	1
License:	GPLv2+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/timer/
Url:		https://gitlab.com/farhi/octave-timer/
Source0:	https://gitlab.com/farhi/octave-timer/-/archive/%{version}/octave-timer-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
A Matlab-compatible timer class to execute periodic actions.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

