#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lme4
Version  : 1.1
Release  : 18
URL      : http://cran.r-project.org/src/contrib/lme4_1.1-7.tar.gz
Source0  : http://cran.r-project.org/src/contrib/lme4_1.1-7.tar.gz
Summary  : Linear mixed-effects models using Eigen and S4
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RcppEigen
Requires: R-Rcpp
Requires: R-nloptr
Requires: R-minqa
Requires: R-ggplot2
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-ggplot2
BuildRequires : R-knitr
BuildRequires : R-minqa
BuildRequires : R-nloptr
BuildRequires : clr-R-helpers

%description
Catalog of currently-failing examples (commented out, testsx, etc.):
glmmExt.R: "fail for MM" on Gaussian/inverse examples -- seems fine for me
lmer-0.R: sstudy9 example.  Should *not* work; is a meaningful error message possible?
prLogistic.R: Thailand/clustered-data example from ?prLogisticDelta example in prLogistic package
Presumably the problem is that 100/411 random-effect levels have only zeros -- but should this mess things up?
glmmML and lme4.0 give nearly identical answers

%prep
%setup -q -c -n lme4

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library lme4
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library lme4 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lme4/CITATION
/usr/lib64/R/library/lme4/DESCRIPTION
/usr/lib64/R/library/lme4/INDEX
/usr/lib64/R/library/lme4/Meta/Rd.rds
/usr/lib64/R/library/lme4/Meta/data.rds
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
/usr/lib64/R/library/lme4/data/Rdata.rdb
/usr/lib64/R/library/lme4/data/Rdata.rds
/usr/lib64/R/library/lme4/data/Rdata.rdx
/usr/lib64/R/library/lme4/doc/Doxyfile
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
/usr/lib64/R/library/lme4/doc/profiling.txt
/usr/lib64/R/library/lme4/help/AnIndex
/usr/lib64/R/library/lme4/help/aliases.rds
/usr/lib64/R/library/lme4/help/lme4.rdb
/usr/lib64/R/library/lme4/help/lme4.rdx
/usr/lib64/R/library/lme4/help/paths.rds
/usr/lib64/R/library/lme4/html/00Index.html
/usr/lib64/R/library/lme4/html/R.css
/usr/lib64/R/library/lme4/libs/lme4.so
/usr/lib64/R/library/lme4/libs/symbols.rds
/usr/lib64/R/library/lme4/testdata/Johnson.rda
/usr/lib64/R/library/lme4/testdata/SO_sep25.RData
/usr/lib64/R/library/lme4/testdata/Thailand.rda
/usr/lib64/R/library/lme4/testdata/boo01L.RData
/usr/lib64/R/library/lme4/testdata/colonizer_rand.rda
/usr/lib64/R/library/lme4/testdata/confint_ex.rda
/usr/lib64/R/library/lme4/testdata/crabs_randdata00.Rda
/usr/lib64/R/library/lme4/testdata/crabs_randdata2.Rda
/usr/lib64/R/library/lme4/testdata/culcita_dat.RData
/usr/lib64/R/library/lme4/testdata/dat20101314.csv
/usr/lib64/R/library/lme4/testdata/gopherdat2.RData
/usr/lib64/R/library/lme4/testdata/gotway_hessianfly.rda
/usr/lib64/R/library/lme4/testdata/hotpower.csv
/usr/lib64/R/library/lme4/testdata/koller-data.R
/usr/lib64/R/library/lme4/testdata/lme-tst-fits.R
/usr/lib64/R/library/lme4/testdata/lme-tst-fits.Rout
/usr/lib64/R/library/lme4/testdata/lme-tst-fits.rda
/usr/lib64/R/library/lme4/testdata/lme-tst-funs.R
/usr/lib64/R/library/lme4/testdata/mastitis.rda
/usr/lib64/R/library/lme4/testdata/polytom2.RData
/usr/lib64/R/library/lme4/testdata/polytom3.RData
/usr/lib64/R/library/lme4/testdata/polytomous_test.RData
/usr/lib64/R/library/lme4/testdata/polytomous_vcov_ex.RData
/usr/lib64/R/library/lme4/testdata/prLogistic.RData
/usr/lib64/R/library/lme4/testdata/radinger_dat.RData
/usr/lib64/R/library/lme4/testdata/rankMatrix.rda
/usr/lib64/R/library/lme4/testdata/respiratory.RData
/usr/lib64/R/library/lme4/testdata/survdat_reduced.Rda
/usr/lib64/R/library/lme4/testdata/tprfm1.RData
/usr/lib64/R/library/lme4/testdata/trees513.R
/usr/lib64/R/library/lme4/testdata/trees513.RData
/usr/lib64/R/library/lme4/tests/Rplots.pdf
/usr/lib64/R/library/lme4/tests/napredict2.R
/usr/lib64/R/library/lme4/tests/test-NAhandling.R
/usr/lib64/R/library/lme4/tests/test-catch.R
/usr/lib64/R/library/lme4/tests/test-doubleVertNotation.R
/usr/lib64/R/library/lme4/tests/test-factors.R
/usr/lib64/R/library/lme4/tests/test-formulaEval.R
/usr/lib64/R/library/lme4/tests/test-glmFamily.R
/usr/lib64/R/library/lme4/tests/test-glmer.R
/usr/lib64/R/library/lme4/tests/test-glmer.Rout
/usr/lib64/R/library/lme4/tests/test-glmmFail.R
/usr/lib64/R/library/lme4/tests/test-lmer.R
/usr/lib64/R/library/lme4/tests/test-lmerResp.R
/usr/lib64/R/library/lme4/tests/test-methods.R
/usr/lib64/R/library/lme4/tests/test-oldRZXfailure.R
/usr/lib64/R/library/lme4/tests/test-rank.R
/usr/lib64/R/library/lme4/tests/test-resids.R
/usr/lib64/R/library/lme4/tests/test-start.R
/usr/lib64/R/library/lme4/tests/test-stepHalving.R
/usr/lib64/R/library/lme4/tests/test-summary.R
/usr/lib64/R/library/lme4/tests/test-utils.R
/usr/lib64/R/library/lme4/tests/tmp.html
/usr/lib64/R/library/lme4/tests/wenseleers.rda
/usr/lib64/R/library/lme4/vignettedata/calcium.txt
/usr/lib64/R/library/lme4/vignettedata/mcmcsampdat.RData
