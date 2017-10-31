How to link from r cran to Version Control
===========================

Not all packages on CRAN have information of their repository.

Some don't have URL field:
```
db.latest_package.findOne({"_source.URL":null})
"Author" : "Scott Fortmann-Roe",
"License" : "GPL (>= 2)",
"Version" : "1.0.0",
"Type" : "Package",
"LinkingTo" : "",
"Date/Publication" : "2015-08-16 23:05:52",
"Description" : "Supplies tools for tabulating and analyzing the results of predictive models. The methods employed are applicable to virtually any predictive model and make comparisons between different methodologies straightforward.",
"Repository" : "CRAN",
"NeedsCompilation" : "no",
"Title" : "Accurate, Adaptable, and Accessible Error Metrics for Predictive\nModels",
"Packaged" : "2015-08-16 14:17:33 UTC; scott",
"Date" : "2015-08-15",
"crandb_file_date" : "2015-08-16 17:08:22",
"releases" : [ ],
"Package" : "A3",
"revdeps" : 1,
"Suggests" : "e1071 (*), randomForest (*), ",
"date" : "2015-08-16T23:05:52+00:00",
"Enhances" : "",
"Maintainer" : "Scott Fortmann-Roe <scottfr@berkeley.edu>",
"Imports" : "",
"Depends" : "xtable (*), R (>= 2.15.0), pbapply (*), "

```

Some have an empty content in their URL field:
```
db.latest_package.findOne({"_source.URL":""})
"Author" : "Michail Tsagris [aut, cre], Giorgos Athineou [aut]",
"Version" : "2.6",
"releases" : [ ],
"Title" : "Compositional Data Analysis",
"NeedsCompilation" : "no",
"LinkingTo" : "",
"Date/Publication" : "2017-10-07 14:30:51 UTC",
"Description" : "Regression, classification, contour plots, hypothesis testing and fitting of distributions for compositional data are some of the functions included.",
"Repository" : "CRAN",
"Authors@R" : "c(person(\"Michail\", \"Tsagris\", role = c(\"aut\", \"cre\"), email = \"mtsagris@yahoo.gr\"),\nperson(\"Giorgos\", \"Athineou\", role = \"aut\", email = \"gioathineou@gmail.com\") )",
"Packaged" : "2017-10-07 11:07:31 UTC; user",
"Date" : "2017-10-07",
"crandb_file_date" : "2017-10-07 14:38:51",
"License" : "GPL (>= 2)",
"Package" : "Compositional",
"URL" : "",
"revdeps" : 1,
"Suggests" : "",
"date" : "2017-10-07T13:30:51+00:00",
"Enhances" : "",
"Maintainer" : "Michail Tsagris <mtsagris@yahoo.gr>",
"Imports" : "emplik (*), foreach (*), parallel (*), sn (*), Rfast (*), stats (*), mixture (*), doParallel (*), MASS (*), fields (*), ",
"MD5sum" : "bcfb1cc878180076eaa53c118cae2ebb",
"Depends" : "R (>= 3.2.2), "

```

Some package on CRAN has A URL, but pointing to web page and not a repository.
```
db.latest_package.findOne({"$and": [{"_source.URL":{$not: /github/}},{"_source.URL":{$exists: true, $ne: ""}}]})
"Author" : "Michael Thrun, Jorn Lotsch, Alfred Ultsch",
"Version" : "1.2.1",
"releases" : [ ],
"NeedsCompilation" : "no",
"LinkingTo" : "",
"Date/Publication" : "2017-03-13 14:31:38",
"Description" : "For a given data set, the package provides a novel method of computing precise limits to acquire subsets which are easily interpreted. Closely related to the Lorenz curve, the ABC curve visualizes the data by graphically representing the cumulative distribution function. Based on an ABC analysis the algorithm calculates, with the help of the ABC curve, the optimal limits by exploiting the mathematical properties pertaining to distribution of analyzed items. The data containing positive values is divided into three disjoint subsets A, B and C, with subset A comprising very profitable values, i.e. largest data values (\"the important few\"), subset B comprising values where the yield equals to the effort required to obtain it, and the subset C comprising of non-profitable values, i.e., the smallest data sets (\"the trivial many\"). Package is based on \"Computed ABC Analysis for rational Selection of most informative Variables in multivariate Data\", PLoS One. Ultsch. A., Lotsch J. (2015) <DOI:10.1371/journal.pone.0129767>.",
"Repository" : "CRAN",
"Type" : "Package",
"Title" : "Computed ABC Analysis",
"Packaged" : "2017-03-13 12:40:55 UTC; mthrun",
"Date" : "2017-03-13",
"crandb_file_date" : "2017-03-13 13:32:49",
"License" : "GPL-3",
"Package" : "ABCanalysis",
"URL" : "https://www.uni-marburg.de/fb12/datenbionik/software-en",
"revdeps" : 1,
"Suggests" : "",
"date" : "2017-03-13T13:31:38+00:00",
"Enhances" : "",
"Maintainer" : "Florian Lerch <lerch@mathematik.uni-marburg.de>",
"Encoding" : "UTF-8",
"Imports" : "plotrix (*), ",
"Depends" : "R (>= 2.10), ",
"LazyLoad" : "yes"
```

