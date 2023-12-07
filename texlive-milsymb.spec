Name:		texlive-milsymb
Version:	66697
Release:	1
Summary:	LaTeX package for TikZ based drawing of military symbols as per NATO APP-6(C)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/milsymb
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/milsymb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/milsymb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers commands to draw military symbols as per
NATO APP-6(C) https://www.awl.edu.pl/images/en/APP_6_C.pdf. It
has a set of commands for drawing all symbols found in the
document up to the control measures, as well as support for
custom non-standard symbols. Control measures are planned to be
included in a future release.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/milsymb
%doc %{_texmfdistdir}/doc/latex/milsymb

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
