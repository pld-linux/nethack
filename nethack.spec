%define file_version 331
Summary:	NetHack - An adventure into the Mazes of Menace
Summary(es):	Juego estilo rogue que se basa en Dungeons and Dragons (calabozos y dragones)
Summary(no):	NetHack - Et eventyr i en faretruende labyrint
Summary(pl):	NetHack - Przygoda w Labiryntach Gro¼by
Summary(pt_BR):	Jogo estilo rogue baseado no Dungeons and Dragons
Name:		nethack
Version:	3.3.1
Release:	2
License:	Nethack GPL
Group:		Applications/Games
Group(cs):	Aplikace/Hry
Group(da):	Programmer/Spil
Group(de):	Applikationen/Spiele
Group(es):	Aplicaciones/Juegos
Group(fr):	Applications/Jeux
Group(is):	Forrit/Leikir
Group(it):	Applicazioni/Giochi
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥²¡¼¥à
Group(no):	Applikasjoner/Spill
Group(pl):	Aplikacje/Gry
Group(pt):	Aplicações/Jogos
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/éÇÒÙ
Group(sl):	Programi/Igre
Group(sv):	Tillämpningar/Spel
Source0:	ftp://ftp.nethack.org/pub/nethack/nh331/src/%{name}-%{file_version}.tgz
Source1:	http://www.spod-central.org/~psmith/nh/spoi-%{file_version}.tar.gz
Source2:	http://www.spod-central.org/~psmith/nh/gazetteer.tar.gz
Source3:	%{name}.desktop
Source4:	%{name}.png
Source5:	Guidebook-3.2pl.ps.gz
Patch0:		%{name}-pld.patch
Icon:		roguelike.gif
URL:		http://www.nethack.org/
BuildRequires:	bison
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _nhdir	%{_datadir}/games/nethack
%define _dyndir	/var/games/nethack

%description
NetHack - An adventure into the Mazes of Menace. Nethack is a
D&D-inspired, roguelike game. It is a very elaborate and deep game,
developed over the years by the same team of individuals.

%description -l pt_BR
Nethack é um jogo clássico estilo rogue, baseado no Dungeons and
Dragons. Ele é um jogo muito elaborado e profundo, desenvolvido há
anos pelo mesmo time de indivíduos.

%description -l es
Nethack es un juego clásico estilo rogue, basado en el juego Dungeons
and Dragons (calabozos y dragones). Es un juego muy elaborado y
profundo, desarrollado desde hace muchos años por el mismo grupo de
individuos.

%description -l no
NetHack - Et eventyr i en faretruende labyrint.

NetHack 3.3.1 er siste utvidelse til NetHack, et tøm og røm eventyr
spill. Det er basert på spill som Rouge og Hack, og er etterfølgeren
til versjon 3.0 og 3.1 av NetHack.

Denne utgaven er kopilert støtte for følgende utvidelser: QT og
ncurses.

%description -l pl
NetHack -- Przygoda w Labiryntach Gro¼by.

NetHack jest gr± przygodow±, której akcja toczy siê w podziemnych
labiryntach. Wywodzi siê ze starszych gier, Rouge i Hack, i zawiera
wiele nowych rozszerzeñ w stosunku do poprzednich wersji.

%package spoilers
Summary:	Spoilers to NetHack
Summary(pl):	Spoilery dla NetHacka
Group:		Applications/Games
Group(cs):	Aplikace/Hry
Group(da):	Programmer/Spil
Group(de):	Applikationen/Spiele
Group(es):	Aplicaciones/Juegos
Group(fr):	Applications/Jeux
Group(is):	Forrit/Leikir
Group(it):	Applicazioni/Giochi
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥²¡¼¥à
Group(no):	Applikasjoner/Spill
Group(pl):	Aplikacje/Gry
Group(pt):	Aplicações/Jogos
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/éÇÒÙ
Group(sl):	Programi/Igre
Group(sv):	Tillämpningar/Spel

%description spoilers
Spoilers - a set of texts which explain many secrets in the game.
Beware: the game after reading it becomes even more addictive!!!

%description spoilers -l pl
Spoilery - zbiór tekstów wyja¶niaj±cych wiele sekretów w grze. Uwaga:
po przeczytaniu gra staje siê jeszcze bardziej uzale¿niaj±ca!

%prep
%setup -q -a 1 -a 2
%patch0 -p1

%build
./sys/unix/setup.sh links

%{__make} OPTFLAGS="%{rpmcflags}" all

%{__make} -C util OPTFLAGS="%{rpmcflags}" recover

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games/Roguelike}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__make} -C doc manpages DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_mandir}/man6/{dlb.6,dgn_comp.6,lev_comp.6}

install util/recover	$RPM_BUILD_ROOT%{_nhdir}

cp %{SOURCE5} .
gzip -9nf doc/Guidebook README doc/window.doc \
	$RPM_BUILD_ROOT%{_nhdir}/license \
	nhspoilers/README nhspoilers/*.txt nhspoilers/gazetteer/README

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Games/Roguelike
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz doc/{Guidebook,window.doc}.gz
%doc $RPM_BUILD_ROOT%{_nhdir}/license.gz
%lang(pl) %doc Guidebook-3.2pl.ps.gz

%attr(2755,root,games) %{_prefix}/games/nethack
%attr(2755,root,games) %{_nhdir}/nethack
%attr(2755,root,games) %{_nhdir}/recover

%attr(755,root,root) %dir %{_nhdir}
%{_nhdir}/nhdat
%{_nhdir}/*.xpm
%{_nhdir}/x11tiles

%attr(2775,root,games) %dir %{_dyndir}
%attr(2775,root,games) %dir %{_dyndir}/save
%attr(664,root,games) %{_dyndir}/perm
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) %{_dyndir}/record
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) %{_dyndir}/logfile

%{_mandir}/man6/*

%{_applnkdir}/Games/Roguelike/*
%{_pixmapsdir}/*

%files spoilers
%defattr(644,root,root,755)
%doc nhspoilers/README.gz nhspoilers/*.txt.gz
%doc %dir nhspoilers/gazetteer
