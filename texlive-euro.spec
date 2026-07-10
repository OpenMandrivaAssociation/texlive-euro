%global tl_name euro
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Provide Euro values for national currency amounts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/euro
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euro.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euro.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euro.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Converts arbitrary national currency amounts using the Euro as base
unit, and typesets monetary amounts in almost any desired way. Write,
e.g., \ATS{17.6} to get something like '17,60 oS (1,28 Euro)'
automatically. Conversion rates for the initial Euro-zone countries are
already built-in. Further rates can be added easily. The package uses
the fp package to do its sums.

