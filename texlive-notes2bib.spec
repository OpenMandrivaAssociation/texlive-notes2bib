# revision 31162
# category Package
# catalog-ctan /macros/latex/contrib/notes2bib
# catalog-date 2013-07-11 12:09:47 +0200
# catalog-license lppl
# catalog-version 2.0k
Name:		texlive-notes2bib
Version:	2.0k
Release:	7
Summary:	Integrating notes into the bibliography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/notes2bib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notes2bib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notes2bib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notes2bib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a new type of note, bibnote, which will
always be added to the bibliography. The package allows
footnotes and endnotes to be moved into the bibliography in the
same way. The package can be used with natbib and biblatex as
well as plain LaTeX citations. Both sorted and unsorted
bibliography styles are supported. The package uses the LaTeX 3
macros and the associated xpackages bundle. It also makes use
of the e-TeX extensions (any post-2005 LaTeX distribution will
provide these by default, but users of older systems may need
to use an elatex command or equivalent). The package relies on
LaTeX 3 support from the l3kernel and l3packages bundles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/notes2bib/notes2bib.sty
%doc %{_texmfdistdir}/doc/latex/notes2bib/README
%doc %{_texmfdistdir}/doc/latex/notes2bib/notes2bib.pdf
#- source
%doc %{_texmfdistdir}/source/latex/notes2bib/notes2bib.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
