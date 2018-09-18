

# # get input to know how many fast/slow songs to output
# # for example: 2 2, or 2 1, or 1 1
# # input: N/A
# # output: a list of 2 numbers
# def getInput():
#   sys.stdout.write("Enter numbers of fast and slow songs, such as 2 2: ")
#   numbers = [int(x) for x in raw_input().split()]
#   return numbers


# # append new input to file
# def writeHistory(R):
#   newline = ', '.join(R)
#   with open("history.txt", 'a') as hfile:
#     hfile.write(newline+"\n")
import re

class Row(object):
  year=0
  date=0
  name=""
  amount=0.0
  cat = ""
  tag=""
  desc=""

  def __init__(self, year, date, name, amount, cat, tag, desc):
    self.year = year
    self.date = date
    self.name = name
    self.amount = amount
    self.cat = cat
    self.tag = tag
    self.desc = desc

# read csv file and output as a dictionary
def read(inputpath):
  # dictionary for the final output
  # adict = OrderedDict()
  
  with open(inputpath, 'r') as f:
    entries = []
    next(f)
    for lines in f:
      newline = lines.rstrip()
      row = newline.split(",")
      entries.append(Row(row[0],row[1],row[2], row[3], row[4], row[5], row[6]))
    
    groc = 0
    household = 0
    trans = 0
    parking = 0
    food = 0
    total = 0

    for entry in entries:
      if entry.amount:
        print float(entry.amount)

      if entry.cat == "Grocery":
        groc += float(entry.amount)

      if entry.cat == "Household":
        household += float(entry.amount)

      if entry.cat == "Transportation":
        trans += float(entry.amount)

      if entry.cat == "Transportation":
        trans += float(entry.amount)

      if re.search('food', entry.tag, re.IGNORECASE):
          food += float(entry.amount)    
    print "grocery", groc
    print "household", household
    print "transportation", trans
    
    print "food", food
    print "total", total