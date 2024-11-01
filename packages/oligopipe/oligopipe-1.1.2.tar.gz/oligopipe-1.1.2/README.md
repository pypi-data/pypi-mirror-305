# oligopipe - Python package for Oligogenic Variant Analysis pipelines

This package offers a command-line interface to the Oligogenic Variant Analysis pipelines 
developed at the [Interuniversity Institute of Bioinformatics in Brussels](https://ibsquare.be).

It contains two modules:
* **prediction with VarCoPP2.0**, as discussed in the paper “[Faster and more accurate pathogenic combination predictions with VarCoPP2.0](https://doi.org/10.1186/s12859-023-05291-3)":
  
   takes a patient's variants from VCF/TSV along with additional parameters and predicts the pathogenicity of all digenic variant combinations. 

* **prioritization with HOP**, as discussed in the paper "[Prioritization of oligogenic variant combinations in whole exomes](https://doi.org/10.1093/bioinformatics/btae184)":
      
   takes a patient's variants from VCF/TSV along with information about the patient's disease (HPO terms or a gene panel) and ranks variant combinations based on how likely they are to cause the patient's disease. 



## Requirements

The package requires Python 3.8-3.10 (currently higher versions are not supported yet). 

Additional requirements are specified in the `requirements.txt` file and automatically satisfied when installing with `pip`.

## Installation

### PIP-based installation

The easiest way to install is via the [PyPI archive](https://pypi.org/project/oligopipe/) with the command

    pip install oligopipe

It is recommended to use a virtual environment for the management of dependencies.

### Source-based installation

The source code can be installed by cloning the repository or unpacking from a source code archive and running

    pip install .

in the source directory.

For the purposes of testing or development, you may prefer to install as an editable module via PIP by running

    pip install -e .

in the source directory.

## Usage

Running `oligopipe` without any arguments or with `--help` returns the overview of the CLI:

    $ oligopipe
    usage: oligopipe [-h] {predict,prioritize,config} ...
    
    CLI for oligopipe - oligogenic variant analysis pipelines
    
    optional arguments:
      -h, --help            show this help message and exit
    
    Commands:
      Run oligopipe {command} -h to get detailed help
    
      {predict,prioritize,config}
        predict             Run a VarCoPP prediction
        prioritize          Run a prioritization analysis with HOP -- under construction
        config              Show the template config file


The individual pipelines are available as submodules of the CLI, and also have dedicated help pages.

Both modules allow using a YAML config file for submitting input parameters and file paths, 
as well as passing them as command-line arguments (which will be favored if both are given). 
Running the `oligopipe config` module will print out a template for that config file.

### Running a prediction

Please refer to [the docs](https://oligogenic.github.io/oligopipe-docs/) for extensive documentation on the pipeline logic, the expected inputs and outputs.

Check the available arguments:

    $ oligopipe predict --help

The input arguments are grouped in categories:
* **Variant input**: VCF or TSV file and genome build (both required), patient's sex
* **Filtering options**
* **Output options**
* **Database credentials** (required; see below)

An example prediction run could then look like this (with database credentials in the config file):

    $ oligopipe predict --config path/to/input_config.yaml \
                        --variants-vcf path/to/example_vcf_2_hg19.vcf --genome-build hg19 --patient-sex F \
                        --panel path/to/example_vcf_2_gene_panel.txt \
                        --outdir results 

Which will create the following result files:
* `metadata.json`: summary of the pipeline run (inputs, statistics)
* `predictions_with_annotations.json`: "raw" output of the predictions, containing also feature annotations 
* `predicted_variant_combinations.tsv`: table of variant combinations with their predictions
* `predicted_gene_pairs.tsv`: table of gene pairs with prediction statistics
* one file per type of variants that were discarded by the pipeline (if applicable):
  * `filtered_variants.txt`
  * `missing_variants.txt` (missing from the annotation database)
  * `invalid_zygosity_variants.txt`

**Note**: if no variant combinations remain after the filtering, then the gene pair/variant combination files are not created

### Running a prioritization
Not available yet

### Annotation database
The pipelines rely on an annotation database for quick retrieval of the variant, gene and gene pair input features for VarCoPP.

We currently offer limited access to such a database for use in this package. 
If you wish to get access, please [email us](mailto:oligopipe@ibsquare.be) so that we can provide you with the credentials.


## Additional documentation

Extensive documentation (and a FAQ page) about the pipelines can be found in [the docs](https://oligogenic.github.io/oligopipe-docs/).

## Citations

Prediction with VarCoPP(2.0):
* **Versbraegen N., Gravel B., Nachtegael C., Renaux A., Verkinderen E., Nowé A., Lenaerts T., Papadimitriou S.** (2023) Faster and more accurate pathogenic combination predictions with VarCoPP2.0. _BMC Bioinformatics_. 24:179. DOI: [https://doi.org/10.1186/s12859-023-05291-3]()
* **Papadimitriou S., Gazzo A., Versbraegen N., Nachtegael C., Aerts J., Moreau Y., Van Dooren S., Nowé A., Smits G., Lenaerts T.** (2019) Predicting disease-causing variant combinations. _Proceedings of the National Academy of Sciences_. 116(24):11878-11887. DOI: [https://doi.org/10.1073/pnas.1815601116]()

Prioritization with HOP:
* **Gravel B., Renaux A., Papadimitriou S., Smits G., Nowé A., Lenaerts T.** (2024) Prioritization of oligogenic variant combinations in whole exomes. _Bioinformatics_. Volume 40, Issue 4, April 2024, btae184. DOI: [https://doi.org/10.1093/bioinformatics/btae184]()



## Support

If you are having issues, please let us know via [oligopipe@ibsquare.be](mailto:oligopipe@ibsquare.be).

### Known issues
If you run `oligopipe` on a Macbook with M1 chip, you might get errors related to dependencies `psycopg2` and `python-magic`.
Try to resolve them by running:
* `pip uninstall psycopg2` and then `pip install psycopg2-binary`
* `pip install python-magic-bin`

## License

The package is licensed under the MIT license.
