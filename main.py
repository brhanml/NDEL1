# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



'''

Below is the script used to generate missense mutations for analysis via the meta-SNP tool.

'''

f2 = open("mut_file.txt", "w")
amino_acids = ["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]

fasta = "AEQRNRDLQADNQRLKYEVEALKEKLEHQYAQSYKQVSVLEDDLSQTRAIKEQLHKYVRELEQANDDLERAKRATIVSLEDFEQRLNQAIERNAFLESELDEKESLLVSVQ"


count = 168
for char in fasta:
    for ele in amino_acids:
        f2.write(char + str(count) + ele + ";" + "\n")
    count += 1

f2.close()


'''

Below is the script used to generate the missense mutations for each chain of NDEL1 for analysis via FoldX.
NDEL1 is a tetramic protein with 4 identical chains. The B chain was selected as using the A chain for input resulted in errors.

'''


#f1 = open("new.txt", "r")
f2 = open("mut_file.txt", "w")
amino_acids = ["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]

fasta = "AEQRNRDLQADNQRLKYEVEALKEKLEHQYAQSYKQVSVLEDDLSQTRAIKEQLHKYVRELEQANDDLERAKRATIVSLEDFEQRLNQAIERNAFLESELDEKESLLVSVQ"

#print(len(amino_acids))

count = 58
for char in fasta:
    for ele in amino_acids:
        f2.write(char + "B" + str(count) + ele + ";" + "\n")
    count += 1

#f1.close()
f2.close()