Summary:	Quake for Linux
Summary(pl):	Quake dla Linuksa
Name:		quake
Version:	1.06
Release:	1
Vendor:		id Software
URL:		http://www.idsoftware.com/
Source0:	ftp://ftp.idsoftware.com/idstuff/source/q1source.zip
Source1:	ftp://ftp.idsoftware.com/idstuff/quake/%{name}106.zip
Source2:	%{name}.png
Source3:	%{name}-gl.desktop
Source4:	%{name}-x11.desktop
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-makefileQW.patch
Patch2:		%{name}-QWGL.patch
Patch3:		%{name}-QWGLmouse.patch
Patch4:		%{name}-GL.patch
Patch5:		%{name}-basedir.patch
Group:		Applications/Games
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	XFree86-OpenGL-devel
BuildRequires:	XFree86-driver-nvidia
BuildRequires:	lha
BuildRequires:	svgalib-devel

%description
"The most important PC game ever" - PC ZONE SVGA client.

%description -l pl
"Najwa¿niejsza gra wszechczasów na PC" - klient PC ZONE dla SVGA.

%package X11
Summary:	Quake for Linux - X11
Summary(pl):	Quake dla Linuksa - X11
Group:		Applications/Games
Requires:	quake

%description X11
"The most important PC game ever" - PC ZONE X11 client.

%description X11 -l pl
"Najwa¿niejsza gra wszechczasów na PC" - klient PC ZONE dla X11.

%package GL
Summary:	Quake for Linux - GL
Summary(pl):	Quake dla Linuksa - GL
Group:		Applications/Games
Requires:	quake

%description GL
"The most important PC game ever" - PC ZONE GL client.

%description GL -l pl
"Najwa¿niejsza gra wszechczasów na PC" - klient PC ZONE dla GL.

%package PAK
Summary:	Quake for Linux - shareware episode
Summary(pl):	Quake dla Linuksa - epizod shareware
Group:		Applications/Games
License:	non-commercial
Requires:	quake

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

%build
cp WinQuake/Makefile.linuxi386 WinQuake/Makefile
%{__make} -C WinQuake MOUNT_DIR=`pwd`/WinQuake EGCS=gcc GLIBC=.glibc
cp QW/Makefile.Linux QW/Makefile
%{__make} -C QW MAINDIR=`pwd`/QW
lha -ef resource.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/quake/id1,%{_pixmapsdir},%{_applnkdir}/Games/Arcade}

install WinQuake/debugi386.glibc/bin/* $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

install QW/debugi386.glibc/qwcl $RPM_BUILD_ROOT%{_bindir}
install QW/debugi386.glibc/qwcl.x11 $RPM_BUILD_ROOT%{_bindir}
install QW/debugi386.glibc/qwsv $RPM_BUILD_ROOT%{_bindir}
install QW/debugi386.glibc/glqwcl.glx $RPM_BUILD_ROOT%{_bindir}

install id1/* $RPM_BUILD_ROOT%{_datadir}/quake/id1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/squake
%attr(755,root,root) %{_bindir}/qwcl
%attr(755,root,root) %{_bindir}/qwsv
%doc WinQuake/docs/INSTALL WinQuake/docs/INSTALL.Quake WinQuake/docs/README WinQuake/docs/readme.squake QW/docs/qwcl-readme.txt QW/docs/readme*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake.x11
%attr(755,root,root) %{_bindir}/qwcl.x11
%{_pixmapsdir}/*
%{_applnkdir}/Games/Arcade/quake-x11.desktop
%doc WinQuake/docs/README.X11

%files GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glquake.glx
%attr(755,root,root) %{_bindir}/glqwcl.glx
%{_pixmapsdir}/*
%{_applnkdir}/Games/Arcade/quake-gl.desktop
%doc WinQuake/docs/readme.glquake QW/docs/glqwcl-readme.txt

%files PAK
%defattr(644,root,root,755)
%{_datadir}/*
%doc *.txt

%clean
rm -rf $RPM_BUILD_ROOT
