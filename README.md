# Major_low_ADL_QTL
scripts belonging to major low ADL QTL publication

### Please get in touch if you need help running the scripts on your own data sets: [Hanna Schilbert (email)](mailto:hschilbe@cebitec.uni-bielefeld.de?subject=[GitHub]BnaFLSs_scripts_request) ###

## Usage

### General recommendation

Full paths should be used to specify input and output files and folders. Sequence names should not contain white space characters like spaces and TABs. Underscores can be used to replace spaces.

## assign_read_to_chr.py
This script assigns a long-read read to the given chromosomal sequences derived from the A- and the C-genome of Brassica napus. By using the k-mer approach the border sequence of a chimeric read, containing a A- and a C-genome specific sequence part, can be identified. The chimeric read will first be splitted in to k-mers, second each k-mer will be assigned to the A- or C-genome. If a k-mer is present in both subgenomes it will be excluded from further analysis. The number of unique sub-genome specific k-mers per read position will be plotted and stored as PDF. The underlying data of the figure, e.g. position and sequence per analysed k-mer and its subgenome assignment is provided in an additional file.

```
Usage:
  python assign_read_to_chr.py --read <FILE> --refA <FILE> --refA <FILE> --out <DIR>
  
  Mandatory:
  
  Inputs 
  --read    STR     read sequence in FASTA format
  --refA    STR     A-subgenome specific sequence derived from e.g. an assembly file
  --refB    STR     C-subgenome specific sequence derived from e.g. an assembly file

  Output directory
  --out    STR     Output directory
  
  Optional:
  --k    INT     k-mer size, activate k-mer approach
```

`--read` fasta-file that contains the sequence of a lond-read that should be analysed.

`--refA` fasta-file containing the A-subgenome specific sequence which should be used as a subject for the assignment to the A-subgenome. 

`--refB` fasta-file containing the C-subgenome specific sequence which should be used as a subject for the assignment to the C-subgenome. 

`--k` size of the k-mer given as integer.

