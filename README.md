#  OriC-ENS: A Sequence-Based Ensemble Classifier for Predicting Origin of Replication in S. cerevisiae.

### Abstract
To be added
### [1]. Read File:
All the datasets file are in `FASTA` format which can be with `.txt` or `.fasta` extension. E.g. `anyName.txt` or  `anyName.fasta`. Please know more about the FASTA file format [by clicking here!](https://en.wikipedia.org/wiki/FASTA_format).

```
>1AKHA|1
KKEKSPKGKSSISPQARAFLEEVFRRKQSLNSKEKEEVAKKCGITPLQVRVWFINKRMRSK
>1AOII|1
ATCAATATCCACCTGCAGATTCTACCAAAAGTGTATTTGGAAACTGCTCCATCAAAAGGCATGTTCAGCTGAATTCAGCTGAACATGCCTTTTGATGGAGCAGTTTCCAAATACACTTTTGGTAGAATCTGCAGGTGGATATTGAT
>1B6WA|1
MELPIAPIGRIIKDAGAERVSDDARITLAKILEEMGRDIASEAIKLARHAGRKTIKAEDIELAVRRFK
```

### [2]. Feature Generation:

#### Proper explanation of features: 
K is an integer number representation of feature N. For example k=3 means the number of nucleotides ranging from 1 to 3 inclusive.
kGap is an integer number representation of gap count in feature N. For example k=5 means the number of gaps ranging from 1 to 5 inclusive.

**Table 1:**  DNA dataset feature extraction

| Features  | Type  | Number of features  | Feature Structure  | Explanation  |
| --------- | ----- | ------------------- | ------------------ | ------------ |
| 1 | Monomer Composition  | 4  | N | when K=1, 4 features for DNA/RNA | 
| 2 | Dipeptide Composition  | 16  | NN | when K=2, 4\*4=16 features for DNA/RNA | 
| 3 | Tripeptide Composition  | 64  | NNN | when K=3, 4\*4\*4=64 features for DNA/RNA | 
| 4 | K-gapped Di-mono Composition  | 64  | NN_N | when KGap=1, 64 features for DNA/RNA |
| 5 | K-gapped Mono-Di Composition  | 64  | N_NN | when KGap=1, 64 features for DNA/RNA |
|  | **Total**  | **212**  |  |  |

**Note:** For DNA sequences N = {A,C,G,T}


### [3]. How to Run Package:

#### [3.1] Test Command-line #1: Without Feature Selection
```console
user@machine:~$ python main.py -fa protein.fasta -la proteinLabel.txt -seq protein
```

#### [3.2] Test Command-line #2: Customize Feature Selection
```console
user@machine:~$ python main.py -fa protein.fasta -la proteinLabel.txt -seq protein -f1 0 500 -f2 400 2400 -f3 1600 24420
```

#### [3.3] Test Command-line #3: Customize Feature Selection, and Classifier Selection
```console
user@machine:~$ python main.py -fa protein.fasta -la proteinLabel.txt -seq protein –m1 DT –m2 SVM –m3 LR -f1 0 500 -f2 400 2400 -f3 1600 24420
```
**Note: You can use anyone from them.**

**Table 3:**  command line element
| Symbol  | Explanation  |
| ------- | ------------ |
| -fa | Fasta file with .txt or .fasta format  |
| -la | Label file with .txt extension  |



### References












