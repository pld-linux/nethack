Summary:	NetHack - An adventure into the Mazes of Menace
Summary(no):	NetHack - Et eventyr i en faretruende labyrint
Summary(pl):	NetHack - Przygoda w Labiryntach Gro¼by 
Name:		nethack
Version:	3.2.2
Release:	6
Group:		Games
Group(pl):	Gry
License:	GPL
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		nethack-pld.patch
Patch1:		nethack-makefile.patch
Icon:		rougelike.gif
URL:		http://www.win.tue.nl/games/roguelike/nethack/
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetHack 3.2.2 -- An adventure into the Mazes of Menace.

NetHack 3.2.2 is a new enhancement to the dungeon exploration game
NetHack. It is a distant descendent of Rogue and Hack, and a direct
descendent of NetHack 3.1 and 3.0.

Compiled with: X11 support, glibc 2.1 and ncurses.

%description -l no
NetHack 3.2.2 -- Et eventyr i en faretruende labyrint.

NetHack 3.2.2 er siste utvidelse til NetHack, et tøm og røm eventyr
spill. Det er basert på spill som Rouge og Hack, og er etterfølgeren
til versjon 3.0 og 3.1 av NetHack.

Denne utgaven er kopilert støtte for følgende utvidelser: X11, glibc
2.1 og ncurses.

%description -l pl
NetHack 3.2.2 -- Przygoda w Labiryntach Gro¼by.

NetHack 3.2.2 jest przygodow± gr±, której akcja toczy siê w
podziemnych labiryntach. Wywodzi siê ze starszych gier, Rouge i Hack,
i zawiera wiele nowych rozszerzeñ w stosunku do poprzednich wersji 3.0
i 3.1.

Kompilowany ze wsparciem dla X11, glibc 2.1 i ncurses.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./sys/unix/setup.sh links

%{__make} OPTFLAGS="$RPM_OPT_FLAGS" all

%{__make} -C util OPTFLAGS="$RPM_OPT_FLAGS" recover

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{games/nethack,fonts/misc} \
$RPM_BUILD_ROOT{%{_mandir}/man6,%{_prefix}/X11R6/lib/X11/app-defaults} \
	$RPM_BUILD_ROOT/var/games/nethack

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__make} -C doc manpages DESTDIR=$RPM_BUILD_ROOT

install util/recover	$RPM_BUILD_ROOT%{_datadir}/games/nethack
install util/*_comp	$RPM_BUILD_ROOT%{_datadir}/games/nethack

install win/X11/NetHack.ad \
$RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/app-defaults/NetHack

(cd win/X11 ;
%{_prefix}/X11R6/bin/bdftopcf < nh10.bdf > nh10.pcf
%{_prefix}/X11R6/bin/bdftopcf < ibm.bdf > ibm.pcf
install nh10.pcf ibm.pcf $RPM_BUILD_ROOT%{_datadir}/fonts/misc
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man6/* \
	$RPM_BUILD_ROOT%{_datadir}/fonts/misc/*.pcf \
	doc/Guidebook* doc/tmac.n README doc/window.doc 

%post
/usr/X11R6/bin/mkfontdir /usr/share/fonts/misc

%postun
/usr/X11R6/bin/mkfontdir /usr/share/fonts/misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{Guidebook*,tmac.n,Guidebook,window.doc}.gz 
%doc win/X11/nethack.rc README.gz
%attr(0755,root,root) %{_prefix}/games/nethack
%attr(2755,root,games) %{_datadir}/games/nethack/nethack
%attr(2755,root,games) %{_datadir}/games/nethack/recover
%attr(0755,root,root) %{_datadir}/games/nethack/*_comp

%attr(755,root,root) %dir %{_datadir}/games/nethack
%{_datadir}/games/nethack/nhdat
%{_datadir}/games/nethack/license
%{_datadir}/games/nethack/*.xpm
%{_datadir}/games/nethack/x11tiles

%attr(775,root,games) %dir /var/games/nethack
%attr(775,root,games) %dir /var/games/nethack/save
%attr(664,root,games) /var/games/nethack/perm
%attr(664,root,games) /var/games/nethack/record
%attr(664,root,games) /var/games/nethack/logfile

%{_datadir}/fonts/misc/*.pcf.gz
%{_mandir}/man6/*

%config %{_prefix}/X11R6/lib/X11/app-defaults/NetHack
