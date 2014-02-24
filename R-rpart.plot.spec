%define debug_package %{nil}
%global packname  rpart.plot
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4.4
Release:          1
Summary:          Plot rpart models.  An enhanced version of plot.rpart
Group:            Sciences/Mathematics
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/rpart.plot_1.4-4.tar.gz
Requires:         R-rpart 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-rpart

%description
Plot rpart models. Extends plot.rpart and text.rpart in the rpart package.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
#%{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
# %{rlibdir}/%{packname}/libs
%{rlibdir}/rpart.plot/slowtests/README.txt
%{rlibdir}/rpart.plot/slowtests/code.in.rpart.report.with.prp.R
%{rlibdir}/rpart.plot/slowtests/data.stagec
%{rlibdir}/rpart.plot/slowtests/make.bat
%{rlibdir}/rpart.plot/slowtests/test.prp.R
%{rlibdir}/rpart.plot/slowtests/test.prp.Rout.save
%{rlibdir}/rpart.plot/slowtests/test.prp.save.ps
%{rlibdir}/rpart.plot/slowtests/user-manual-figs.R


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2_2-1
+ Revision: 777619
- Import R-rpart.plot
- Import R-rpart.plot



