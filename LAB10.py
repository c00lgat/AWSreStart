"""
Your module description
"""

infile = "preproinsulin-seq.txt"
outfile = "preproinsulin-seq-clean.txt"

delete_list = ["ORIGIN", "1", "61", "//", " ", "\n"]


with open(infile) as fin, open (outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
        
        

file = open('preproinsulin-seq-clean.txt', 'r')
text = file.read()


new_out_file = "lsinsulin-seq-clean.txt"
with open(new_out_file, "w+") as fout:
    for letter in range(24):
        fout.write(text[letter])
    


new_out_file = "binsulin-seq-clean.txt"
with open(new_out_file, "w+") as fout:
    for letter in range(25,55):
        fout.write(text[letter])
        
        

new_out_file = "cinsulin-seq-clean.txt"
with open(new_out_file, "w+") as fout:
    for letter in range(55,90):
        fout.write(text[letter])
        
        
        
new_out_file = "ainsulin-seq-clean.txt"
with open(new_out_file, "w+") as fout:
    for letter in range(55,90):
        fout.write(text[letter])
