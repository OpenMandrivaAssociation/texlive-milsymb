%global tl_name milsymb
%global tl_revision 78431

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.03
Release:	%{tl_revision}.1
Summary:	LaTeX package for TikZ based drawing of military symbols as per NATO APP-6(C)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/milsymb
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/milsymb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/milsymb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers commands to draw military symbols as per NATO
APP-6(C) https://web.archive.org/web/20150921231042/http://armawiki.zumo
rc.de/files/NATO/APP-6(C).pdf . It has a set of commands for drawing all
symbols found in the document up to the control measures, as well as
support for custom non-standard symbols. Control measures are planned to
be included in a future release.

