from random import rand

SEQUENCES = [] #A list of the generated sequence
SEQUENCETYPE = "RNA" #RNA || DNA
NUMBEROFSEQUENCES = 5 #The number of sequences to be generated
SEQUENCELENGTH = 100 #The length of each sequence
SUBSEQUENCE = "AGBT" #A subseqence of the RNA/DNA that the program is going to try to find.

def CreateDNASequence(): #Create a random DNA sequence of length SEQUENCELENGTH
  pass

def CreateRNASequence(): #Create a random RNA sequence of length SEQUENCELENGTH
  pass

def WriteSequences(): #Generates and writes the sequences to a file. 
  if SEQUENCETYPE == 'RNA':
    for i in range(NUMBEROFSEQUENCES):
      CreateRNASequence()
  elif SEQUENCETYPE == 'DNA':
    for i in range(NUMBEROFSEQUENCES):
      CreateDNASequence()

  #Write SEQUENCES to a file.
  
def main():
  WriteSequences() 

if __name__ == "__main__":
    main()
