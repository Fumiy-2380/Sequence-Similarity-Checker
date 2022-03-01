import tkinter as tk
from tkinter import filedialog as fd
import xlsxwriter as xlw

import sys
sys.setrecursionlimit(5000)

# Set up where results will go
workbook = xlw.Workbook("Sequence_similarity_results.xlsx")
worksheet = workbook.add_worksheet("Similarity Matrix")
cworksheet = workbook.add_worksheet("Hybridization Matrix")

# Import sequences of DNA strands using tkinter
root = tk.Tk()
root.withdraw()

file1 = fd.askopenfilename()
file2 = fd.askopenfilename()

sequence_list1 = []
sequence_list2 = []

with open(file1, "r") as set1:
    for line in set1:
        sequence_list1.append(line.strip("\n"))
with open(file2, "r") as set2:
    for line in set2:
        sequence_list2.append(line.strip("\n"))
# ----------------------------------------------------------------------------------------------------------------------------------------------------- #

# Define functions
def sequentialMatches(str1, str2, check_frame):
    """
    Recursive function to find the % similarity between two strings.
    Takes a slice of the first string, str1, and checks if that slice is in the second string str2. 
    The size of the slice is determined by check_frame. If a match does exist, the check_frame is increased,
    and the function is run again recursively. 
    Returns the max number of check_frame until there are no matches between the two strings, the maximum number of sequential matches between strings.
    """
    number_of_matches = 0 
    for i in range(0,(len(str1)-check_frame)):
        if str1[i:(i+check_frame)] in str2:
            number_of_matches += 1
    if str1 == str2:
        return 100
    elif (str1 != str2) and (number_of_matches >= 1):
        return sequentialMatches(str1, str2, check_frame + 1)
    elif number_of_matches == 0:
        return (check_frame-1)

def complement(someString):
    """
    Finds the complementary sequence of a sequence of DNA.
    """
    tempList = []
    for char in someString:
        if char == "A":
            tempList.append("T")
        elif char == "T":
            tempList.append("A")
        elif char == "C":
            tempList.append("G")
        elif char == "G":
            tempList.append("C")
    tempList.reverse()
    return "".join(tempList)

def shortest(*someStrings):
    """
    Finds the shortest string out of the many strings inputted as arguments, separated by commas.
    """
    storeList = []
    for someString in someStrings:
        storeList.append(someString)
    iter_index = 0
    shortest = storeList[0]
    while iter_index < len(storeList):
        if len(shortest) > len(storeList[iter_index]):
            shortest = storeList[iter_index]
        else:
            pass
        iter_index += 1
    return len(shortest)

# ----------------------------------------------------------------------------------------------------------------------------------------------------- # 

# Run Program
if __name__ == "__main__":
    for seqString in sequence_list1:        # Double for loop - compares all sequences in list 2 with each sequence of list 1
        input1 = seqString                  # first input of similarity() function
        for seqString2 in sequence_list2:
            input2 = seqString2             # second input of similarity() function
            cinput2 = complement(seqString2)
            similarity_score = sequentialMatches(input1, input2, 2)/shortest(input1, input2)*100 # Calculate the first similarity score
            csimilarity_score = sequentialMatches(input1, cinput2, 2)/shortest(input1, cinput2)*100 # Calculate the second similarity score, with the input1 string and complementary sequence of input2 string
            if similarity_score >= 100: # If the similarity is 100%, just return 100
                worksheet.write(sequence_list1.index(seqString)+1, sequence_list2.index(seqString2)+1, 100)
            else: # If the similarity is not 100%, calculate the percent using similarity divided by the shortest string.
                worksheet.write(sequence_list1.index(seqString)+1, sequence_list2.index(seqString2)+1, similarity_score)
            if csimilarity_score == 100: # If the similarity of input1 and the complementary sequence of input2 is 100%, return 100
                cworksheet.write(sequence_list1.index(seqString)+1, sequence_list2.index(seqString2)+1, 100)
            else: # If similarity is not 100%, calculate the percent similarity using similarity divided by the shortest string.
                cworksheet.write(sequence_list1.index(seqString)+1, sequence_list2.index(seqString2)+1, csimilarity_score)
    
    # Parameters of the output excel sheet - format and conditinoal formatting
    format1 = workbook.add_format({'bg_color':'#FFC7CE', 'font_color':'#9C0006'})
    worksheet.conditional_format('B1:XFD1048576', {'type':'cell', 'criteria':'>=', 'value':33, 'format':format1})
    cworksheet.conditional_format('B1:XFD1048576', {'type':'cell', 'criteria':'>=', 'value':33, 'format':format1})

workbook.close()