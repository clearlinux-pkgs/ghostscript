#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ghostscript
Version  : 9.22
Release  : 6
URL      : https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs922/ghostscript-9.22.tar.gz
Source0  : https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs922/ghostscript-9.22.tar.gz
Summary  : Loads and saves PNG files
Group    : Development/Tools
License  : AGPL-3.0 BSD-2-Clause BSL-1.0 FTL GPL-2.0 IJG Libpng MIT libtiff
Requires: ghostscript-bin
Requires: ghostscript-lib
Requires: ghostscript-data
Requires: ghostscript-doc
BuildRequires : cmake
BuildRequires : cups-dev
BuildRequires : dbus-dev
BuildRequires : e2fsprogs-dev
BuildRequires : freeglut-dev
BuildRequires : glu-dev
BuildRequires : krb5-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xt)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev
BuildRequires : scons
BuildRequires : sed
BuildRequires : zlib-dev

%description
See the note about version numbers near the top of png.h
See INSTALL for instructions on how to install libpng.

%package bin
Summary: bin components for the ghostscript package.
Group: Binaries
Requires: ghostscript-data

%description bin
bin components for the ghostscript package.


%package data
Summary: data components for the ghostscript package.
Group: Data

%description data
data components for the ghostscript package.


%package dev
Summary: dev components for the ghostscript package.
Group: Development
Requires: ghostscript-lib
Requires: ghostscript-bin
Requires: ghostscript-data
Provides: ghostscript-devel

%description dev
dev components for the ghostscript package.


%package doc
Summary: doc components for the ghostscript package.
Group: Documentation

%description doc
doc components for the ghostscript package.


%package lib
Summary: lib components for the ghostscript package.
Group: Libraries
Requires: ghostscript-data

%description lib
lib components for the ghostscript package.


%prep
%setup -q -n ghostscript-9.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520545873
%configure --disable-static
make  %{?_smp_mflags} all so

%install
export SOURCE_DATE_EPOCH=1520545873
rm -rf %{buildroot}
%make_install install-so

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dvipdf
/usr/bin/eps2eps
/usr/bin/gs
/usr/bin/gsbj
/usr/bin/gsc
/usr/bin/gsdj
/usr/bin/gsdj500
/usr/bin/gslj
/usr/bin/gslp
/usr/bin/gsnd
/usr/bin/gsx
/usr/bin/lprsetup.sh
/usr/bin/pdf2dsc
/usr/bin/pdf2ps
/usr/bin/pf2afm
/usr/bin/pfbtopfa
/usr/bin/pphs
/usr/bin/printafm
/usr/bin/ps2ascii
/usr/bin/ps2epsi
/usr/bin/ps2pdf
/usr/bin/ps2pdf12
/usr/bin/ps2pdf13
/usr/bin/ps2pdf14
/usr/bin/ps2pdfwr
/usr/bin/ps2ps
/usr/bin/ps2ps2
/usr/bin/unix-lpr.sh

