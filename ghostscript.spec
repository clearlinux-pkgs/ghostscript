#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : ghostscript
Version  : 10.01.1
Release  : 44
URL      : https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10011/ghostscript-10.01.1.tar.xz
Source0  : https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10011/ghostscript-10.01.1.tar.xz
Summary  : IJS (InkJet Server) Raster Image Transport Protocol
Group    : Development/Tools
License  : AGPL-3.0 Apache-2.0 BSD-2-Clause BSL-1.0 GPL-2.0 GPL-3.0 IJG Libpng MIT libtiff
Requires: ghostscript-bin = %{version}-%{release}
Requires: ghostscript-data = %{version}-%{release}
Requires: ghostscript-lib = %{version}-%{release}
Requires: ghostscript-license = %{version}-%{release}
Requires: ghostscript-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : cups-dev
BuildRequires : dbus-dev
BuildRequires : e2fsprogs-dev
BuildRequires : freeglut-dev
BuildRequires : glu-dev
BuildRequires : gnutls-dev
BuildRequires : grep
BuildRequires : krb5-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(lept)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(libopenjp2)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwebpmux)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xt)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed
BuildRequires : tiff-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
IJS 0.35
News as of 0.35:
11 Feb 2004
The autoconf build system has been moderized and we now use
libtool for portable shared library building. Thanks to Roger
Leigh for helping with that.

%package bin
Summary: bin components for the ghostscript package.
Group: Binaries
Requires: ghostscript-data = %{version}-%{release}
Requires: ghostscript-license = %{version}-%{release}

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
Requires: ghostscript-lib = %{version}-%{release}
Requires: ghostscript-bin = %{version}-%{release}
Requires: ghostscript-data = %{version}-%{release}
Provides: ghostscript-devel = %{version}-%{release}
Requires: ghostscript = %{version}-%{release}

%description dev
dev components for the ghostscript package.


%package doc
Summary: doc components for the ghostscript package.
Group: Documentation
Requires: ghostscript-man = %{version}-%{release}

%description doc
doc components for the ghostscript package.


%package lib
Summary: lib components for the ghostscript package.
Group: Libraries
Requires: ghostscript-data = %{version}-%{release}
Requires: ghostscript-license = %{version}-%{release}

%description lib
lib components for the ghostscript package.


%package license
Summary: license components for the ghostscript package.
Group: Default

%description license
license components for the ghostscript package.


%package man
Summary: man components for the ghostscript package.
Group: Default

%description man
man components for the ghostscript package.


%prep
%setup -q -n ghostscript-10.01.1
cd %{_builddir}/ghostscript-10.01.1
pushd ..
cp -a ghostscript-10.01.1 buildavx2
popd

