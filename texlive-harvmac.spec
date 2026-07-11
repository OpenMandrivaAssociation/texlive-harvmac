%global tl_name harvmac
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros for scientific articles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/harvmac
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/harvmac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/harvmac.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Known as 'Harvard macros', since written at that University.

