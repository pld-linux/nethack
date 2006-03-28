#
# Conditional build:
%bcond_without	qt	# no X11 and Qt bloat 
%bcond_with	vanilla	# build vanilla NetHack (without patches)
#
# --define 'wizard other_username', default is root
%define		_wizard		%{?wizard:%{wizard}}%{!?wizard:"root"}
#
# no patches for now, wait for updates
%define		with_vanilla	1
#
%define		file_version	%(echo %{version} | tr -d .)
Summary:	NetHack - An adventure into the Mazes of Menace
Summary(es):	Juego estilo rogue que se basa en Dungeons and Dragons (calabozos y dragones)
Summary(nb):	NetHack - Et eventyr i en faretruende labyrint
Summary(pl):	NetHack - Przygoda w Labiryntach Gro�by
Summary(pt_BR):	Jogo estilo rogue baseado no Dungeons and Dragons
Name:		nethack
Version:	3.4.3
Release:	2
License:	Nethack GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/sourceforge/nethack/%{name}-%{file_version}-src.tgz
# Source0-md5:	21479c95990eefe7650df582426457f9
Source1:	http://www.spod-central.org/~psmith/nh/spoi-%{file_version}.tar.gz
# Source1-md5:	72cac599c3660eac0a54b17ece8989ff
#Source1:	http://www.spod-central.org/~psmith/nh/spoi-340.tar.gz
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
# patches below are adapted from ones found at http://avrc.city.ac.uk/nethack/patches.html
# warning: order is important in most cases
Patch100:	%{name}-show_born.patch
Patch101:	%{name}-dump.patch
Patch102:	%{name}-behind_boulder.patch
Patch103:	%{name}-yafm-monabil.patch
Patch104:	%{name}-chivalry.patch
Patch105:	%{name}-kenny.patch
Patch106:	%{name}-sticky_objects.patch
Patch107:	%{name}-steed-fix.patch
Patch108:	%{name}-wash_hands.patch
Patch109:	%{name}-listmons.patch
Patch110:	%{name}-flipcoin.patch
Patch111:	%{name}-ride_key.patch
Patch112:	%{name}-dungeon_growth.patch
Patch113:	%{name}-dragon_hoard.patch
Patch114:	%{name}-torch.patch
Patch115:	%{name}-hole.patch
Patch116:	%{name}-mirror.patch
Patch117:	%{name}-newt.patch
# after adding additional features update this patch
Patch200:	%{name}-makedefs.patch
URL:		http://www.nethack.org/
%{?with_qt:BuildRequires:	XFree86-devel}
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	groff
BuildRequires:	ncurses-devel
%{?with_qt:BuildRequires:	qt-devel >= 3.0.3}
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

%{!?with_vanilla:This package contains additional features.}

%description -l pt_BR
Nethack � um jogo cl�ssico estilo rogue, baseado no Dungeons and
Dragons. Ele � um jogo muito elaborado e profundo, desenvolvido h�
anos pelo mesmo time de indiv�duos.

%description -l es
Nethack es un juego cl�sico estilo rogue, basado en el juego Dungeons
and Dragons (calabozos y dragones). Es un juego muy elaborado y
profundo, desarrollado desde hace muchos a�os por el mismo grupo de
individuos.

%description -l nb
NetHack - Et eventyr i en faretruende labyrint.

NetHack 3.4.0 er siste utvidelse til NetHack, et t�m og r�m eventyr
spill. Det er basert p� spill som Rouge og Hack, og er etterf�lgeren
til versjon 3.0 og 3.1 av NetHack.

Denne utgaven er kopilert st�tte for f�lgende utvidelser: Qt og
ncurses.