%files data
%defattr(-,root,root,-)
/usr/share/ghostscript/9.22/doc/API.htm
/usr/share/ghostscript/9.22/doc/AUTHORS
/usr/share/ghostscript/9.22/doc/C-style.htm
/usr/share/ghostscript/9.22/doc/COPYING
/usr/share/ghostscript/9.22/doc/Changes.htm
/usr/share/ghostscript/9.22/doc/Commprod.htm
/usr/share/ghostscript/9.22/doc/DLL.htm
/usr/share/ghostscript/9.22/doc/Deprecated.htm
/usr/share/ghostscript/9.22/doc/Details.htm
/usr/share/ghostscript/9.22/doc/Details8.htm
/usr/share/ghostscript/9.22/doc/Details9.htm
/usr/share/ghostscript/9.22/doc/Develop.htm
/usr/share/ghostscript/9.22/doc/Devices.htm
/usr/share/ghostscript/9.22/doc/Drivers.htm
/usr/share/ghostscript/9.22/doc/Fonts.htm
/usr/share/ghostscript/9.22/doc/GS9_Color_Management.pdf
/usr/share/ghostscript/9.22/doc/GS9_Color_Management.tex
/usr/share/ghostscript/9.22/doc/Helpers.htm
/usr/share/ghostscript/9.22/doc/Hershey.htm
/usr/share/ghostscript/9.22/doc/History1.htm
/usr/share/ghostscript/9.22/doc/History2.htm
/usr/share/ghostscript/9.22/doc/History3.htm
/usr/share/ghostscript/9.22/doc/History4.htm
/usr/share/ghostscript/9.22/doc/History5.htm
/usr/share/ghostscript/9.22/doc/History6.htm
/usr/share/ghostscript/9.22/doc/History7.htm
/usr/share/ghostscript/9.22/doc/History8.htm
/usr/share/ghostscript/9.22/doc/History9.htm
/usr/share/ghostscript/9.22/doc/Install.htm
/usr/share/ghostscript/9.22/doc/Issues.htm
/usr/share/ghostscript/9.22/doc/Language.htm
/usr/share/ghostscript/9.22/doc/Lib.htm
/usr/share/ghostscript/9.22/doc/Make.htm
/usr/share/ghostscript/9.22/doc/News.htm
/usr/share/ghostscript/9.22/doc/Projects.htm
/usr/share/ghostscript/9.22/doc/Ps-style.htm
/usr/share/ghostscript/9.22/doc/Ps2epsi.htm
/usr/share/ghostscript/9.22/doc/Psfiles.htm
/usr/share/ghostscript/9.22/doc/Readme.htm
/usr/share/ghostscript/9.22/doc/Release.htm
/usr/share/ghostscript/9.22/doc/Source.htm
/usr/share/ghostscript/9.22/doc/Unix-lpr.htm
/usr/share/ghostscript/9.22/doc/Use.htm
/usr/share/ghostscript/9.22/doc/WhatIsGS.htm
/usr/share/ghostscript/9.22/doc/Xfonts.htm
/usr/share/ghostscript/9.22/doc/gs-vms.hlp
/usr/share/ghostscript/9.22/doc/gs.css
/usr/share/ghostscript/9.22/doc/gsdoc.el
/usr/share/ghostscript/9.22/doc/index.html
/usr/share/ghostscript/9.22/doc/pscet_status.txt
/usr/share/ghostscript/9.22/doc/thirdparty.htm
/usr/share/ghostscript/9.22/examples/alphabet.ps
/usr/share/ghostscript/9.22/examples/annots.pdf
/usr/share/ghostscript/9.22/examples/cjk/all_ac1.ps
/usr/share/ghostscript/9.22/examples/cjk/all_ag1.ps
/usr/share/ghostscript/9.22/examples/cjk/all_aj1.ps
/usr/share/ghostscript/9.22/examples/cjk/all_aj2.ps
/usr/share/ghostscript/9.22/examples/cjk/all_ak1.ps
/usr/share/ghostscript/9.22/examples/cjk/article9.ps
/usr/share/ghostscript/9.22/examples/cjk/gscjk_ac.ps
/usr/share/ghostscript/9.22/examples/cjk/gscjk_ag.ps
/usr/share/ghostscript/9.22/examples/cjk/gscjk_aj.ps
/usr/share/ghostscript/9.22/examples/cjk/gscjk_ak.ps
/usr/share/ghostscript/9.22/examples/cjk/iso2022.ps
/usr/share/ghostscript/9.22/examples/cjk/iso2022v.ps
/usr/share/ghostscript/9.22/examples/colorcir.ps
/usr/share/ghostscript/9.22/examples/doretree.ps
/usr/share/ghostscript/9.22/examples/escher.ps
/usr/share/ghostscript/9.22/examples/golfer.eps
/usr/share/ghostscript/9.22/examples/grayalph.ps
/usr/share/ghostscript/9.22/examples/ridt91.eps
/usr/share/ghostscript/9.22/examples/snowflak.ps
/usr/share/ghostscript/9.22/examples/text_graph_image_cmyk_rgb.pdf
/usr/share/ghostscript/9.22/examples/text_graphic_image.pdf
/usr/share/ghostscript/9.22/examples/tiger.eps
/usr/share/ghostscript/9.22/examples/transparency_example.ps
/usr/share/ghostscript/9.22/examples/vasarely.ps
/usr/share/ghostscript/9.22/examples/waterfal.ps
/usr/share/ghostscript/9.22/lib/PDFA_def.ps
/usr/share/ghostscript/9.22/lib/PDFX_def.ps
/usr/share/ghostscript/9.22/lib/PM760p.upp
/usr/share/ghostscript/9.22/lib/PM760pl.upp
/usr/share/ghostscript/9.22/lib/PM820p.upp
/usr/share/ghostscript/9.22/lib/PM820pl.upp
/usr/share/ghostscript/9.22/lib/Stc670p.upp
/usr/share/ghostscript/9.22/lib/Stc670pl.upp
/usr/share/ghostscript/9.22/lib/Stc680p.upp
/usr/share/ghostscript/9.22/lib/Stc680pl.upp
/usr/share/ghostscript/9.22/lib/Stc740p.upp
/usr/share/ghostscript/9.22/lib/Stc740pl.upp
/usr/share/ghostscript/9.22/lib/Stc760p.upp
/usr/share/ghostscript/9.22/lib/Stc760pl.upp
/usr/share/ghostscript/9.22/lib/Stc777p.upp
/usr/share/ghostscript/9.22/lib/Stc777pl.upp
/usr/share/ghostscript/9.22/lib/Stp720p.upp
/usr/share/ghostscript/9.22/lib/Stp720pl.upp
/usr/share/ghostscript/9.22/lib/Stp870p.upp
/usr/share/ghostscript/9.22/lib/Stp870pl.upp
/usr/share/ghostscript/9.22/lib/acctest.ps
/usr/share/ghostscript/9.22/lib/align.ps
/usr/share/ghostscript/9.22/lib/bj8.rpd
/usr/share/ghostscript/9.22/lib/bj8gc12f.upp
/usr/share/ghostscript/9.22/lib/bj8hg12f.upp
/usr/share/ghostscript/9.22/lib/bj8oh06n.upp
/usr/share/ghostscript/9.22/lib/bj8pa06n.upp
/usr/share/ghostscript/9.22/lib/bj8pp12f.upp
/usr/share/ghostscript/9.22/lib/bj8ts06n.upp
/usr/share/ghostscript/9.22/lib/bjc6000a1.upp
/usr/share/ghostscript/9.22/lib/bjc6000b1.upp
/usr/share/ghostscript/9.22/lib/bjc610a0.upp
/usr/share/ghostscript/9.22/lib/bjc610a1.upp
/usr/share/ghostscript/9.22/lib/bjc610a2.upp
/usr/share/ghostscript/9.22/lib/bjc610a3.upp
/usr/share/ghostscript/9.22/lib/bjc610a4.upp
/usr/share/ghostscript/9.22/lib/bjc610a5.upp
/usr/share/ghostscript/9.22/lib/bjc610a6.upp
/usr/share/ghostscript/9.22/lib/bjc610a7.upp
/usr/share/ghostscript/9.22/lib/bjc610a8.upp
/usr/share/ghostscript/9.22/lib/bjc610b1.upp
/usr/share/ghostscript/9.22/lib/bjc610b2.upp
/usr/share/ghostscript/9.22/lib/bjc610b3.upp
/usr/share/ghostscript/9.22/lib/bjc610b4.upp
/usr/share/ghostscript/9.22/lib/bjc610b6.upp
/usr/share/ghostscript/9.22/lib/bjc610b7.upp
/usr/share/ghostscript/9.22/lib/bjc610b8.upp
/usr/share/ghostscript/9.22/lib/caption.ps
/usr/share/ghostscript/9.22/lib/cbjc600.ppd
/usr/share/ghostscript/9.22/lib/cbjc800.ppd
/usr/share/ghostscript/9.22/lib/cdj550.upp
/usr/share/ghostscript/9.22/lib/cdj690.upp
/usr/share/ghostscript/9.22/lib/cdj690ec.upp
/usr/share/ghostscript/9.22/lib/cid2code.ps
/usr/share/ghostscript/9.22/lib/dmp_init.ps
/usr/share/ghostscript/9.22/lib/dmp_site.ps
/usr/share/ghostscript/9.22/lib/dnj750c.upp
/usr/share/ghostscript/9.22/lib/dnj750m.upp
/usr/share/ghostscript/9.22/lib/docie.ps
/usr/share/ghostscript/9.22/lib/escp_24.src
/usr/share/ghostscript/9.22/lib/font2pcl.ps
/usr/share/ghostscript/9.22/lib/ghostpdf.ppd
/usr/share/ghostscript/9.22/lib/gs_ce_e.ps
/usr/share/ghostscript/9.22/lib/gs_cmdl.ps
/usr/share/ghostscript/9.22/lib/gs_il2_e.ps
/usr/share/ghostscript/9.22/lib/gs_kanji.ps
/usr/share/ghostscript/9.22/lib/gs_ksb_e.ps
/usr/share/ghostscript/9.22/lib/gs_l.xbm
/usr/share/ghostscript/9.22/lib/gs_l.xpm
/usr/share/ghostscript/9.22/lib/gs_l_m.xbm
/usr/share/ghostscript/9.22/lib/gs_lgo_e.ps
/usr/share/ghostscript/9.22/lib/gs_lgx_e.ps
/usr/share/ghostscript/9.22/lib/gs_m.xbm
/usr/share/ghostscript/9.22/lib/gs_m.xpm
/usr/share/ghostscript/9.22/lib/gs_m_m.xbm
/usr/share/ghostscript/9.22/lib/gs_s.xbm
/usr/share/ghostscript/9.22/lib/gs_s.xpm
/usr/share/ghostscript/9.22/lib/gs_s_m.xbm
/usr/share/ghostscript/9.22/lib/gs_t.xbm
/usr/share/ghostscript/9.22/lib/gs_t.xpm
/usr/share/ghostscript/9.22/lib/gs_t_m.xbm
/usr/share/ghostscript/9.22/lib/gs_wl1_e.ps
/usr/share/ghostscript/9.22/lib/gs_wl2_e.ps
/usr/share/ghostscript/9.22/lib/gs_wl5_e.ps
/usr/share/ghostscript/9.22/lib/gslp.ps
/usr/share/ghostscript/9.22/lib/gsnup.ps
/usr/share/ghostscript/9.22/lib/ht_ccsto.ps
/usr/share/ghostscript/9.22/lib/image-qa.ps
/usr/share/ghostscript/9.22/lib/jispaper.ps
/usr/share/ghostscript/9.22/lib/landscap.ps
/usr/share/ghostscript/9.22/lib/lines.ps
/usr/share/ghostscript/9.22/lib/mkcidfm.ps
/usr/share/ghostscript/9.22/lib/necp2x.upp
/usr/share/ghostscript/9.22/lib/necp2x6.upp
/usr/share/ghostscript/9.22/lib/pdf2dsc.ps
/usr/share/ghostscript/9.22/lib/pf2afm.ps
/usr/share/ghostscript/9.22/lib/pfbtopfa.ps
/usr/share/ghostscript/9.22/lib/ppath.ps
/usr/share/ghostscript/9.22/lib/pphs.ps
/usr/share/ghostscript/9.22/lib/prfont.ps
/usr/share/ghostscript/9.22/lib/printafm.ps
/usr/share/ghostscript/9.22/lib/ps2ai.ps
/usr/share/ghostscript/9.22/lib/ps2epsi.ps
/usr/share/ghostscript/9.22/lib/ras1.upp
/usr/share/ghostscript/9.22/lib/ras24.upp
/usr/share/ghostscript/9.22/lib/ras3.upp
/usr/share/ghostscript/9.22/lib/ras32.upp
/usr/share/ghostscript/9.22/lib/ras4.upp
/usr/share/ghostscript/9.22/lib/ras8m.upp
/usr/share/ghostscript/9.22/lib/rollconv.ps
/usr/share/ghostscript/9.22/lib/s400a1.upp
/usr/share/ghostscript/9.22/lib/s400b1.upp
/usr/share/ghostscript/9.22/lib/sharp.upp
/usr/share/ghostscript/9.22/lib/sipixa6.upp
/usr/share/ghostscript/9.22/lib/st640ih.upp
/usr/share/ghostscript/9.22/lib/st640ihg.upp
/usr/share/ghostscript/9.22/lib/st640p.upp
/usr/share/ghostscript/9.22/lib/st640pg.upp
/usr/share/ghostscript/9.22/lib/st640pl.upp
/usr/share/ghostscript/9.22/lib/st640plg.upp
/usr/share/ghostscript/9.22/lib/stc.upp
/usr/share/ghostscript/9.22/lib/stc1520h.upp
/usr/share/ghostscript/9.22/lib/stc2.upp
/usr/share/ghostscript/9.22/lib/stc200_h.upp
/usr/share/ghostscript/9.22/lib/stc2_h.upp
/usr/share/ghostscript/9.22/lib/stc2s_h.upp
/usr/share/ghostscript/9.22/lib/stc300.upp
/usr/share/ghostscript/9.22/lib/stc300bl.upp
/usr/share/ghostscript/9.22/lib/stc300bm.upp
/usr/share/ghostscript/9.22/lib/stc500p.upp
/usr/share/ghostscript/9.22/lib/stc500ph.upp
/usr/share/ghostscript/9.22/lib/stc600ih.upp
/usr/share/ghostscript/9.22/lib/stc600p.upp
/usr/share/ghostscript/9.22/lib/stc600pl.upp
/usr/share/ghostscript/9.22/lib/stc640p.upp
/usr/share/ghostscript/9.22/lib/stc740ih.upp
/usr/share/ghostscript/9.22/lib/stc800ih.upp
/usr/share/ghostscript/9.22/lib/stc800p.upp
/usr/share/ghostscript/9.22/lib/stc800pl.upp
/usr/share/ghostscript/9.22/lib/stc_h.upp
/usr/share/ghostscript/9.22/lib/stc_l.upp
/usr/share/ghostscript/9.22/lib/stcany.upp
/usr/share/ghostscript/9.22/lib/stcany_h.upp
/usr/share/ghostscript/9.22/lib/stcinfo.ps
/usr/share/ghostscript/9.22/lib/stcolor.ps
/usr/share/ghostscript/9.22/lib/stocht.ps
/usr/share/ghostscript/9.22/lib/traceimg.ps
/usr/share/ghostscript/9.22/lib/traceop.ps
/usr/share/ghostscript/9.22/lib/uninfo.ps
/usr/share/ghostscript/9.22/lib/viewcmyk.ps
/usr/share/ghostscript/9.22/lib/viewgif.ps
/usr/share/ghostscript/9.22/lib/viewjpeg.ps
/usr/share/ghostscript/9.22/lib/viewmiff.ps
/usr/share/ghostscript/9.22/lib/viewpbm.ps
/usr/share/ghostscript/9.22/lib/viewpcx.ps
/usr/share/ghostscript/9.22/lib/viewps2a.ps
/usr/share/ghostscript/9.22/lib/winmaps.ps
/usr/share/ghostscript/9.22/lib/zeroline.ps
/usr/share/man/de/man1/dvipdf.1
/usr/share/man/de/man1/eps2eps.1
/usr/share/man/de/man1/gsnd.1
/usr/share/man/de/man1/pdf2dsc.1
/usr/share/man/de/man1/pdf2ps.1
/usr/share/man/de/man1/printafm.1
/usr/share/man/de/man1/ps2ascii.1
/usr/share/man/de/man1/ps2pdf.1
/usr/share/man/de/man1/ps2pdf12.1
/usr/share/man/de/man1/ps2pdf13.1
/usr/share/man/de/man1/ps2pdf14.1
/usr/share/man/de/man1/ps2ps.1

%files dev
%defattr(-,root,root,-)
/usr/include/ghostscript/gdevdsp.h
/usr/include/ghostscript/gserrors.h
/usr/include/ghostscript/iapi.h
/usr/include/ghostscript/ierrors.h
/usr/lib64/libgs.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgs.so.9
/usr/lib64/libgs.so.9.22
