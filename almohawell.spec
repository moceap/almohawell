%global almohawelllib %{_prefix}/lib/Almohawell
%global owner moceap
%global commit #Write commit here

Name:				almohawell
Version:			9.3.2
Release:			3%{?dist}
License:			GPLv2+
Summary:			Linux Packages Installer and Convertor
Summary(ar):		حوّل و ثبّت أنواعًا مُتعددة من الحُزم
Source:				https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Requires:			perl
Requires:			dpkg
Requires:			debhelper
Requires:			rpm-build
BuildArch:          noarch
URL:				http://almohawell.sf.net

%description
Almohawell is a tool to install any type of Linux
packages on any distro, and can convert between
them. Almohawell support Rpm,Deb,Tgz and others.

%description -l ar
يُعدّ المحوّل كأداة لتثبيت أي نوع من حزم لينُكس على
أي توزيعة، كما يمكنه التّحويل بين تلك الحزم.يدعم
المحوّل الحزم الرّدهاتية والدّيبيانية والسّلاكويرية و
غيرها.

%prep
%setup -qn %{name}

%build
#nothing to build

%install
make install DESTDIR=%{buildroot}

%files
%doc README
%license LICENSE gpl-2.0.txt
%{_bindir}/almohawell
%{almohawelllib}/Almohawell/Package/*.pm
%{almohawelllib}/Almohawell/Package.pm

%changelog
* Sat Jul 11 2015 Mosaab Alzoubi <moceap@hotmail.com> - 9.3.2-3
- Separate requires
- Add #Nothing to build note
- Fix lib dir x86_64 detecting
- Add %%license
- New source in Github
- Update %%description
- Update Summary

* Fri Oct 18 2013 Mosaab Alzoubi <moceap@hotmail.com> - 9.3.2-2
- To zero warnings by rpmlint.

* Thu Oct 17 2013 Mosaab Alzoubi <moceap@hotmail.com> - 9.3.2-1
- Fix legal line.

* Tue Oct 8 2013 Mosaab Alzoubi <moceap@hotmail.com> - 9.3.1-3
- Hosted at Ojuba project.

* Mon Oct 7 2013 Mosaab Alzoubi <moceap@hotmail.com> - 9.3.1-2
- Release line fixed.

* Mon Oct 7 2013 Mosaab Alzoubi <moceap@hotmail.com> - 9.3.1-1
- Full revision to be compatible with Fedora rules.

* Sun Mar 31 2013 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 9.3-1
- update.

* Sun Feb 03 2013 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 9.1-1
- fix perl path.

* Wed Dec 19 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 9.0-1
- Initial Release.
