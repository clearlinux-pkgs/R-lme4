#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-lme4
Version  : 1.1.35.3
Release  : 120
URL      : https://cran.r-project.org/src/contrib/lme4_1.1-35.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lme4_1.1-35.3.tar.gz
Summary  : Linear Mixed-Effects Models using 'Eigen' and S4
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lme4-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppEigen
Requires: R-minqa
Requires: R-nloptr
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-knitr
BuildRequires : R-minqa
BuildRequires : R-nloptr
BuildRequires : buildreq-R

%description
The models and their components are represented using S4 classes and
    methods.  The core computational algorithms are implemented using the
    'Eigen' C++ library for numerical linear algebra and 'RcppEigen' "glue".

%package lib
Summary: lib components for the R-lme4 package.
Group: Libraries

%description lib
lib components for the R-lme4 package.


%prep
%setup -q -n lme4
pushd ..
cp -a lme4 buildavx2
popd
pushd ..
cp -a lme4 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713371444

%install
export SOURCE_DATE_EPOCH=1713371444
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/lme4/doc/PLSvGLS.R
/usr/lib64/R/library/lme4/doc/PLSvGLS.Rnw
/usr/lib64/R/library/lme4/doc/PLSvGLS.pdf
/usr/lib64/R/library/lme4/doc/Theory.R
/usr/lib64/R/library/lme4/doc/Theory.Rnw
/usr/lib64/R/library/lme4/doc/Theory.pdf
/usr/lib64/R/library/lme4/doc/index.html
/usr/lib64/R/library/lme4/doc/lmer.R
/usr/lib64/R/library/lme4/doc/lmer.Rnw
/usr/lib64/R/library/lme4/doc/lmer.pdf
/usr/lib64/R/library/lme4/doc/lmerperf.R
/usr/lib64/R/library/lme4/doc/lmerperf.Rmd
/usr/lib64/R/library/lme4/doc/lmerperf.html
/usr/lib64/R/library/lme4/help/AnIndex
/usr/lib64/R/library/lme4/help/aliases.rds
/usr/lib64/R/library/lme4/help/lme4.rdb
/usr/lib64/R/library/lme4/help/lme4.rdx
/usr/lib64/R/library/lme4/help/paths.rds
/usr/lib64/R/library/lme4/html/00Index.html
/usr/lib64/R/library/lme4/html/R.css
/usr/lib64/R/library/lme4/testdata/Johnson.rda
/usr/lib64/R/library/lme4/testdata/SO_sep25.RData
/usr/lib64/R/library/lme4/testdata/Thailand.rda
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
/usr/lib64/R/library/lme4/testdata/harmel_density.R
/usr/lib64/R/library/lme4/testdata/harmel_profile.rds
/usr/lib64/R/library/lme4/testdata/hotpower.csv
/usr/lib64/R/library/lme4/testdata/koller-data.R
/usr/lib64/R/library/lme4/testdata/lme-tst-fits.R
/usr/lib64/R/library/lme4/testdata/lme-tst-fits.rda
/usr/lib64/R/library/lme4/testdata/lme-tst-funs.R
/usr/lib64/R/library/lme4/testdata/lmerperf.rda
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
/usr/lib64/R/library/lme4/testdata/strip_env.R
/usr/lib64/R/library/lme4/testdata/survdat_reduced.Rda
/usr/lib64/R/library/lme4/testdata/tprfm1.RData
/usr/lib64/R/library/lme4/testdata/trees513.R
/usr/lib64/R/library/lme4/testdata/trees513.RData
/usr/lib64/R/library/lme4/tests/AAAtest-all.R
/usr/lib64/R/library/lme4/tests/HSAURtrees.R
/usr/lib64/R/library/lme4/tests/README
/usr/lib64/R/library/lme4/tests/REMLdev.R
/usr/lib64/R/library/lme4/tests/ST.R
/usr/lib64/R/library/lme4/tests/agridat_gotway.R
/usr/lib64/R/library/lme4/tests/bootMer.R
/usr/lib64/R/library/lme4/tests/boundary.R
/usr/lib64/R/library/lme4/tests/confint.R
/usr/lib64/R/library/lme4/tests/devCritFun.R
/usr/lib64/R/library/lme4/tests/drop.R
/usr/lib64/R/library/lme4/tests/drop1contrasts.R
/usr/lib64/R/library/lme4/tests/dynload.R
/usr/lib64/R/library/lme4/tests/elston.R
/usr/lib64/R/library/lme4/tests/evalCall.R
/usr/lib64/R/library/lme4/tests/extras.R
/usr/lib64/R/library/lme4/tests/falsezero_dorie.R
/usr/lib64/R/library/lme4/tests/fewlevels.R
/usr/lib64/R/library/lme4/tests/getME.R
/usr/lib64/R/library/lme4/tests/glmer-1.R
/usr/lib64/R/library/lme4/tests/glmerControlPass.R
/usr/lib64/R/library/lme4/tests/glmerWarn.R
/usr/lib64/R/library/lme4/tests/glmmExt.R
/usr/lib64/R/library/lme4/tests/glmmWeights.R
/usr/lib64/R/library/lme4/tests/hatvalues.R
/usr/lib64/R/library/lme4/tests/is.R
/usr/lib64/R/library/lme4/tests/lmList-tst.R
/usr/lib64/R/library/lme4/tests/lme4_nlme.R
/usr/lib64/R/library/lme4/tests/lmer-0.R
/usr/lib64/R/library/lme4/tests/lmer-1.R
/usr/lib64/R/library/lme4/tests/lmer-conv.R
/usr/lib64/R/library/lme4/tests/lmer2_ex.R
/usr/lib64/R/library/lme4/tests/methods.R
/usr/lib64/R/library/lme4/tests/minval.R
/usr/lib64/R/library/lme4/tests/modFormula.R
/usr/lib64/R/library/lme4/tests/nbinom.R
/usr/lib64/R/library/lme4/tests/nlmer-conv.R
/usr/lib64/R/library/lme4/tests/nlmer.R
/usr/lib64/R/library/lme4/tests/offset.R
/usr/lib64/R/library/lme4/tests/optimizer.R
/usr/lib64/R/library/lme4/tests/polytomous.R
/usr/lib64/R/library/lme4/tests/prLogistic.R
/usr/lib64/R/library/lme4/tests/predict_basis.R
/usr/lib64/R/library/lme4/tests/predsim.R
/usr/lib64/R/library/lme4/tests/priorWeights.R
/usr/lib64/R/library/lme4/tests/priorWeightsModComp.R
/usr/lib64/R/library/lme4/tests/profile-tst.R
/usr/lib64/R/library/lme4/tests/refit.R
/usr/lib64/R/library/lme4/tests/resids.R
/usr/lib64/R/library/lme4/tests/respiratory.R
/usr/lib64/R/library/lme4/tests/simulate.R
/usr/lib64/R/library/lme4/tests/test-glmernbref.R
/usr/lib64/R/library/lme4/tests/testOptControl.R
/usr/lib64/R/library/lme4/tests/testcolonizer.R
/usr/lib64/R/library/lme4/tests/testcrab.R
/usr/lib64/R/library/lme4/tests/testthat/test-NAhandling.R
/usr/lib64/R/library/lme4/tests/testthat/test-allFit.R
/usr/lib64/R/library/lme4/tests/testthat/test-catch.R
/usr/lib64/R/library/lme4/tests/testthat/test-doubleVertNotation.R
/usr/lib64/R/library/lme4/tests/testthat/test-eval.R
/usr/lib64/R/library/lme4/tests/testthat/test-factors.R
/usr/lib64/R/library/lme4/tests/testthat/test-formulaEval.R
/usr/lib64/R/library/lme4/tests/testthat/test-glmFamily.R
/usr/lib64/R/library/lme4/tests/testthat/test-glmer.R
/usr/lib64/R/library/lme4/tests/testthat/test-glmernb.R
/usr/lib64/R/library/lme4/tests/testthat/test-glmernbref.R
/usr/lib64/R/library/lme4/tests/testthat/test-glmmFail.R
/usr/lib64/R/library/lme4/tests/testthat/test-lmList.R
/usr/lib64/R/library/lme4/tests/testthat/test-lmer.R
/usr/lib64/R/library/lme4/tests/testthat/test-lmerResp.R
/usr/lib64/R/library/lme4/tests/testthat/test-methods.R
/usr/lib64/R/library/lme4/tests/testthat/test-nbinom.R
/usr/lib64/R/library/lme4/tests/testthat/test-nlmer.R
/usr/lib64/R/library/lme4/tests/testthat/test-oldRZXfailure.R
/usr/lib64/R/library/lme4/tests/testthat/test-predict.R
/usr/lib64/R/library/lme4/tests/testthat/test-ranef.R
/usr/lib64/R/library/lme4/tests/testthat/test-rank.R
/usr/lib64/R/library/lme4/tests/testthat/test-resids.R
/usr/lib64/R/library/lme4/tests/testthat/test-simulate_formula.R
/usr/lib64/R/library/lme4/tests/testthat/test-start.R
/usr/lib64/R/library/lme4/tests/testthat/test-stepHalving.R
/usr/lib64/R/library/lme4/tests/testthat/test-summary.R
/usr/lib64/R/library/lme4/tests/testthat/test-utils.R
/usr/lib64/R/library/lme4/tests/throw.R
/usr/lib64/R/library/lme4/tests/varcorr.R
/usr/lib64/R/library/lme4/tests/vcov-etc.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/lme4/libs/lme4.so
/V4/usr/lib64/R/library/lme4/libs/lme4.so
/usr/lib64/R/library/lme4/libs/lme4.so
