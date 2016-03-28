#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 3/25/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

#main program file

from FBStock import *

stocks=FBStock() #create FBStock instance
stocks.openFile()
stocks.get_data_list() #create stock data list


#ask what year they want to find the average of
year=0
while not 2012<=year<=2016:
  try:
    year=int(raw_input('What year do you want averaged? '))
    if not 2012<=year<=2016:
      print 'Year must be between 2012 and 2016\n'
  except ValueError:
    print 'Please enter a valid year between 2012 and 2016\n'
  except TypeError:
    print 'Please enter a valid year\n'

print
stocks.average_data(year)
raw_input('Press ENTER to end')