%build
## build_prepend content
# if this file is missing, configure will fall back to check for system-installed libpng
rm -f libpng/pngread.c
# if these files are missing, configure will fall back to check for system-installed libjpeg
rm -f jpeg/jpeglib.h
rm -f jpeg-6b/jpeglib.h
# if this file is missing, configure will fall back to check for system-installed openjpeg
rm -f openjpeg/src/lib/openjp2/openjpeg.h
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686940848
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --with-system-libtiff \
--without-tesseract
make  %{?_smp_mflags}  all so

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
# if this file is missing, configure will fall back to check for system-installed libpng
rm -f libpng/pngread.c
# if these files are missing, configure will fall back to check for system-installed libjpeg
rm -f jpeg/jpeglib.h
rm -f jpeg-6b/jpeglib.h
# if this file is missing, configure will fall back to check for system-installed openjpeg
rm -f openjpeg/src/lib/openjp2/openjpeg.h
## build_prepend end
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --with-system-libtiff \
--without-tesseract
make  %{?_smp_mflags}  all so
popd
%install
export SOURCE_DATE_EPOCH=1686940848
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ghostscript
cp %{_builddir}/ghostscript-%{version}/contrib/chp2200/COPYING %{buildroot}/usr/share/package-licenses/ghostscript/dfac199a7539a404407098a2541b9482279f690d || :
cp %{_builddir}/ghostscript-%{version}/contrib/lxm3200-tweaked/LICENSE %{buildroot}/usr/share/package-licenses/ghostscript/3bfe807735331dd9d4ce59bc8efe86e2e7fe7b75 || :
cp %{_builddir}/ghostscript-%{version}/cups/LICENSE.txt %{buildroot}/usr/share/package-licenses/ghostscript/4f9df3f6d8b289409ab4ef55e9ca885d8ae1decd || :
cp %{_builddir}/ghostscript-%{version}/doc/COPYING %{buildroot}/usr/share/package-licenses/ghostscript/78e50e186b04c8fe1defaa098f1c192181b3d837 || :
cp %{_builddir}/ghostscript-%{version}/extract/COPYING %{buildroot}/usr/share/package-licenses/ghostscript/78e50e186b04c8fe1defaa098f1c192181b3d837 || :
cp %{_builddir}/ghostscript-%{version}/freetype/docs/GPLv2.TXT %{buildroot}/usr/share/package-licenses/ghostscript/dac7127c82749e3107b53530289e1cd548860868 || :
cp %{_builddir}/ghostscript-%{version}/jbig2dec/COPYING %{buildroot}/usr/share/package-licenses/ghostscript/78e50e186b04c8fe1defaa098f1c192181b3d837 || :
cp %{_builddir}/ghostscript-%{version}/jbig2dec/LICENSE %{buildroot}/usr/share/package-licenses/ghostscript/21c1d4cf3616efc56f2a970d63e9c626a2283ba6 || :
cp %{_builddir}/ghostscript-%{version}/lcms2mt/COPYING %{buildroot}/usr/share/package-licenses/ghostscript/704c75535f661058e8e776ce8112e78db11fdce1 || :
cp %{_builddir}/ghostscript-%{version}/lcms2mt/plugins/fast_float/COPYING.GPL3 %{buildroot}/usr/share/package-licenses/ghostscript/1de7bacb4fbbd7b6d391a69abfe174c2509ec303 || :
cp %{_builddir}/ghostscript-%{version}/lcms2mt/utils/jpgicc/LICENSE_iccjpeg %{buildroot}/usr/share/package-licenses/ghostscript/46e7b80883a260d5531d06126e6bea86daccac9b || :
cp %{_builddir}/ghostscript-%{version}/leptonica/leptonica-license.txt %{buildroot}/usr/share/package-licenses/ghostscript/e0b1dceebde3eb567f610aa97227aa6a5e713810 || :
cp %{_builddir}/ghostscript-%{version}/leptonica/prog/leptonica-license.txt %{buildroot}/usr/share/package-licenses/ghostscript/e0b1dceebde3eb567f610aa97227aa6a5e713810 || :
cp %{_builddir}/ghostscript-%{version}/leptonica/src/leptonica-license.txt %{buildroot}/usr/share/package-licenses/ghostscript/e0b1dceebde3eb567f610aa97227aa6a5e713810 || :
cp %{_builddir}/ghostscript-%{version}/libpng/LICENSE %{buildroot}/usr/share/package-licenses/ghostscript/fc3951ba26fe1914759f605696a1d23e3b41766f || :
cp %{_builddir}/ghostscript-%{version}/libpng/contrib/gregbook/COPYING %{buildroot}/usr/share/package-licenses/ghostscript/80b6f4fcbc19d7431482cba012e86f587828c1ba || :
cp %{_builddir}/ghostscript-%{version}/libpng/contrib/gregbook/LICENSE %{buildroot}/usr/share/package-licenses/ghostscript/aa4b9207aaff26bc16c562d6cd766a9eed49af1e || :
cp %{_builddir}/ghostscript-%{version}/libpng/contrib/pngminus/LICENSE.txt %{buildroot}/usr/share/package-licenses/ghostscript/29883b5b9150592328072643614229f6d320bc6e || :
cp %{_builddir}/ghostscript-%{version}/openjpeg/LICENSE %{buildroot}/usr/share/package-licenses/ghostscript/a1a529b822da257f69972ea711df38489e9d4251 || :
cp %{_builddir}/ghostscript-%{version}/tesseract/LICENSE %{buildroot}/usr/share/package-licenses/ghostscript/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/ghostscript-%{version}/tiff/COPYRIGHT %{buildroot}/usr/share/package-licenses/ghostscript/a2f64f2a85f5fd34bda8eb713c3aad008adbb589 || :
cp %{_builddir}/ghostscript-%{version}/zlib/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/ghostscript/3f317fbb3e08fd99169d2e77105d562ea0e482c7 || :
pushd ../buildavx2/
%make_install_v3 install-so
popd
%make_install install-so
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gs
/V3/usr/bin/gsc
/V3/usr/bin/gsx
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
/usr/share/ghostscript/10.01.1/lib/PDFA_def.ps
/usr/share/ghostscript/10.01.1/lib/PDFX_def.ps
/usr/share/ghostscript/10.01.1/lib/PM760p.upp
/usr/share/ghostscript/10.01.1/lib/PM760pl.upp
/usr/share/ghostscript/10.01.1/lib/PM820p.upp
/usr/share/ghostscript/10.01.1/lib/PM820pl.upp
/usr/share/ghostscript/10.01.1/lib/Stc670p.upp
/usr/share/ghostscript/10.01.1/lib/Stc670pl.upp
/usr/share/ghostscript/10.01.1/lib/Stc680p.upp
/usr/share/ghostscript/10.01.1/lib/Stc680pl.upp
/usr/share/ghostscript/10.01.1/lib/Stc740p.upp
/usr/share/ghostscript/10.01.1/lib/Stc740pl.upp
/usr/share/ghostscript/10.01.1/lib/Stc760p.upp
/usr/share/ghostscript/10.01.1/lib/Stc760pl.upp
/usr/share/ghostscript/10.01.1/lib/Stc777p.upp
/usr/share/ghostscript/10.01.1/lib/Stc777pl.upp
/usr/share/ghostscript/10.01.1/lib/Stp720p.upp
/usr/share/ghostscript/10.01.1/lib/Stp720pl.upp
/usr/share/ghostscript/10.01.1/lib/Stp870p.upp
/usr/share/ghostscript/10.01.1/lib/Stp870pl.upp
/usr/share/ghostscript/10.01.1/lib/acctest.ps
/usr/share/ghostscript/10.01.1/lib/align.ps
/usr/share/ghostscript/10.01.1/lib/bj8.rpd
/usr/share/ghostscript/10.01.1/lib/bj8gc12f.upp
/usr/share/ghostscript/10.01.1/lib/bj8hg12f.upp
/usr/share/ghostscript/10.01.1/lib/bj8oh06n.upp
/usr/share/ghostscript/10.01.1/lib/bj8pa06n.upp
/usr/share/ghostscript/10.01.1/lib/bj8pp12f.upp
/usr/share/ghostscript/10.01.1/lib/bj8ts06n.upp
/usr/share/ghostscript/10.01.1/lib/bjc6000a1.upp
/usr/share/ghostscript/10.01.1/lib/bjc6000b1.upp
/usr/share/ghostscript/10.01.1/lib/bjc610a0.upp
/usr/share/ghostscript/10.01.1/lib/bjc610a1.upp
/usr/share/ghostscript/10.01.1/lib/bjc610a2.upp
/usr/share/ghostscript/10.01.1/lib/bjc610a3.upp
/usr/share/ghostscript/10.01.1/lib/bjc610a4.upp
/usr/share/ghostscript/10.01.1/lib/bjc610a5.upp
/usr/share/ghostscript/10.01.1/lib/bjc610a6.upp
/usr/share/ghostscript/10.01.1/lib/bjc610a7.upp
/usr/share/ghostscript/10.01.1/lib/bjc610a8.upp
/usr/share/ghostscript/10.01.1/lib/bjc610b1.upp
/usr/share/ghostscript/10.01.1/lib/bjc610b2.upp
/usr/share/ghostscript/10.01.1/lib/bjc610b3.upp
/usr/share/ghostscript/10.01.1/lib/bjc610b4.upp
/usr/share/ghostscript/10.01.1/lib/bjc610b6.upp
/usr/share/ghostscript/10.01.1/lib/bjc610b7.upp
/usr/share/ghostscript/10.01.1/lib/bjc610b8.upp
/usr/share/ghostscript/10.01.1/lib/caption.ps
/usr/share/ghostscript/10.01.1/lib/cbjc600.ppd
/usr/share/ghostscript/10.01.1/lib/cbjc800.ppd
/usr/share/ghostscript/10.01.1/lib/cdj550.upp
/usr/share/ghostscript/10.01.1/lib/cdj690.upp
/usr/share/ghostscript/10.01.1/lib/cdj690ec.upp
/usr/share/ghostscript/10.01.1/lib/cid2code.ps
/usr/share/ghostscript/10.01.1/lib/dnj750c.upp
/usr/share/ghostscript/10.01.1/lib/dnj750m.upp
/usr/share/ghostscript/10.01.1/lib/docie.ps
/usr/share/ghostscript/10.01.1/lib/font2pcl.ps
/usr/share/ghostscript/10.01.1/lib/ghostpdf.ppd
/usr/share/ghostscript/10.01.1/lib/gs_ce_e.ps
/usr/share/ghostscript/10.01.1/lib/gs_css_e.ps
/usr/share/ghostscript/10.01.1/lib/gs_il2_e.ps
/usr/share/ghostscript/10.01.1/lib/gs_kanji.ps
/usr/share/ghostscript/10.01.1/lib/gs_ksb_e.ps
/usr/share/ghostscript/10.01.1/lib/gs_l.xbm
/usr/share/ghostscript/10.01.1/lib/gs_l.xpm
/usr/share/ghostscript/10.01.1/lib/gs_l_m.xbm
/usr/share/ghostscript/10.01.1/lib/gs_lgo_e.ps
/usr/share/ghostscript/10.01.1/lib/gs_lgx_e.ps
/usr/share/ghostscript/10.01.1/lib/gs_m.xbm
/usr/share/ghostscript/10.01.1/lib/gs_m.xpm
/usr/share/ghostscript/10.01.1/lib/gs_m_m.xbm
/usr/share/ghostscript/10.01.1/lib/gs_s.xbm
/usr/share/ghostscript/10.01.1/lib/gs_s.xpm
/usr/share/ghostscript/10.01.1/lib/gs_s_m.xbm
/usr/share/ghostscript/10.01.1/lib/gs_t.xbm
/usr/share/ghostscript/10.01.1/lib/gs_t.xpm
/usr/share/ghostscript/10.01.1/lib/gs_t_m.xbm
/usr/share/ghostscript/10.01.1/lib/gs_wl1_e.ps
/usr/share/ghostscript/10.01.1/lib/gs_wl2_e.ps
/usr/share/ghostscript/10.01.1/lib/gs_wl5_e.ps
/usr/share/ghostscript/10.01.1/lib/gslp.ps
/usr/share/ghostscript/10.01.1/lib/gsnup.ps
/usr/share/ghostscript/10.01.1/lib/ht_ccsto.ps
/usr/share/ghostscript/10.01.1/lib/image-qa.ps
/usr/share/ghostscript/10.01.1/lib/jispaper.ps
/usr/share/ghostscript/10.01.1/lib/landscap.ps
/usr/share/ghostscript/10.01.1/lib/lines.ps
/usr/share/ghostscript/10.01.1/lib/mkcidfm.ps
/usr/share/ghostscript/10.01.1/lib/necp2x.upp
/usr/share/ghostscript/10.01.1/lib/necp2x6.upp
/usr/share/ghostscript/10.01.1/lib/pdf2dsc.ps
/usr/share/ghostscript/10.01.1/lib/pdf_info.ps
/usr/share/ghostscript/10.01.1/lib/pf2afm.ps
/usr/share/ghostscript/10.01.1/lib/pfbtopfa.ps
/usr/share/ghostscript/10.01.1/lib/ppath.ps
/usr/share/ghostscript/10.01.1/lib/pphs.ps
/usr/share/ghostscript/10.01.1/lib/prfont.ps
/usr/share/ghostscript/10.01.1/lib/printafm.ps
/usr/share/ghostscript/10.01.1/lib/ps2ai.ps
/usr/share/ghostscript/10.01.1/lib/ps2epsi.ps
/usr/share/ghostscript/10.01.1/lib/ras1.upp
/usr/share/ghostscript/10.01.1/lib/ras24.upp
/usr/share/ghostscript/10.01.1/lib/ras3.upp
/usr/share/ghostscript/10.01.1/lib/ras32.upp
/usr/share/ghostscript/10.01.1/lib/ras4.upp
/usr/share/ghostscript/10.01.1/lib/ras8m.upp
/usr/share/ghostscript/10.01.1/lib/rollconv.ps
/usr/share/ghostscript/10.01.1/lib/s400a1.upp
/usr/share/ghostscript/10.01.1/lib/s400b1.upp
/usr/share/ghostscript/10.01.1/lib/sharp.upp
/usr/share/ghostscript/10.01.1/lib/sipixa6.upp
/usr/share/ghostscript/10.01.1/lib/st640ih.upp
/usr/share/ghostscript/10.01.1/lib/st640ihg.upp
/usr/share/ghostscript/10.01.1/lib/st640p.upp
/usr/share/ghostscript/10.01.1/lib/st640pg.upp
/usr/share/ghostscript/10.01.1/lib/st640pl.upp
/usr/share/ghostscript/10.01.1/lib/st640plg.upp
/usr/share/ghostscript/10.01.1/lib/stc.upp
/usr/share/ghostscript/10.01.1/lib/stc1520h.upp
/usr/share/ghostscript/10.01.1/lib/stc2.upp
/usr/share/ghostscript/10.01.1/lib/stc200_h.upp
/usr/share/ghostscript/10.01.1/lib/stc2_h.upp
/usr/share/ghostscript/10.01.1/lib/stc2s_h.upp
/usr/share/ghostscript/10.01.1/lib/stc300.upp
/usr/share/ghostscript/10.01.1/lib/stc300bl.upp
/usr/share/ghostscript/10.01.1/lib/stc300bm.upp
/usr/share/ghostscript/10.01.1/lib/stc500p.upp
/usr/share/ghostscript/10.01.1/lib/stc500ph.upp
/usr/share/ghostscript/10.01.1/lib/stc600ih.upp
/usr/share/ghostscript/10.01.1/lib/stc600p.upp
/usr/share/ghostscript/10.01.1/lib/stc600pl.upp
/usr/share/ghostscript/10.01.1/lib/stc640p.upp
/usr/share/ghostscript/10.01.1/lib/stc740ih.upp
/usr/share/ghostscript/10.01.1/lib/stc800ih.upp
/usr/share/ghostscript/10.01.1/lib/stc800p.upp
/usr/share/ghostscript/10.01.1/lib/stc800pl.upp
/usr/share/ghostscript/10.01.1/lib/stc_h.upp
/usr/share/ghostscript/10.01.1/lib/stc_l.upp
/usr/share/ghostscript/10.01.1/lib/stcany.upp
/usr/share/ghostscript/10.01.1/lib/stcany_h.upp
/usr/share/ghostscript/10.01.1/lib/stcinfo.ps
/usr/share/ghostscript/10.01.1/lib/stcolor.ps
/usr/share/ghostscript/10.01.1/lib/stocht.ps
/usr/share/ghostscript/10.01.1/lib/traceimg.ps
/usr/share/ghostscript/10.01.1/lib/traceop.ps
/usr/share/ghostscript/10.01.1/lib/uninfo.ps
/usr/share/ghostscript/10.01.1/lib/viewcmyk.ps
/usr/share/ghostscript/10.01.1/lib/viewgif.ps
/usr/share/ghostscript/10.01.1/lib/viewjpeg.ps
/usr/share/ghostscript/10.01.1/lib/viewmiff.ps
/usr/share/ghostscript/10.01.1/lib/viewpbm.ps
/usr/share/ghostscript/10.01.1/lib/viewpcx.ps
/usr/share/ghostscript/10.01.1/lib/viewps2a.ps
/usr/share/ghostscript/10.01.1/lib/winmaps.ps
/usr/share/ghostscript/10.01.1/lib/zeroline.ps

