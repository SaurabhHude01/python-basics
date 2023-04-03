import re

# read in the file
with open("preproinsulin-seq.txt", "r") as f:
    seq = f.read()

# use regex to remove unwanted characters
seq = re.sub(r'ORIGIN.*\n', '', seq)  # remove everything between ORIGIN and the first newline character
seq = re.sub(r'\d+', '', seq)  # remove all numbers
seq = re.sub(r'\s', '', seq)  # remove all whitespace characters
seq = seq.replace('//','')  # remove the remaining //

# confirm that the resulting sequence has 110 characters
if len(seq) == 110:
    print("Sequence has 110 characters.")
else:
    print("Sequence does not have 110 characters.")

# write cleaned sequence to file
with open("preproinsulin-seq-clean.txt", "w") as f:
    f.write(seq)
    
# read in the cleaned preproinsulin sequence
with open("preproinsulin-seq-clean.txt", "r") as f:
    preproinsulin_seq = f.read()

# save the LS insulin sequence to lsinsulin-seq-clean.txt
ls_insulin_seq = preproinsulin_seq[0:24]
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(ls_insulin_seq)
if len(ls_insulin_seq) == 24:
    print("lsinsulin-seq-clean.txt saved successfully.")
else:
    print("Error: lsinsulin-seq-clean.txt does not have 24 characters.")

# save the B insulin sequence to binsulin-seq-clean.txt
b_insulin_seq = preproinsulin_seq[24:54]
with open("binsulin-seq-clean.txt", "w") as f:
    f.write(b_insulin_seq)
if len(b_insulin_seq) == 30:
    print("binsulin-seq-clean.txt saved successfully.")
else:
    print("Error: binsulin-seq-clean.txt does not have 30 characters.")

# save the C insulin sequence to cinsulin-seq-clean.txt
c_insulin_seq = preproinsulin_seq[54:89]
with open("cinsulin-seq-clean.txt", "w") as f:
    f.write(c_insulin_seq)
if len(c_insulin_seq) == 35:
    print("cinsulin-seq-clean.txt saved successfully.")
else:
    print("Error: cinsulin-seq-clean.txt does not have 35 characters.")

# save the A insulin sequence to ainsulin-seq-clean.txt
a_insulin_seq = preproinsulin_seq[89:110]
with open("ainsulin-seq-clean.txt", "w") as f:
    f.write(a_insulin_seq)
if len(a_insulin_seq) == 21:
    print("ainsulin-seq-clean.txt saved successfully.")
else:
    print("Error: ainsulin-seq-clean.txt does not have 21 characters.")
