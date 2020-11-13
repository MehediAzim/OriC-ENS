#  OriC-ENS: A Sequence-Based Ensemble Classifier for Predicting Origin of Replication in S. cerevisiae.

### Abstract

DNA Replication plays the most crucial part in biological inheritance, ensuring an even flow of
genetic information from parent to offspring. The beginning site of DNA Replication which is
called the Origin of Replication (ORI), plays a significant role in understanding the molecular
mechanisms and genomic analysis of DNA. Hence, it is paramount to accurately identify the
origin of replication in order to gain a more accurate understanding of the biochemical and
genomic properties of DNA. In this paper, We have proposed a new approach named OriC-ENS
that uses sequence-based feature extraction techniques, K-mer, K-gapped Mono-Di and Di
Mono, and an ensemble classification technique that uses majority voting for the identification of
Origin of Replication. We have used three SVM classifiers, one for the K-mer features and two
more for K-Gapped Mono-Di and K-Gapped Di-mono features. Finally, we used majority
voting to combine the prediction by each predictor. Experimental results on the S. Cerevisie
dataset has shown that our method achieves an accuracy of 91.62% which outperforms other
state-of-the-art methods by a significant margin. We have also tested our method using other
metrics such as Matthews Correlation Coefficient (MCC), Area Under Curve(AUC), Sensitivity,
and Specificity, where it has achieved a score of 0.83, 0.98, 0.90, and 0.92 respectively
### [1]. Read File:
All the datasets file are in `FASTA` format which can be with `.txt` or `.fasta` extension. E.g. `anyName.txt` or  `anyName.fasta`. Please know more about the FASTA file format [by clicking here!](https://en.wikipedia.org/wiki/FASTA_format).

```
>1AOII|1
ATCAATATCCACCTGCAGATTCGATTCAACTACCAGATTCGATTCAACTACCAGATTCGATTCAACTACCACTGCAGATTCGATTCAACTACCAGATTCGATTCAACTACCAGATTCGATAGATTCGATTCAACTACCAGATTCGATTCAACCTACCAGATTCGATTCAACTACCACTGCAGATTCGATTCAACTACCAGATTCGATTCAACTACCAGATTCGATAGATCTACCAGATTCGATTCAACTACCACTGCAGATTCGATTCAACTACCAGATTCGATTCAACTACCAGATTCGATAGAT
>2AOII|2
ATCAATATCCACAATACCTGCAGATTCTACCGATTCGATTCAACTACCAGATTCGATTCAACGATTCGATTCAACTACCAGATTCGATTCAACTACCACTGCAGATTCGATTCAACTACCAGATTCGATTCAACTACCAGATTCGATAGATTCGATTCAACTACCAGATTCGATTCAACCTACCAGATTCGATTCAACTACCACTGCAGATTCGATTCAACTACCAGATTCGATTCAACTACCAGATTCGATAGATCTACCAGATTCGATTCAACTACCACTTACCACTGCAGATTCGATTCAACTACCAGATTCGATTCAACTACCAGATTCGATAGATTCGATTCAACTACCAGATTCGATTCAACCTACCAGATTCGATTCAACTACCACTGCAGATTCGATTCAACTACCAGATTCGATTCAACTACCAGATTCGATAGATCTACCAGATTCGATTCAACTACCACTA
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

**NB:** For DNA sequences N = {A,C,G,T}


### [3]. How to Run Package:

#### [3.1] Test Command-line #1: Run on OriC data
```console
user@machine:~$ python main.py
```

#### [3.2] Test Command-line #2: Run on different dataset
```console
user@machine:~$ python main.py -fa dna.fasta -la dnaLabel.txt
```

**NB: You can use anyone from them.**

**Table 3:**  command line element
| Symbol  | Explanation  |
| ------- | ------------ |
| -fa | Fasta file with .txt or .fasta format  |
| -la | Label file with .txt extension  



### References












