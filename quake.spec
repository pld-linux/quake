Summary(pl):	Quake dla Linuxa
Summary:	Quake for Linux
Name:		quake
Version:	1.06
Release:	1
Vendor:		id Software
URL:		http://www.idsoftware.com/
Source0:	ftp://ftp.idsoftware.com/idstuff/source/q1source.zip
Source1:	ftp://ftp.idsoftware.com/idstuff/quake/%{name}106.zip
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-makefileQW.patch
Patch2:		%{name}-QWGL.patch
Patch3:		%{name}-QWGLmouse.patch
Patch4:		%{name}-GL.patch
Group:		Applications/Games
Copyright:	Restricted
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	XFree86-OpenGL-devel
BuildRequires:	XFree86-driver-nvidia
BuildRequires:	lha

%description
"The most important PC game ever" - PC ZONE SVGA client

%description -l pl
"Najwazniejsza gra wszechczasow na PC" - PC ZONE Klient dla SVGA

%package x11
Summary:	Quake dla Linuxa - x11
Summary(pl):	Quake for Linux - x11
Group:		Applications/Games
Requires:	quake

%description x11
"The most important PC game ever" - PC ZONE x11 client

%description x11 -l pl
"Najwazniejsza gra wszechczasow na PC" - PC ZONE Klient dla x11

%package GL
Summary:	Quake dla Linuxa - GL
Summary(pl):	Quake for Linux - GL
Group:		Applications/Games
Requires:	quake

%description GL -l pl
"Najwazniejsza gra wszechczasow na PC" - PC ZONE Klient dla GL

%package PAK
Summary:	Quake dla Linuxa - epizod shareware
Summary(pl):	Quake for Linux - shareware episode
Group:		Applications/Games
Requires:	quake

%description PAK -l pl
"Najwazniejsza gra wszechczasow na PC" - PC ZONE Pliki PAK,
zawierajace 1 epizod shareware.

%prep
%setup -q -c -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp WinQuake/Makefile.linuxi386 WinQuake/Makefile
%{__make} -C WinQuake MOUNT_DIR=`pwd`/WinQuake EGCS=gcc GLIBC=.glibc
cp QW/Makefile.Linux QW/Makefile
%{__make} -C QW MAINDIR=`pwd`/QW
lha -ef resource.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/quake/id1}

install WinQuake/debugi386.glibc/bin/* $RPM_BUILD_ROOT%{_bindir}

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

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quake.x11
%attr(755,root,root) %{_bindir}/qwcl.x11
%doc WinQuake/docs/README.X11

%files GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glquake.glx
%attr(755,root,root) %{_bindir}/glqwcl.glx
%doc WinQuake/docs/readme.glquake QW/docs/glqwcl-readme.txt

%files PAK
%defattr(644,root,root,755)
%{_datadir}/*
%doc *.txt

%clean
rm -rf $RPM_BUILD_ROOT
