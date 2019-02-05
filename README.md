# Ultrafast_Variant_Ranking
Ultrafast Variant Ranking for Cancer and Beyond!

Goal: To enhance the annotation of noncoding variation in support of massively parallel reporter assays, including the generation of short nucleotide sequences to use experimentally. 

## Introduction 

Open-CRAVAT is a python package that performs genomic variant interpretation. The modular and locally-installed command-line or GUI interface allows for  annoations of gene- and variant-level impact, interactions, conservation, and scoring. In this work, we advance the platform to assist in the interrogation of genetic variation via massively parallel reporter assays (MPRAs). 

MPRAs are used to validate DNA nucleotides for their regulatory roles. MPRAs are one of the functional assays used to validate cis regulatory elements for their enhancer/silencer like activity. Both MPRAs and a similar assay called STARR-seq (self-transcribing active regulatory region sequencing) use short nucleotide sequences (100-400bp) to functionaly validate regulatory variants. 

## Workflow![alt text](asd2.png)

## Goals 
  
* We will add functionality for variant input via dbSNP identifiers (rsids). 
* For users that have run GATK ReadBackedPhasing, the tool will now automatically generate haplotype block annotations. 
* Module to generate short sequences to be used in MPRA  

## Dependencies 

* Open-CRAVAT https://github.com/KarchinLab/open-cravat/wiki 
* Python 3+ https://www.python.org/download/releases/3.0/
* GATK ReadBackedPhasing https://software.broadinstitute.org/gatk/documentation/tooldocs/3.8-0/org_broadinstitute_gatk_tools_walkers_phasing_ReadBackedPhasing.php

## Resources utilized
 
* dbSNP identifiers 
* Promoter capture hic processed data for 17 human primary blood cell types DOI:https://doi.org/10.1016/j.cell.2016.09.037

## Participants

Kymberleigh Pagel, Johns Hopkins University, Baltimore MD, kpagel1@jhu.edu <br>
Kyle Moad, In Silico Solutions, Falls Church VA, kmoad@insilico.us.com <br>
Mary Wood, Portland VA Research Foundation and Oregon Health and Science University, Portland OR, mary.a.wood.91@gmail.com <br>
Arpit Mishra, University of Washington, Seattle, arpitm@uw.edu <br>
