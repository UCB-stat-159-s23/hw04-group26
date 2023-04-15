# run everything in the same shell
.ONESHELL:
SHELL:= /bin/bash

# create conda environment
.PHONY: env
env: 
        source /srv/conda/etc/profile.d/conda.sh
        conda env create -f environment.yml
        conda activate ligo

# create html
.PHONY: html
html:
        jupyter notebook build . 
        
# clean sub-folders
.PHONY: clean
clean: 
        rm -rf figures/*
        rm -rf audio/*
        rm -rf _build