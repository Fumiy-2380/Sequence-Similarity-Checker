# Sequence-Similarity-Checker
Compares sets of staple DNA strands used in DNA origami to analyze sequence similarity between them, checking for any potential issues with binding specificity. Can be used to avoid non-specific binding of staple strands to the scaffold, which may cause inaccurate structure formation. 

Requires xlsxwriter 
$pip3 install xlsxwriter

# File Pre-treatment:
The column with only the sequences from the excel (or csv) sheet exported from caDNAno should be copied and pasted into a .txt file for the sequence sets that are to be compared. The two .txt files should be put in a folder in the same location as this script.

# Running the Script 
$cd #change directory to the folder containing this script and the two .txt files. 
$python3 SeqSimCheck.py

The script will then ask for the file names where the staple sequences are stored. Input them one at a time:
$file1.txt
$file2.txt

Finally, input the desired length of "sub-sections" of the staple sequences that is to be compared. Inputting 7 will set the comparing "frame" to 7 bases. The first 7 bases on staple 1 will be compared to the first 7 bases on staple 2, then the first 7 bases will be compared to 7 bases on staple 2 but shifted one base towards the 3' end. After the first 7 bases of staple1 has been compared to the entire staple 2 length, the script will shift the 7 base frame one base to the 3' end on staple 1, iterating the process. Once the entirety of staple 1 has been compared with staple 2, the variable staple2 is reassigned a different sequence from staple_set2, and compared in the same way. After sequence 1 has been compared with all of the sequences in staple_set2, staple1 will be reassigned another sequence from staple_set1. 

The columns and rows represent each staple strand sequence. The value stored in any cell represents the number of matches that were found between those two sequences. Higher values indicate higher similarity between the sequences. 
