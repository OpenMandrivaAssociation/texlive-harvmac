Name:		texlive-harvmac
Version:	20180303
Release:	2
Summary:	Macros for scientific articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/harvmac
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harvmac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harvmac.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Known as 'Harvard macros', since written at that University.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/harvmac
%doc %{_texmfdistdir}/doc/plain/harvmac

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
