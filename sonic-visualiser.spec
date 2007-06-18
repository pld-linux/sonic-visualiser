# TODO:
# - no idea why it links libvamp-hostsdk.so 
# - it works only with jackd;
#   it looks that in AudioTargetFactory::createCallbackTarget it calls abstract
#   AudioCallbackPlayTarget::isOK and AudioCallbackPlayTarget::~AudioCallbackPlayTarget
# - check BReq; 
# - only one file packaged?
#
Summary:	Sonic Visualiser - an application for viewing and analysing the contents of music audio files
Summary(pl.UTF-8):	Sonic Visualiser - przeglądarka i analizator zawartości plików dźwiękowych
Name:		sonic-visualiser
Version:	1.0
Release:	1.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/sv1/%{name}-%{version}.tar.gz
# Source0-md5:	1df2731920628b41563153fc37959ed5
URL:		http://www.sonicvisualiser.org/
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	bzip2-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libfishsound-devel
BuildRequires:	liblo-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libmad-devel
BuildRequires:	liboggz-devel
BuildRequires:	libraptor-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	portaudio-devel
BuildRequires:	qt4-qmake
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
qt4-qmake
%{__make} \
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
