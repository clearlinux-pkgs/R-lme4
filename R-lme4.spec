#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lme4
Version  : 1.1.13
Release  : 36
URL      : http://cran.r-project.org/src/contrib/lme4_1.1-13.tar.gz
Source0  : http://cran.r-project.org/src/contrib/lme4_1.1-13.tar.gz
Summary  : Linear Mixed-Effects Models using 'Eigen' and S4
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lme4-lib
Requires: R-Rcpp
Requires: R-RcppEigen
Requires: R-ggplot2
Requires: R-minqa
Requires: R-nloptr
Requires: R-pbkrtest
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-ggplot2
BuildRequires : R-knitr
BuildRequires : R-minqa
BuildRequires : R-nloptr
BuildRequires : R-pbkrtest
BuildRequires : clr-R-helpers

%description
Catalog of currently-failing examples (commented out, testsx, etc.):
glmmExt.R: "fail for MM" on Gaussian/inverse examples -- seems fine for me
lmer-0.R: sstudy9 example.  Should *not* work; is a meaningful error message possible?
prLogistic.R: Thailand/clustered-data example from ?prLogisticDelta example in prLogistic package
Presumably the problem is that 100/411 random-effect levels have only zeros -- but should this mess things up?
glmmML and lme4.0 give nearly identical answers

%package lib
Summary: lib components for the R-lme4 package.
Group: Libraries

%description lib
lib components for the R-lme4 package.


%prep
%setup -q -c -n lme4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492800189

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492800189
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lme4
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library lme4 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lme4/CITATION
/usr/lib64/R/library/lme4/DESCRIPTION
/usr/lib64/R/library/lme4/INDEX
/usr/lib64/R/library/lme4/Meta/Rd.rds
/usr/lib64/R/library/lme4/Meta/data.rds
/usr/lib64/R/library/lme4/Meta/features.rds
/usr/lib64/R/library/lme4/Meta/hsearch.rds
/usr/lib64/R/library/lme4/Meta/links.rds
/usr/lib64/R/library/lme4/Meta/nsInfo.rds
/usr/lib64/R/library/lme4/Meta/package.rds
/usr/lib64/R/library/lme4/Meta/vignette.rds
/usr/lib64/R/library/lme4/NAMESPACE
/usr/lib64/R/library/lme4/NEWS.Rd
/usr/lib64/R/library/lme4/R/lme4
/usr/lib64/R/library/lme4/R/lme4.rdb
/usr/lib64/R/library/lme4/R/lme4.rdx
/usr/lib64/R/library/lme4/R/sysdata.rdb
/usr/lib64/R/library/lme4/R/sysdata.rdx
/usr/lib64/R/library/lme4/data/Rdata.rdb
/usr/lib64/R/library/lme4/data/Rdata.rds
/usr/lib64/R/library/lme4/data/Rdata.rdx
/usr/lib64/R/library/lme4/doc/Doxyfile
/usr/lib64/R/library/lme4/doc/PLSvGLS.pdf
/usr/lib64/R/library/lme4/doc/Theory.pdf
/usr/lib64/R/library/lme4/doc/index.html
/usr/lib64/R/library/lme4/doc/lme4-extras.pdf
/usr/lib64/R/library/lme4/doc/lmer.pdf
/usr/lib64/R/library/lme4/doc/lmerperf.html
/usr/lib64/R/library/lme4/doc/profiling.txt
/usr/lib64/R/library/lme4/help/AnIndex
/usr/lib64/R/library/lme4/help/aliases.rds
/usr/lib64/R/library/lme4/help/lme4.rdb
/usr/lib64/R/library/lme4/help/lme4.rdx
/usr/lib64/R/library/lme4/help/paths.rds
/usr/lib64/R/library/lme4/html/00Index.html
/usr/lib64/R/library/lme4/html/R.css
/usr/lib64/R/library/lme4/libs/symbols.rds
/usr/lib64/R/library/lme4/testdata/Johnson.rda
/usr/lib64/R/library/lme4/testdata/SO_sep25.RData
/usr/lib64/R/library/lme4/testdata/Thailand.rda
/usr/lib64/R/library/lme4/testdata/badhess.RData
/usr/lib64/R/library/lme4/testdata/badprof.rds
/usr/lib64/R/library/lme4/testdata/boo01L.RData
/usr/lib64/R/library/lme4/testdata/colonizer_rand.rda
/usr/lib64/R/library/lme4/testdata/confint_ex.rda
/usr/lib64/R/library/lme4/testdata/crabs_randdata00.Rda
/usr/lib64/R/library/lme4/testdata/crabs_randdata2.Rda
/usr/lib64/R/library/lme4/testdata/culcita_dat.RData
/usr/lib64/R/library/lme4/testdata/dat20101314.csv
/usr/lib64/R/library/lme4/testdata/dataEx_Glmer.txt
/usr/lib64/R/library/lme4/testdata/fakesim.RData
/usr/lib64/R/library/lme4/testdata/gopherdat2.RData
/usr/lib64/R/library/lme4/testdata/gotway_hessianfly.rda
/usr/lib64/R/library/lme4/testdata/hotpower.csv
/usr/lib64/R/library/lme4/testdata/koller-data.R
/usr/lib64/R/library/lme4/testdata/lme-tst-fits.R
/usr/lib64/R/library/lme4/testdata/lme-tst-fits.rda
/usr/lib64/R/library/lme4/testdata/lme-tst-funs.R
/usr/lib64/R/library/lme4/testdata/mastitis.rda
/usr/lib64/R/library/lme4/testdata/polytom2.RData
/usr/lib64/R/library/lme4/testdata/polytom3.RData
/usr/lib64/R/library/lme4/testdata/polytomous_test.RData
/usr/lib64/R/library/lme4/testdata/polytomous_vcov_ex.RData
/usr/lib64/R/library/lme4/testdata/prLogistic.RData
/usr/lib64/R/library/lme4/testdata/radinger_dat.RData
/usr/lib64/R/library/lme4/testdata/rankMatrix.rds
/usr/lib64/R/library/lme4/testdata/respiratory.RData
/usr/lib64/R/library/lme4/testdata/sbTobb.Rdata
/usr/lib64/R/library/lme4/testdata/survdat_reduced.Rda
/usr/lib64/R/library/lme4/testdata/tprfm1.RData
/usr/lib64/R/library/lme4/testdata/trees513.R
/usr/lib64/R/library/lme4/testdata/trees513.RData
/usr/lib64/R/library/lme4/utils/allFit.R
/usr/lib64/R/library/lme4/vignettedata/calcium.txt
/usr/lib64/R/library/lme4/vignettedata/mcmcsampdat.RData

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lme4/libs/lme4.so
