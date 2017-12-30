# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/harvmac
# catalog-date 2008-12-20 16:08:04 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-harvmac
Version:	20170414
Release:	1
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081220-2
+ Revision: 752523
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081220-1
+ Revision: 718604
- texlive-harvmac
- texlive-harvmac
- texlive-harvmac
- texlive-harvmac

