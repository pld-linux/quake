Summary:	Quake for Linux
Summary(pl):	Quake dla Linuksa
Name:		quake
Version:	1.06
Release:	2
Vendor:		id Software
License:	GPL except .pak file
Group:		Applications/Games
Source0:	ftp://ftp.idsoftware.com/idstuff/source/q1source.zip
# Source0-md5:	70a802bd815a61a99e6c1c9a4eaeb0f2
Source1:	ftp://ftp.idsoftware.com/idstuff/quake/%{name}106.zip
# Source1-md5:	8cee4d03ee092909fdb6a4f84f0c1357
Source2:	%{name}.png
Source3:	%{name}-gl.desktop
Source4:	%{name}-x11.desktop
Source5:	%{name}-svga.desktop
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-makefileQW.patch
Patch2:		%{name}-QWGL.patch
Patch3:		%{name}-QWGLmouse.patch
Patch4:		%{name}-GL.patch
Patch5:		%{name}-basedir.patch
Patch6:		%{name}-localdir.patch
Patch7:		%{name}-nosound.patch
URL:		http://www.idsoftware.com/
BuildRequires:	OpenGL-devel
BuildRequires:	lha
BuildRequires:	svgalib-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
"The most important PC game ever."

%description -l pl
"Najwa¿niejsza gra wszechczasów na PC."

%package common
Summary:	Quake for Linux - common files
Summary(pl):	Quake dla Linuksa - pliki wspólne
License:	GPL
Group:		Applications/Games

%description common
"The most important PC game ever" - common files.

%description common -l pl
"Najwa¿niejsza gra wszechczasów na PC" - pliki wspólne.

%package svga
Summary:	Quake for Linux - svgalib version
Summary(pl):	Quake dla Linuksa - wersja korzystaj±ca z svgalib
License:	GPL
Group:		Applications/Games
Requires:	quake-common

%description svga
"The most important PC game ever" - PC ZONE SVGA client.

%description svga -l pl
"Najwa¿niejsza gra wszechczasów na PC" - klient PC ZONE dla SVGA.

%package X11
Summary:	Quake for Linux - X11
Summary(pl):	Quake dla Linuksa - X11
License:	GPL
Group:		Applications/Games
Requires:	quake-common

%description X11
"The most important PC game ever" - PC ZONE X11 client.

%description X11 -l pl
"Najwa¿niejsza gra wszechczasów na PC" - klient PC ZONE dla X11.

%package GL
Summary:	Quake for Linux - GL
Summary(pl):	Quake dla Linuksa - GL
License:	GPL
Group:		Applications/Games
Requires:	OpenGL
Requires:	quake-common

%description GL
"The most important PC game ever" - PC ZONE GL client.

%description GL -l pl
"Najwa¿niejsza gra wszechczasów na PC" - klient PC ZONE dla GL.

%package PAK
Summary:	Quake for Linux - shareware episode
Summary(pl):	Quake dla Linuksa - epizod shareware
License:	non-commercial
Group:		Applications/Games
Requires:	quake-common

%description PAK
"The most important PC game ever" - PC ZONE PAK files containing one
shareware episode.

%description PAK -l pl
"Najwa¿niejsza gra wszechczasów na PC" - pliki PC ZONE PAK,
zawieraj±ce 1 epizod shareware.

%prep
%setup -q -c -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
cp WinQuake/Makefile.linuxi386 WinQuake/Makefile
%{__make} -C WinQuake MOUNT_DIR=`pwd`/WinQuake EGCS=gcc GLIBC=.glibc
cp QW/Makefile.Linux QW/Makefile
%{__make} -C QW MAINDIR=`pwd`/QW
lha -ef resource.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/quake/id1,%{_pixmapsdir},%{_applnkdir}/Games/FPP}

install WinQuake/debugi386.glibc/bin/* $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} %{SOURCE4} %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Games/FPP

install QW/debugi386.glibc/qwcl $RPM_BUILD_ROOT%{_bindir}
install QW/debugi386.glibc/qwcl.x11 $RPM_BUILD_ROOT%{_bindir}
install QW/debugi386.glibc/qwsv $RPM_BUILD_ROOT%{_bindir}
install QW/debugi386.glibc/glqwcl.glx $RPM_BUILD_ROOT%{_bindir}

install id1/* $RPM_BUILD_ROOT%{_datadir}/quake/id1

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc WinQuake/docs/INSTALL WinQuake/docs/INSTALL.Quake WinQuake/docs/README QW/docs/qwcl-readme.txt QW/docs/readme*
%attr(755,root,root) %{_bindir}/qwsv
%{_pixmapsdir}/*

%files svga
%defattr(644,root,root,755)
%doc WinQuake/docs/readme.squake
%attr(755,root,root) %{_bindir}/squake
%attr(755,root,root) %{_bindir}/qwcl
%{_applnkdir}/Games/FPP/quake-svga.desktop

%files X11
%defattr(644,root,root,755)
%doc WinQuake/docs/README.X11
%attr(755,root,root) %{_bindir}/quake.x11
%attr(755,root,root) %{_bindir}/qwcl.x11
%{_applnkdir}/Games/FPP/quake-x11.desktop

%files GL
%defattr(644,root,root,755)
%doc WinQuake/docs/readme.glquake QW/docs/glqwcl-readme.txt
%attr(755,root,root) %{_bindir}/glquake.glx
%attr(755,root,root) %{_bindir}/glqwcl.glx
%{_applnkdir}/Games/FPP/quake-gl.desktop

%files PAK
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/quake