%description -l pl
Gra dziej�ca si� w lochu, podobna do rogue, lecz bardziej dopracowana.
Bardzo popularna na Uniksach i maszynach klasy PC (nethack jest
prawdopodobnie najszerzej rozpowszechnion� darmow� gr� labiryntow�.)
Najwcze�niejsze wersje, napisane przez Jaya Fenlasona, a nast�pnie
znacznie rozszerzone przez Andriesa Brouwara, nazywa�y si� po prostu
'hack' (r�ba�, sieka�.) Nazwa zmieni�a si� gdy opieka nad gr� zosta�a
przej�ta przez grup� hacker�w zawi�zan� przez Mike'a Stephensona.

%{!?with_vanilla:Ten pakiet zawiera dodatkowe bajery.}

%package spoilers
Summary:	Spoilers to NetHack
Summary(pl):	Psuje dla NetHacka
Group:		Applications/Games

%description spoilers
Spoilers - a set of texts which explain many secrets in the game.
Beware: the game after reading it becomes even more addictive! (But
you will lose delights of discovering its secrets.)

%description spoilers -l pl
Psuje - zbi�r tekst�w wyja�niaj�cych wiele sekret�w w grze. Uwaga: po
przeczytaniu gra staje si� jeszcze bardziej uzale�niaj�ca! (Lecz
stracisz rozkosze poznawania jej tajnik�w.)

%package doc-pdf
Summary:	Nethack Guidebook, PDF format
Summary(pl):	Nethackowy podr�cznik w formacie PDF
Group:		Applications/Games

%description doc-pdf
Nethack Guidebook, PDF format.

%description doc-pdf -l pl
Nethackowy podr�cznik w formacie PDF.

%prep
%setup -q -a1 -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?with_qt:%patch3 -p1}
%patch4 -p1

# patches adding fun
%{!?with_vanilla:%patch100 -p1}
%{!?with_vanilla:%patch101 -p1}
%{!?with_vanilla:%patch102 -p1}
%{!?with_vanilla:%patch103 -p1}
%{!?with_vanilla:%patch104 -p1}
%{!?with_vanilla:%patch105 -p1}
%{!?with_vanilla:%patch106 -p1}
%{!?with_vanilla:%patch107 -p1}
%{!?with_vanilla:%patch108 -p1}
%{!?with_vanilla:%patch109 -p1}
%{!?with_vanilla:%patch110 -p1}
%{!?with_vanilla:%patch111 -p1}
%{!?with_vanilla:%patch112 -p1}
%{!?with_vanilla:%patch113 -p1}
#%%{!?with_vanilla:%patch114 -p1}
#%%{!?with_vanilla:%patch115 -p1}
#%%{!?with_vanilla:%patch116 -p1}
%{!?with_vanilla:%patch117 -p1}
%{!?with_vanilla:%patch200 -p1}

%build
sh ./sys/unix/setup.sh links

%{__make} all \
	CFLAGS="%{rpmcflags} -I../include -I%{_includedir}/ncurses -DWIZARD='\"%{_wizard}\"' -DINSURANCE" \
	LFLAGS="%{rpmldflags}" \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	LD="%{__cxx}" \
	QTDIR="%{_prefix}"

%{__make} -C util recover \
	CFLAGS="%{rpmcflags} -I../include -DINSURANCE" \
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

%attr(755,root,root) %dir %{_nhdir}
%{_nhdir}/nhdat
%{?with_qt:%{_nhdir}/*.x[bp]m}
%{?with_qt:%{_nhdir}/x11tiles}

%attr(2775,root,games) %dir %{_dyndir}
%attr(2775,root,games) %dir %{_dyndir}/save
%attr(664,root,games) %{_dyndir}/perm
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) %{_dyndir}/record
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) %{_dyndir}/logfile

%{_mandir}/man6/*

%{_desktopdir}/*
%{_pixmapsdir}/*

%files spoilers
%defattr(644,root,root,755)
%doc nhspoilers/README nhspoilers/*.txt
%doc %dir nhspoilers/gazetteer
%doc vol3-1.2.2.pdf

%files doc-pdf
%defattr(644,root,root,755)
%doc Guidebook.pdf
