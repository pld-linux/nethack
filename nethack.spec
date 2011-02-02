#
# Conditional build:
%bcond_without	qt	# no X11 and Qt bloat 
#
# --define 'wizard other_username', default is root
%define		_wizard		%{?wizard:%{wizard}}%{!?wizard:"root"}
#
%define		file_version	%(echo %{version} | tr -d .)
Summary:	NetHack - An adventure into the Mazes of Menace
Summary(es.UTF-8):	Juego estilo rogue que se basa en Dungeons and Dragons (calabozos y dragones)
Summary(nb.UTF-8):	NetHack - Et eventyr i en faretruende labyrint
Summary(pl.UTF-8):	NetHack - Przygoda w Labiryntach Groźby
Summary(pt_BR.UTF-8):	Jogo estilo rogue baseado no Dungeons and Dragons
Name:		nethack
Version:	3.4.3
Release:	6
License:	Nethack GPL
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/nethack/%{name}-%{file_version}-src.tgz
# Source0-md5:	21479c95990eefe7650df582426457f9
Source1:	http://www.spod-central.org/~psmith/nh/spoi-%{file_version}.tar.gz
# Source1-md5:	72cac599c3660eac0a54b17ece8989ff
Source2:	http://www.spod-central.org/~psmith/nh/gazetteer.tar.gz
# Source2-md5:	651997ab54552b5e9a586cef46bcc50a
Source3:	%{name}.desktop
Source4:	%{name}.png
Source5:	Guidebook-3.2pl.ps.gz
# Source5-md5:	4a2a9a38deb08e9c4177c3b5ce6e627e
Source6:	Guidebook.pdf
Source7:	%{name}rc.gz
# Source7-md5:	ffd3d14ab4df527e9f3738320dec7f93
# http://avrc.city.ac.uk/nethack/VernonSpoilers/vol3-1.2.2.pdf
Source8:	%{name}-vol3-1.2.2.pdf
Patch0:		%{name}-config.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-gcc3.patch
Patch3:		%{name}-qt.patch
Patch4:		%{name}-qt33.patch
# http://www.userfriendly.org/games/nethack/nethack-3.4.3-turbonerd-0.1.0.patch
Patch5:		%{name}-3.4.3-turbonerd-0.1.0.patch
URL:		http://www.nethack.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	groff
BuildRequires:	ncurses-devel
%{?with_qt:BuildRequires:	qt-devel >= 3.0.3}
BuildRequires:	util-linux-ng
%{?with_qt:BuildRequires:	xorg-lib-libX11-devel}
Requires:	/bin/gzip
Conflicts:	applnk < 1.5.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_nhdir		%{_datadir}/nethack
%define		_dyndir		/var/games/nethack

%description
A dungeon game similar to rogue but more elaborate, very popular at
Unix sites and on PC-class machines (nethack is probably the most
widely distributed of the freeware dungeon games). The earliest
versions, written by Jay Fenlason and later considerably enhanced by
Andries Brouwer, were simply called `hack'. The name changed when
maintenance was taken over by a group of hackers originally organized
by Mike Stephenson.

%description -l pt_BR.UTF-8
Nethack é um jogo clássico estilo rogue, baseado no Dungeons and
Dragons. Ele é um jogo muito elaborado e profundo, desenvolvido há
anos pelo mesmo time de indivíduos.

%description -l es.UTF-8
Nethack es un juego clásico estilo rogue, basado en el juego Dungeons
and Dragons (calabozos y dragones). Es un juego muy elaborado y
profundo, desarrollado desde hace muchos años por el mismo grupo de
individuos.

%description -l nb.UTF-8
NetHack - Et eventyr i en faretruende labyrint.

NetHack 3.4.0 er siste utvidelse til NetHack, et tøm og røm eventyr
spill. Det er basert på spill som Rouge og Hack, og er etterfølgeren
til versjon 3.0 og 3.1 av NetHack.

Denne utgaven er kopilert støtte for følgende utvidelser: Qt og
ncurses.

%description -l pl.UTF-8
Gra dziejąca się w lochu, podobna do rogue, lecz bardziej dopracowana.
Bardzo popularna na Uniksach i maszynach klasy PC (nethack jest
prawdopodobnie najszerzej rozpowszechnioną darmową grą labiryntową.)
Najwcześniejsze wersje, napisane przez Jaya Fenlasona, a następnie
znacznie rozszerzone przez Andriesa Brouwara, nazywały się po prostu
'hack' (rąbać, siekać.) Nazwa zmieniła się gdy opieka nad grą została
przejęta przez grupę hackerów zawiązaną przez Mike'a Stephensona.

%package spoilers
Summary:	Spoilers to NetHack
Summary(pl.UTF-8):	Psuje dla NetHacka
Group:		Applications/Games

%description spoilers
Spoilers - a set of texts which explain many secrets in the game.
Beware: the game after reading it becomes even more addictive! (But
you will lose delights of discovering its secrets.)

%description spoilers -l pl.UTF-8
Psuje - zbiór tekstów wyjaśniających wiele sekretów w grze. Uwaga: po
przeczytaniu gra staje się jeszcze bardziej uzależniająca! (Lecz
stracisz rozkosze poznawania jej tajników.)

%package doc-pdf
Summary:	Nethack Guidebook, PDF format
Summary(pl.UTF-8):	Nethackowy podręcznik w formacie PDF
Group:		Applications/Games

%description doc-pdf
Nethack Guidebook, PDF format.

%description doc-pdf -l pl.UTF-8
Nethackowy podręcznik w formacie PDF.

%prep
%setup -q -a1 -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?with_qt:%patch3 -p1}
%patch4 -p1
%patch5 -p1

%build
sh ./sys/unix/setup.sh links

%{__make} -j1 all \
	CFLAGS="%{rpmcflags} -I../include -I/usr/include/ncurses -DWIZARD='\"%{_wizard}\"'" \
	LFLAGS="%{rpmldflags}" \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	LD="%{__cxx}" \
	QTDIR="%{_prefix}"

%{__make} -C util recover \
	CFLAGS="%{rpmcflags} -I../include" \
	LFLAGS="%{rpmldflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_mandir}/man6}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install util/recover $RPM_BUILD_ROOT%{_nhdir}

install doc/nethack.6 doc/recover.6 $RPM_BUILD_ROOT%{_mandir}/man6

cp %{SOURCE5} %{SOURCE6} %{SOURCE7} .
cp %{SOURCE8} vol3-1.2.2.pdf

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/Guidebook doc/window.doc doc/fixes* %{name}rc.gz
#%doc $RPM_BUILD_ROOT%{_nhdir}/license CHANGES*
%lang(pl) %doc Guidebook-3.2pl.ps.gz

%attr(2755,root,games) %{_prefix}/games/nethack
%attr(2755,root,games) %{_nhdir}/nethack
%attr(2755,root,games) %{_nhdir}/recover

%dir %{_nhdir}
%{_nhdir}/nhdat
%{?with_qt:%{_nhdir}/*.x[bp]m}
%{?with_qt:%{_nhdir}/x11tiles}

%attr(2775,root,games) %dir %{_dyndir}
%attr(2775,root,games) %dir %{_dyndir}/save
%attr(664,root,games) %{_dyndir}/perm
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) %{_dyndir}/record
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) %{_dyndir}/logfile

%{_mandir}/man6/*

%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

%files spoilers
%defattr(644,root,root,755)
%doc nhspoilers/README nhspoilers/*.txt
%doc %dir nhspoilers/gazetteer
%doc vol3-1.2.2.pdf

%files doc-pdf
%defattr(644,root,root,755)
%doc Guidebook.pdf
