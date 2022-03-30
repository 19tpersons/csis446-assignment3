import random
import datetime

SEQUENCELIST = [] #A list of the generated sequence
SEQUENCETYPE = "DNA" #RNA || DNA
NUMBEROFSEQUENCES = 25 #The number of sequences to be generated
SEQUENCELENGTH = 100 #The length of each sequence
SUBSEQUENCE = "ACGT" #A subseqence of the RNA/DNA that the program is going to try to find.
INDEXFILE = "SequenceIndices.txt" #The text file name to store the indices in each sequence

def CreateDNASequence(): #Create a random DNA sequence of length SEQUENCELENGTH
    SEQUENCE = ""
    for i in range(0,SEQUENCELENGTH):
        SEQUENCE += random.choice("ACGT")
    return SEQUENCE

def CreateRNASequence(): #Create a random RNA sequence of length SEQUENCELENGTH
    SEQUENCE = ""
    for i in range(0,SEQUENCELENGTH):
        SEQUENCE += random.choice("ACGU")
    return SEQUENCE

def WriteSequences(): #Generates and writes the sequences to a file. 
  SEQSTR = ""
  SEQINFO = ""
  SUBINDEX = -1  #Stores the index of the sub-sequence
  INDEXSTR = ""
  if SEQUENCETYPE == 'RNA':
    FILENAME = "RNASequence.txt"
    for i in range(NUMBEROFSEQUENCES):
      DATETIME = datetime.datetime.now()  #Creating new datetime for each sequence
      SEQINFO = "<Sequence_" + str(i+1) + "_" + str(DATETIME) + "\n"
      SEQUENCE = CreateRNASequence()
      SEQSTR += SEQINFO + SEQUENCE + "\n"
        
      SUBINDEX = SEQUENCE.find(SUBSEQUENCE)
      if SUBINDEX == -1:
        INDEXSTR += "Sequence " + str(i+1) + " has no occurance of " + SUBSEQUENCE + "\n"
      else:
        INDEXSTR += "Sequence " + str(i+1) + " index of " + SUBSEQUENCE + ": " + str(SUBINDEX) + "\n" #Used for index text file
        
  elif SEQUENCETYPE == 'DNA':
    FILENAME = "DNASequence.txt"
    for i in range(NUMBEROFSEQUENCES):
      DATETIME = datetime.datetime.now()  #Creating new datetime for each sequence
      SEQINFO = "<Sequence_" + str(i+1) + "_" + str(DATETIME) + "\n"
      SEQUENCE = CreateDNASequence()
      SEQSTR += SEQINFO + SEQUENCE + "\n"
        
      SUBINDEX = SEQUENCE.find(SUBSEQUENCE)
      if SUBINDEX == -1:
        INDEXSTR += "Sequence " + str(i+1) + " has no occurance of " + SUBSEQUENCE + "\n"
      else:
        INDEXSTR += "Sequence " + str(i+1) + " index of " + SUBSEQUENCE + ": " + str(SUBINDEX) + "\n" #Used for index text file
  
  # Outputting string to text file
  with open(FILENAME, "w") as f:
    f.write(SEQSTR)
    f.close()
    
  with open(INDEXFILE, "w") as f:
    f.write(INDEXSTR)
    f.close()
  
def main():
  WriteSequences() 

if __name__ == "__main__":
    main()