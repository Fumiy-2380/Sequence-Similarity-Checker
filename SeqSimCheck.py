import xlsxwriter 
workbook = xlsxwriter.Workbook("Sequence_Checker_Results.xlsx")
worksheet = workbook.add_worksheet()

#Store staple sequences in these lists
staple_set1 = []
staple_set2 = []
#Store the matches that occurred between different staples here
matches = []

#input files with sequences to compare
file1 = input("Input sequence file 1 name here: ")
file2 = input("Input sequence file 2 name here: ")
base_check_range = input("Input a number to define length of sequence subsections being compared: ")
#Moves list of staple sequences from txt file to staple_set list
with open(file1, "r") as staple_intro1:
	for line in staple_intro1: 
		line = line.strip("\n")
		staple_set1.append(line)
with open(file2, "r") as staple_intro2: 
	for line in staple_intro2: 
		line = line.strip("\n")
		staple_set2.append(line)
#print(staple_set1)
#print(staple_set2)

#total length of each staple_set list, setting the max number of iterations/comparisons
tot_seq1 = len(staple_set1)
tot_seq2 = len(staple_set2)
#iteration parameters
iter1 = 0
iter2 = 0
num_match = 0 
#comparison code:
while iter1 < tot_seq1: 
	staple1 = staple_set1[iter1] #sequence from staple_set1 will be compared to all sequences in staple_set2 before moving on to next sequence in staple_set1
	while iter2 < tot_seq2: 
		staple2 = staple_set2[iter2]
		#for one staple1-staple2 set
		for j, _ in enumerate(staple1):
			for i, _ in enumerate(staple2):
				if staple1[j:j + int(base_check_range)] == staple2[i:i + int(base_check_range)]:
					num_match += 1
		matches.append([iter1, iter2, num_match])
		worksheet.write(iter1, iter2, num_match)
		iter2 += 1 #move on to compare next sequence in staple_set2 with same staple from staple_set1
		num_match = 0 #reset number of matches for next comparison
	iter2 = 0 #reset so all sequences in staple_set2 can be compared with next staple_set1 sequence
	iter1 += 1 #move on to next staple_set1 sequence to compare
#print(matches)
workbook.close()
print("Analysis complete.")