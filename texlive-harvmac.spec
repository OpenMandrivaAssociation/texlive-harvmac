Name:		texlive-harvmac
Version:	20081220
Release:	1
Summary:	Macros for scientific articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/harvmac
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harvmac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harvmac.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Known as 'Harvard macros', since written at that University.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/harvmac/harvmac.tex
%doc %{_texmfdistdir}/doc/plain/harvmac/README
%doc %{_texmfdistdir}/doc/plain/harvmac/harvsamp.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
