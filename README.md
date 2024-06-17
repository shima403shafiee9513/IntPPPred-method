# IntPPPred
The interactions between proteins and peptides are one of the most crucial biological interactions and are implicated in abnormal cellular behaviors leading to diseases such as cancer. Thus, knowledge of these interactions provides invaluable insights into all cellular processes such as DNA repair, replication, gene expression and metabolism, and drug discovery to treat many diseases including cancer.

The current study introduces an evolutionary computation-based algorithm (IntPPPred) to improve the protein-peptide interaction prediction at the residue level. 

** Computation For Multiple Feature Construction in Bioinformatics (Case Study: Protein-Peptide Interaction Prediction). **

# Please cite the relevant publication if you will employ this paper.

**Citation: ** S. Shafiee, A. Fathi and G. Taherzadeh: Integration of Evolutionary Computation For Multiple Feature Construction in Bioinformatics (Case Study: Protein-Peptide Interaction Prediction).
# System requirement

numpy 1.21.2

pandas 1.1.3

torch 1.8.0

biopython 1.79

python 3.7.9

GSP (2018):https://dl.acm.org/doi/10.1007/s10489-018-1327-7

# Types of Files 

• Test.txt

• Train.txt

• Model.py

• pre-process1

• pre-process2

• pre-process3

• test.final.features.xlsx

• train. final. features.zip

# Guide

• The Data.rar relies on residue by residue. Thus, it includes two files that contain Fast A sequences.

• Pre-processing1,2, 3 are pre-required to run model.py.

• model.py is the proposed method (IntPPPred).

• test.final.features.xlsx and train. final. features.xlsx are basic (low-level) features.

model.py is the main file. To run, all the above files should be provided in one folder. Run in Linux: python model.py to predict the peptide binding regions in proteins.

# Contact 

It was a pleasure to receive your comment and any feedback you can give us on this source code. Likewise, for further details or questions, it is possible to communicate through email (shafiee.shima@razi.ac.ir).

Thanks in advance.

Shafiee.shima@razi.ac.ir
