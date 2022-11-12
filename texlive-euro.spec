Name:		texlive-euro
Version:	22191
Release:	1
Summary:	Provide Euro values for national currency amounts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/euro
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Converts arbitrary national currency amounts using the Euro as
base unit, and typesets monetary amounts in almost any desired
way. Write, e.g., \ATS{17.6} to get something like '17,60 oS
(1,28 Euro)' automatically. Conversion rates for the initial
Euro-zone countries are already built-in. Further rates can be
added easily. The package uses the fp package to do its sums.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/euro/euro.sty
%doc %{_texmfdistdir}/doc/latex/euro/Makefile
%doc %{_texmfdistdir}/doc/latex/euro/euro.pdf
%doc %{_texmfdistdir}/doc/latex/euro/euro.txt
#- source
%doc %{_texmfdistdir}/source/latex/euro/euro.dtx
%doc %{_texmfdistdir}/source/latex/euro/euro.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