%files dev
%defattr(-,root,root,-)
/usr/include/ghostscript/gdevdsp.h
/usr/include/ghostscript/gserrors.h
/usr/include/ghostscript/iapi.h
/usr/include/ghostscript/ierrors.h
/usr/lib64/libgs.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/ghostscript/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgs.so.10.01
/usr/lib64/libgs.so.10
/usr/lib64/libgs.so.10.01

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ghostscript/1de7bacb4fbbd7b6d391a69abfe174c2509ec303
/usr/share/package-licenses/ghostscript/21c1d4cf3616efc56f2a970d63e9c626a2283ba6
/usr/share/package-licenses/ghostscript/29883b5b9150592328072643614229f6d320bc6e
/usr/share/package-licenses/ghostscript/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/ghostscript/3bfe807735331dd9d4ce59bc8efe86e2e7fe7b75
/usr/share/package-licenses/ghostscript/3f317fbb3e08fd99169d2e77105d562ea0e482c7
/usr/share/package-licenses/ghostscript/46e7b80883a260d5531d06126e6bea86daccac9b
/usr/share/package-licenses/ghostscript/4f9df3f6d8b289409ab4ef55e9ca885d8ae1decd
/usr/share/package-licenses/ghostscript/704c75535f661058e8e776ce8112e78db11fdce1
/usr/share/package-licenses/ghostscript/78e50e186b04c8fe1defaa098f1c192181b3d837
/usr/share/package-licenses/ghostscript/80b6f4fcbc19d7431482cba012e86f587828c1ba
/usr/share/package-licenses/ghostscript/a1a529b822da257f69972ea711df38489e9d4251
/usr/share/package-licenses/ghostscript/a2f64f2a85f5fd34bda8eb713c3aad008adbb589
/usr/share/package-licenses/ghostscript/aa4b9207aaff26bc16c562d6cd766a9eed49af1e
/usr/share/package-licenses/ghostscript/dac7127c82749e3107b53530289e1cd548860868
/usr/share/package-licenses/ghostscript/dfac199a7539a404407098a2541b9482279f690d
/usr/share/package-licenses/ghostscript/e0b1dceebde3eb567f610aa97227aa6a5e713810
/usr/share/package-licenses/ghostscript/fc3951ba26fe1914759f605696a1d23e3b41766f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dvipdf.1
/usr/share/man/man1/eps2eps.1
/usr/share/man/man1/gs.1
/usr/share/man/man1/gsbj.1
/usr/share/man/man1/gsdj.1
/usr/share/man/man1/gsdj500.1
/usr/share/man/man1/gslj.1
/usr/share/man/man1/gslp.1
/usr/share/man/man1/gsnd.1
/usr/share/man/man1/pdf2dsc.1
/usr/share/man/man1/pdf2ps.1
/usr/share/man/man1/pf2afm.1
/usr/share/man/man1/pfbtopfa.1
/usr/share/man/man1/printafm.1
/usr/share/man/man1/ps2ascii.1
/usr/share/man/man1/ps2epsi.1
/usr/share/man/man1/ps2pdf.1
/usr/share/man/man1/ps2pdf12.1
/usr/share/man/man1/ps2pdf13.1
/usr/share/man/man1/ps2pdf14.1
/usr/share/man/man1/ps2pdfwr.1
/usr/share/man/man1/ps2ps.1
