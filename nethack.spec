%define file_version 331
Summary:	NetHack - An adventure into the Mazes of Menace
Summary(no):	NetHack - Et eventyr i en faretruende labyrint
Summary(pl):	NetHack - Przygoda w Labiryntach Gro¼by 
Name:		nethack
Version:	3.3.1
Release:	1
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
License:	GPL
Source0:	ftp://ftp.nethack.org/pub/nethack/nh331/src/%{name}-%{file_version}.tgz
Source1:	http://www.spod-central.org/~psmith/nh/spoi-%{file_version}.tar.gz
Source2:	http://www.spod-central.org/~psmith/nh/gazetteer.tar.gz
Patch0:		%{name}-pld.patch
Icon:		roguelike.gif
URL:		http://www.nethack.org/
BuildRequires:	bison
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetHack - An adventure into the Mazes of Menace.

NetHack 3.3.1 is a new enhancement to the dungeon exploration game
NetHack. It is a distant descendent of Rogue and Hack, and a direct
descendent of NetHack 3.1 and 3.0.

Compiled with: QT and ncurses support.

%description -l no
NetHack 3.3.1 -- Et eventyr i en faretruende labyrint.

NetHack 3.3.1 er siste utvidelse til NetHack, et tøm og røm eventyr
spill. Det er basert på spill som Rouge og Hack, og er etterfølgeren
til versjon 3.0 og 3.1 av NetHack.

Denne utgaven er kopilert støtte for følgende utvidelser: QT og
ncurses.

%description -l pl
NetHack 3.3.1 -- Przygoda w Labiryntach Gro¼by.

NetHack 3.3.1 jest przygodow± gr±, której akcja toczy siê w
podziemnych labiryntach. Wywodzi siê ze starszych gier, Rouge i Hack,
i zawiera wiele nowych rozszerzeñ w stosunku do poprzednich wersji 3.0
i 3.1.

Kompilowany ze wsparciem dla QT i ncurses.

%package spoilers
Summary:	Spoilers to NetHack.
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry

%description spoilers
Spoilers - a set of texts which explain many secrets in the game.
Beware: the game after reading it becomes even more addictive!!!

%prep
%setup -q -a 1 -a 2
%patch0 -p1

%build
./sys/unix/setup.sh links

%{__make} OPTFLAGS="%{rpmcflags}" all

%{__make} -C util OPTFLAGS="%{rpmcflags}" recover

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__make} -C doc manpages DESTDIR=$RPM_BUILD_ROOT

install util/recover	$RPM_BUILD_ROOT%{_datadir}/games/nethack
install util/*_comp	$RPM_BUILD_ROOT%{_datadir}/games/nethack

gzip -9nf doc/Guidebook.txt doc/Guidebook README doc/window.doc 

gzip -9nf nhspoilers/README nhspoilers/*.txt nhspoilers/gazetteer/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz doc/{Guidebook.txt,Guidebook,window.doc}.gz 
%attr(2750,root,games) %{_prefix}/games/nethack
%attr(2750,root,games) %{_datadir}/games/nethack/nethack
%attr(2750,root,games) %{_datadir}/games/nethack/recover
%attr(2750,root,games) %{_datadir}/games/nethack/*_comp

%attr(2770,root,games) %dir %{_datadir}/games/nethack
%attr(640,root,games) %{_datadir}/games/nethack/nhdat
%attr(640,root,games) %{_datadir}/games/nethack/license
%attr(640,root,games) %{_datadir}/games/nethack/*.xpm
%attr(640,root,games) %{_datadir}/games/nethack/x11tiles

%attr(775,root,games) %dir /var/games/nethack
%attr(775,root,games) %dir /var/games/nethack/save
%attr(664,root,games) /var/games/nethack/perm
%attr(664,root,games) /var/games/nethack/record
%attr(664,root,games) /var/games/nethack/logfile

%{_mandir}/man6/*

%files spoilers
%defattr(644,root,root,755)
%doc nhspoilers/README.gz nhspoilers/*.txt.gz
%doc %dir nhspoilers/gazetteer
