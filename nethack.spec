%define		file_version	%(echo %{version} | tr -d .)
Summary:	NetHack - An adventure into the Mazes of Menace
Summary(es):	Juego estilo rogue que se basa en Dungeons and Dragons (calabozos y dragones)
Summary(no):	NetHack - Et eventyr i en faretruende labyrint
Summary(pl):	NetHack - Przygoda w Labiryntach Gro¼by
Summary(pt_BR):	Jogo estilo rogue baseado no Dungeons and Dragons
Name:		nethack
Version:	3.4.0
Release:	1
License:	Nethack GPL
Group:		Applications/Games
Source0:	ftp://ftp.nethack.org/pub/nethack/nh%{file_version}/src/%{name}-%{file_version}.tgz
Source1:	http://www.spod-central.org/~psmith/nh/spoi-%{file_version}.tar.gz
Source2:	http://www.spod-central.org/~psmith/nh/gazetteer.tar.gz
Source3:	%{name}.desktop
Source4:	%{name}.png
Source5:	Guidebook-3.2pl.ps.gz
Source6:	Guidebook.pdf
Source7:	%{name}rc.gz
Patch0:		%{name}-config.patch
Patch1:		%{name}-makefile.patch
# remove from cvs:
#Patch0:		%{name}-ph-pld.patch
#Patch1:		%{name}-pld.patch
#Patch2:		%{name}-ph-dlb-files.patch
URL:		http://www.nethack.org/
Requires:	/bin/gzip
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _nhdir	%{_datadir}/nethack
%define _dyndir	/var/games/nethack

%description
A dungeon game similar to rogue but more elaborate, very popular at
Unix sites and on PC-class machines (nethack is probably the most
widely distributed of the freeware dungeon games). The earliest
versions, written by Jay Fenlason and later considerably enhanced by
Andries Brouwer, were simply called `hack'. The name changed when
maintenance was taken over by a group of hackers originally organized
by Mike Stephenson.

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

NetHack 3.4.0 er siste utvidelse til NetHack, et tøm og røm eventyr
spill. Det er basert på spill som Rouge og Hack, og er etterfølgeren
til versjon 3.0 og 3.1 av NetHack.

Denne utgaven er kopilert støtte for følgende utvidelser: QT og
ncurses.

%description -l pl
Gra dziej±ca siê w lochu, podobna do rogue, lecz bardziej dopracowana.
Bardzo popularna na Uniksach i maszynach klasy PC (nethack jest
prawdopodobnie najszerzej rozpowszechnion± darmow± gr± labiryntow±.)
Najwcze¶niejsze wersje, napisane przez Jaya Fenlasona, a nastêpnie
znacznie rozszerzone przez Andriesa Brouwara, nazywa³y siê po prostu
'hack' (r±baæ, siekaæ.) Nazwa zmieni³a siê gdy opieka nad gr± zosta³a
przejêta przez grupê hackerów zawi±zan± przez Mike'a Stephensona.

%package spoilers
Summary:	Spoilers to NetHack
Summary(pl):	Psuje dla NetHacka
Group:		Applications/Games

%description spoilers
Spoilers - a set of texts which explain many secrets in the game.
Beware: the game after reading it becomes even more addictive! (But
you will lose delights of discovering its secrets.)

%description spoilers -l pl
Psuje - zbiór tekstów wyja¶niaj±cych wiele sekretów w grze. Uwaga: po
przeczytaniu gra staje siê jeszcze bardziej uzale¿niaj±ca! (Lecz
stracisz rozkosze poznawania jej tajników.)

%package doc-pdf
Summary:	Nethack Guidebook, PDF format
Summary(pl):	Nethackowy podrêcznik w formacie PDF
Group:		Applications/Games

%description doc-pdf
Nethack Guidebook, PDF format.

%description doc-pdf -l pl
Nethackowy podrêcznik w formacie PDF.

%prep
%setup -q -a 1 -a 2 -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
./sys/unix/setup.sh links

%{__make} all \
	CFLAGS="%{rpmcflags} -I../include -I%{_includedir}/ncurses" \
	LFLAGS="%{rpmldflags}" \
	CC="%{__cc}"

%{__make} -C util recover \
	CFLAGS="%{rpmcflags} -I../include" \
	LFLAGS="%{rpmldflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games/Roguelike,%{_mandir}/man6}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install util/recover $RPM_BUILD_ROOT%{_nhdir}

install doc/nethack.6 doc/recover.6 $RPM_BUILD_ROOT%{_mandir}/man6/

cp %{SOURCE5} %{SOURCE6} %{SOURCE7} .
gzip -9nf doc/Guidebook README doc/window.doc doc/fixes* doc/lists \
	$RPM_BUILD_ROOT%{_nhdir}/license
gzip -9nf	nhspoilers/README nhspoilers/*.txt nhspoilers/gazetteer/README

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Games/Roguelike
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz doc/*.gz %{name}rc.gz
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

%files doc-pdf
%defattr(644,root,root,755)
%doc Guidebook.pdf