Case where github url is not provided but you can find it through BugReports:
----------------------------------------------------------------
```
db.latest_package.findOne({"$and": [{"_source.URL":{$not: /github/}},{"_source.BugReports": /github/}]})
"Author" : "Stéphane Dray <stephane.dray@univ-lyon1.fr>, Anne-Béatrice Dufour <anne-beatrice.dufour@univ-lyon1.fr>, and Jean Thioulouse <jean.thioulouse@univ-lyon1.fr>, with contributions from Thibaut Jombart, Sandrine Pavoine, Jean R. Lobry, Sébastien Ollier, and Aurélie Siberchicot. Based on earlier work by Daniel Chessel.",
"Version" : "1.7-8",
"releases" : [ ],
"NeedsCompilation" : "yes",
"LinkingTo" : "",
"Date/Publication" : "2017-08-09 20:31:18 UTC",
"Description" : "Tools for multivariate data analysis. Several methods are provided for the analysis (i.e., ordination) of one-table (e.g., principal component analysis, correspondence analysis), two-table (e.g., coinertia analysis, redundancy analysis), three-table (e.g., RLQ analysis) and K-table (e.g., STATIS, multiple coinertia analysis). The philosophy of the package is described in Dray and Dufour (2007) <doi:10.18637/jss.v022.i04>.",
"Repository" : "CRAN",
"Title" : "Analysis of Ecological Data : Exploratory and Euclidean Methods\nin Environmental Sciences",
"Packaged" : "2017-08-09 13:05:58 UTC; aurelie",
"Date" : "2017-08-09",
"crandb_file_date" : "2017-08-09 20:38:53",
"License" : "GPL (>= 2)",
"Package" : "ade4",
"URL" : "http://pbil.univ-lyon1.fr/ADE-4, Mailing list:\nhttp://listes.univ-lyon1.fr/wws/info/adelist",
"revdeps" : 39,
"Suggests" : "lattice (*), sp (*), maptools (*), pixmap (*), deldir (*), CircStats (*), ape (*), splancs (*), adegraphics (*), spdep (*), ade4TkGUI (*), MASS (*), adephylo (*), waveslim (*), ",
"date" : "2017-08-09T19:31:18+00:00",
"Enhances" : "",
"Maintainer" : "Aurélie Siberchicot <aurelie.siberchicot@univ-lyon1.fr>",
"Encoding" : "UTF-8",
"Imports" : "methods (*), utils (*), stats (*), grDevices (*), graphics (*), ",
"MD5sum" : "5c792abfafb58b3b77202e1fb725698e",
"Depends" : "R (>= 2.10), ",
"BugReports" : "https://github.com/sdray/ade4/issues"
```

Case where repository is not hosted on github
---------------------------------------------------
```
db.latest_package.findOne({"$and": [{"_source.URL":{$not: /github/}},{"_source.URL": /git/}]})
"Author" : "Gergely Daroczi <daroczig@rapporter.net>",
"License" : "AGPL-3",
"Version" : "1.11.189",
"Type" : "Package",
"LinkingTo" : "",
"Date/Publication" : "2017-09-07 18:33:38 UTC",
"Description" : "Installs the compiled Java modules of the Amazon Web Services ('AWS') 'SDK' to be used in downstream R packages interacting with 'AWS'. See <https://aws.amazon.com/sdk-for-java> for more information on the 'AWS' 'SDK' for Java.",
"Repository" : "CRAN",
"NeedsCompilation" : "no",
"Title" : "'AWS' Java 'SDK' for R",
"Packaged" : "2017-09-06 23:49:11 UTC; daroczig",
"Date" : "2017-09-05",
"crandb_file_date" : "2017-09-07 19:35:52",
"releases" : [ ],
"Package" : "AWR",
"URL" : "https://gitlab.com/daroczig/AWR",
"revdeps" : 1,
"Suggests" : "",
"date" : "2017-09-07T17:33:38+00:00",
"Enhances" : "",
"Maintainer" : "Gergely Daroczi <daroczig@rapporter.net>",
"Imports" : "utils (*), rJava (*), ",
"MD5sum" : "5da7f9f82d36bedea2afc6c7d5a793b1\n",
"Depends" : ""
```

Case where URL web page has a link to repo
--------------------------------------------
```
db.latest_package.findOne({"_source.Package":"RcppStreams"})
"Author" : "Dirk Eddelbuettel <edd@debian.org>",
"Version" : "0.1.1",
"releases" : [ ],
"Type" : "Package",
"NeedsCompilation" : "yes",
"LinkingTo" : "BH (*), Rcpp (*), ",
"Date/Publication" : "2016-08-05 15:11:33",
"Description" : "The 'Streamulus' (template, header-only) library by\nIrit Katriel (at <https://github.com/iritkatriel/streamulus>)\nprovides a very powerful yet convenient framework for stream\nprocessing. This package connects 'Streamulus' to R by providing\nboth the header files and all examples.",
"Repository" : "CRAN",
"RoxygenNote" : "5.0.1",
"Title" : "'Rcpp' Integration of the 'Streamulus' 'DSEL' for Stream\nProcessing",
"Packaged" : "2016-08-05 12:02:51.289261 UTC; edd",
"Date" : "2016-08-05",
"crandb_file_date" : "2016-08-05 09:14:27",
"License" : "GPL (>= 3)",
"Package" : "RcppStreams",
"URL" : "http://dirk.eddelbuettel.com/code/rcpp.streams.html",
"revdeps" : 1,
"Suggests" : "",
"date" : "2016-08-05T15:11:33+00:00",
"Enhances" : "",
"Maintainer" : "Dirk Eddelbuettel <edd@debian.org>",
"Imports" : "Rcpp (*), ",
"Depends" : "R (>= 3.0.0), ",
"BugReports" : "https://github.com/eddelbuettel/rcppstreams/issues"

```
