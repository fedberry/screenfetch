Name:           screenfetch
Version:        3.6.2
Release:        7.20140914gitdec1cd6c%{?dist}
Summary:        A "Bash Screenshot Information Tool"

%global commit dec1cd6c2471defe4459967fbc8ae15b55714338

License:        GPLv3+
URL:            https://github.com/KittyKatt/screenFetch
Source0:        https://github.com/KittyKatt/screenFetch/archive/%{commit}/screenFetch-%{commit}.tar.gz

BuildArch:      noarch


%description
This handy Bash script can be used to generate one of 
those nifty terminal theme information + ASCII distribution
logos you see in everyone's screen-shots nowadays. It will 
auto-detect your distribution and display an ASCII version
of that distribution's logo and some valuable information 
to the right. There are options to specify no ASCII art, 
colors, taking a screen-shot upon displaying info, and even 
customizing the screen-shot command! This script is very easy 
to add to and can easily be extended.

%prep
%setup -qn screenFetch-%{commit}

%build
#Nothing to build

%install
install -m 755 -p -D screenfetch-dev %{buildroot}%{_bindir}/screenfetch
install -m 644 -p -D screenfetch.1 %{buildroot}%{_mandir}/man1/screenfetch.1


%files
%doc CHANGELOG COPYING README.mkdn TODO
%{_bindir}/screenfetch
%{_mandir}/man1/screenfetch.1*

%changelog
* Wed Sep 24 2014 Martín Buenahora <zironid@fedoraproject.org> - 3.6.2-7.20140914gitdec1cd6c
- Deleted dot tag from manpage location (not nedded)

* Wed Sep 24 2014 Martín Buenahora <zironid@fedoraproject.org> - 3.6.2-6.20140914gitdec1cd6c
- Changed manpage on files, to prevent crashes in the future if uncompressed manpages are used

* Mon Sep 15 2014 Martín Buenahora <zironid@fedoraproject.org> - 3.6.2-5.20140914gitdec1cd6c
- Removed mkdir from install
- Added -p -D flags to install command
- Recovered old changelog entries
- Changed Release tag to <release>.<date>git<git short commit>

* Sat Sep 13 2014 Martín Buenahora <zironid@fedoraproject.org> - 3.6.2-4.20140914gitdec1cd6c
- Changed summary to: A "Bash Screenshot Information Tool".
- Added doc tag in front of man page location
- Changed from capital to minuscule the f on the name

* Tue Sep 09 2014 Martin Buenahora <zironid@fedoraproject.org> - 3.6.2-3.20140914gitdec1cd6c
- Deleted the line rm -rf {buildroot} from install section (not needed)

* Tue May 20 2014 Martin Buenahora <zironid@fedoraproject.org> - 3.6.2-2.20140914gitdec1cd6c
- Installed the screenfetch-dev file as screenfetch
- Deleted clean section
- Deleted bash as depedency

* Mon May 19 2014 Martin Buenahora <zironid@fedoraproject.org> - 3.6.2-1.20140914gitdec1cd6c
- Initial version of the package
