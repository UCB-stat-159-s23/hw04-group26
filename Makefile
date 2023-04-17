# run everything in the same shell
.ONESHELL:
SHELL:= /bin/bash

# create conda environment
.PHONY: env
env: 
        source /srv/conda/etc/profile.d/conda.sh
        conda env create -f environment.yml
        conda activate ligo
        conda activate notebook
        conda install ipykernel
        python -m ipykernel install --user --name make-env --display-name "IPython - Make"

# create html
.PHONY: html
html:
        jupyter notebook build . 
        
# clean sub-folders
.PHONY: clean
clean: 
        rm -f figures/*
        rm -f audio/*
        rm -r _build/*