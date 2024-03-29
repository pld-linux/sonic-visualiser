# TODO:
# - It segfaults when jack and oss are not avaiable. It tries to use portaudio
#   Pa_GetDefaultOutputDevice. Pa_GetDefaultHostApi is "oss", unfortunatly
#   without any usefull device.
# 
# - only one file packaged?
#
Summary:	Sonic Visualiser - an application for viewing and analysing the contents of music audio files
Summary(pl.UTF-8):	Sonic Visualiser - przeglądarka i analizator zawartości plików dźwiękowych
Name:		sonic-visualiser
Version:	1.7.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/sv1/%{name}-%{version}.tar.bz2
# Source0-md5:	1d71511cd584e25159f56f41d6344446
URL:		http://www.sonicvisualiser.org/
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	QtGui-devel
BuildRequires:	bzip2-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libfishsound-devel
BuildRequires:	libid3tag-devel
BuildRequires:	liblo-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libmad-devel
BuildRequires:	liboggz-devel
BuildRequires:	libraptor-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	portaudio-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rasqal-devel
BuildRequires:	redland-devel
BuildRequires:	rubberband-devel
BuildRequires:	vamp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sonic Visualiser is an application for viewing and analysing the
contents of music audio files.

The aim of Sonic Visualiser is to be the program you reach for when
you find a musical recording you want to study rather than simply
hear.

As well as a number of features designed to make exploring audio data
as revealing and fun as possible, Sonic Visualiser also has powerful
annotation capabilities to help you to describe what you find, and the
ability to run automated annotation and analysis plugins in the new
Vamp analysis plugin format.

%description -l pl.UTF-8
Sonic Visualiser przeglądarką i analizatorem zawartości plików
dźwiękowych.

Sonic Visualiser stara się być programem, po który sięga się bardziej
w celu przestudiowania nagrania muzycznego, niż jedynie jego odsłuchu.

Ma wiele możliwości stworzonych aby uczynić badanie danych dźwiękowych
tak odkrywczym i zabawnym jak to tylko możliwe. Ma także duże
możliwości pozwalające na opisywanie tego co widać i możliwość
automatycznego uruchamiania wtyczek notatek i analizy w nowym formacie
wtyczek analizujących Vamp.

%prep
%setup -q

%build
qmake-qt4
%{__make} -j1 \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sv/sonic-visualiser $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
