# revision 22191
# category Package
# catalog-ctan /macros/latex/contrib/euro
# catalog-date 2006-09-12 14:13:09 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-euro
Version:	1.1
Release:	6
Summary:	Provide Euro values for national currency amounts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/euro
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 751664
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718387
- texlive-euro
- texlive-euro
- texlive-euro
- texlive-euro

