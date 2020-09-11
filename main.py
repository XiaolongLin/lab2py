
# Author: Xiaolong Lin xxl5453@psu.edu
# Collaborator:Manraj Kumar mmk6281@psu.edu
# Collaborator:John Malay jmm9098@psu.edu   
# Collaborator:Irfan Khan imk5134@psu.edu
# Section: 006R
# Breakout: 15

def getLetterGrade(numbergrade):
 if numbergrade >= 93.0:
  lettergrade = "A"
 elif numbergrade >= 90.0:
  lettergrade = "A-"
 elif 90 > numbergrade >= 87.0:
  lettergrade = "B+"
 elif 87 > numbergrade >= 83.0:
  lettergrade = "B"
 elif 83 > numbergrade >= 80:
  lettergrade = "B-"
 elif 80 > numbergrade >= 77:
  lettergrade = "C+"
 elif 77 > numbergrade >= 70:
  lettergrade = "C"
 elif 70 > numbergrade >= 60:
  lettergrade = "D"
 elif 60 > numbergrade >= 0:
  lettergrade = "F"
 return lettergrade

def run():
 numbergrade = float(input("Enter your CMPSC 131 grade: "))
 print(f"Your letter grade for CMPSC 131 is {getLetterGrade(numbergrade)}.")

if __name__ == "__main__":
 run()