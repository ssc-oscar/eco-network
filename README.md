# eco-network
For investigating ecosystem networks

Ember_Cran_Summary.ipynb:
------------------------
### Data sources:   

Ember Eco (defined as package name *ember*) dependency is retrieved using
```
npm view --json <package> 
```
for upstream (using "dependencies" dictionary, not "devDependencies" or "optDependencies") and 
```
deppkgs <package>
```
for downstream.

Only ember packages with github repo in the npms are included (to ensure that authorship network 
is also obtainable).

Ember Eco authorship linked package is built on top of data retrieved from npms.
First, authors of all *ember* packages are retrieved and for each author a list of 
packages they authored or maintaind is retrieved from NPMS. 

R _CRAN
-------

R CRAN dependency is built from data retrieved from libraries.io (dependencies*csv).
As a result, packages with no upstream dependencies are omitted (are not in libraries.io).

R CRAN authorship package network is built from data retrieved from META CRAN


### Script locations(all on da4 server):

- scripts to generate ember eco dependency:
  - /data/play/script_dealing_ember_dependency/direct_dependencynew.py
  - /data/play/script_dealing_ember_dependency/recursive_downstreams.py
  - /data/play/script_dealing_ember_dependency/recursive_upstreams.py
  - /data/play/script_dealing_ember_dependency/seperate_InOutEco.py  


- scripts to generate ember eco authorship linked network:  
  - /data/play/script_dealing_ember_dependency/authorship_network_for_emberECO.py


- scripts to generate R CRAN authorship linked network:
  - /data/play/script_dealing_R_CRAN_repo/scrape_downR_CRAN_pack_name.py rerieve list of R package names
  - /data/play/script_dealing_R_CRAN_repo/elasticcc.py rerieve R package info from META CRAN
  - /data/play/script_dealing_R_CRAN_repo/parse_auth_email.py generate R CRAN authorship linked network


- scripts to generate R CRAN dependency:
  - /data/play/script_dealing_dependency/downstream_R_CRAN.py
  - /data/play/script_dealing_dependency/upstream_R_CRAN.py
  - In order to parse the dependency requirement field correctly, python package  <semantic_version> is revised to fit R CRAN.

- script /data/play/script_dealing_ember_dependency/generate_data_for_summary.py generate data for R boxplot.

**Notice**: I've changed python file names slightly in code folder in order to make it more comprehensible.
### Data locations(all on da4 server):

- Ember eco dependencies -- **/data/play/Ember_ECO_data/[direct_downstream,direct_upstream,recursive_downstreams,recursive_upstreams][.In,.Out]?**  
 containing 2 columns(seperated by ';'): first field is package name, second is its correlated packages list
- Ember eco authorship linked package network -- **/data/play/Ember_ECO_data/ECOpackage2otherpackagesThu[au,ma]**  
 One network is built through author, the other through maintainer. The data format follows the same structure as eco dependency data mentioned above.
- R CRAN dependencies -- **/data/play/libraries.io.depens/R_CRAN_[direct_upstream,downstream_direct,upstream_recurs,downstream_recurs]_noV**  
 (same format but has different versions for each package)
- R CRAN authorship linked package network -- **/data/play/R_CRAN_data/package2otherpackages.THRU.[au,ma]**  
(same format as Ember eco)
