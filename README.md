# Major_low_ADL_QTL
scripts belonging to major low ADL QTL publication

### Please get in touch if you need help running the scripts on your own data sets: [Hanna Schilbert (email)](mailto:hschilbe@cebitec.uni-bielefeld.de?subject=[GitHub]BnaFLSs_scripts_request) ###

## Usage

### General recommendation

Full paths should be used to specify input and output files and folders. Sequence names should not contain white space characters like spaces and TABs. Underscores can be used to replace spaces.

## assign_read_to_chr.py
This script assigns reads to chromosomes base on a k-mer approach. 

```
Usage:
  python assign_read_to_chr.py --in <FILE> --exp <FILE> --out <DIR>
  
  Mandatory:
  
  Inputs 
  --in     STR     gene IDs, one gene ID per line
  --exp    STR     RNA-Seq count table, columns containing RNA-Seq sample IDs, rows gene IDs
  
  Output directory
  --out    STR     Output directory
  
  Optional:
  --ann    STR     functional annotation file, first column gene IDs, second column functional annotation
```

`--in` txt-file that contains a gene ID or a set of gene IDs for which co-expressed genes should be identified, where one gene ID is listed in one row. The gene ID must match with the gene IDs in the files given at `--exp` and `--ann`.

`--exp` count table/gene expression file containing e.g. the TPM values where the columns contain the RNA-Seq sample IDs and the rows contain the gene IDs. Thus more than one RNA-Seq sample can be analysed at the same time. 

`--out` specify the output directory where the results should be stored

`--ann` functional annotation where one the first column contains gene IDs and the second column contains the functional annotation. Contains a header "Gene_ID\tAnnotation"

All files should be provided in tab separated format.
