#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 3/21/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

from Stock import Stock

class FBStock:
  def __init__(self):
    """receives nothing"""

    self._fileObj=None
    self._stocks=[]
    
  def openFile(self):
    """Continuously ask for a name of the file containing the FB stock
    information until it can be opened for reading """
    while not self._fileObj:
      filename=raw_input('Enter filename with Stock data: ')
      try:
	self._fileObj=file(filename)
      except IOError:
	print 'unable to open file',filename
    
  def get_data_list(self):
    """Read file of stock data, create list of Stock objects"""
    line=self._fileObj.readline() #read first line, trash because headers
    line=self._fileObj.readline()
    while line:
      stockObj=Stock() #create Stock object
      data=line.split() #split line read in

      #assign parts to object
      stockObj.setDate(data[0])
      stockObj.setOpeningVal(float(data[1]))
      stockObj.setHighVal(float(data[2]))
      stockObj.setLowVal(float(data[3]))
      stockObj.setClosingVal(float(data[4]))
      stockObj.setVolume(int(data[5]))
      self._stocks.append(stockObj)

      line=self._fileObj.readline()
    self._fileObj.close()

  def average_data(self,year):
    """Receive a year and find average of data for each column for year.

    Will also calculate and display month within received year with 
    the highest closing value, and month with the lowest closing value.
      **In the case of a "tie", earliest month of that year will be shown."""
    openingAvg=0.0
    highAvg=0.0
    lowAvg=0.0
    closingAvg=0.0
    volAvg=0
    highMonthOpen=0 #highest opening value
    monthHigh=0 #month with the highest open
    lowMonthClose=0 #lowest closing value
    monthLow=0 #month with the lowest close
    counter=0

    for i in range(len(self._stocks)):
      dateStock=self._stocks[i].getDate()
      dateStock=dateStock.split('/') #split the date up into its parts
      if str(year)==dateStock[2]: #if the received year matches the stock data year
        openingAvg+=self._stocks[i].getOpeningVal()
	highAvg+=self._stocks[i].getHighVal()
        lowAvg+=self._stocks[i].getLowVal()
	closingAvg+=self._stocks[i].getClosingVal()
	volAvg+=self._stocks[i].getVolume()
	counter+=1

        #find highest opening value and the month it occured
	if self._stocks[i].getOpeningVal()>highMonthOpen:
	  highMonthOpen=self._stocks[i].getOpeningVal()
	  monthHigh=dateStock[0]
	elif self._stocks[i].getOpeningVal()==highMonthOpen:
	  if monthHigh==0:
	    monthHigh=dateStock[0]
	  elif dateStock[0]<monthHigh:
	    monthHigh=dateStock[0]

        #find lowest closing value and the month it occured
	if lowMonthClose==0:
	  lowMonthClose=self._stocks[i].getClosingVal()
	  monthLow=dateStock[0]
	elif self._stocks[i].getClosingVal()<lowMonthClose:
	  lowMonthClose=self._stocks[i].getClosingVal()
	  monthLow=dateStock[0]
	elif self._stocks[i].getClosingVal()==lowMonthClose:
	  if monthLow==0:
	    monthLow=dateStock[0]
	  elif dateStock[0]<monthLow:
	    monthLow=dateStock[0]
    openingAvg=openingAvg/counter
    highAvg=highAvg/counter
    lowAvg=lowAvg/counter
    closingAvg=closingAvg/counter
    volAvg=volAvg/counter

    print 'Here are the averages for Facebook Stock for year',str(year)
    print 'Opening\tHigh\tLow\tClosing\tVolume'
    print str(openingAvg)+'\t'+str(highAvg)+'\t'+str(lowAvg)+'\t'+str(closingAvg)+'\t'+str(volAvg)
    print '\nThe month with the highest opening value was',str(monthHigh),'with',str(highMonthOpen)
    print 'The month with the lowest closing value was',str(monthLow),'with',str(lowMonthClose)


#unit testing
if __name__=='__main__':
 stocks=FBStock()
 stocks.openFile()
 stocks.get_data_list()
 stocks.average_data(2010)
