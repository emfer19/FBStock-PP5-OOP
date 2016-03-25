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

    self._fileobj=None
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

  def average_data(self,year):
    """Receive a year and find average of data for each column for year.

    Will also calculate and display month within received year with 
    the highest closing value, and month with the lowest closing value.
      **In the case of a "tie", earliest month of that year will be shown."""
    objects=[]
    for i in len(self._stocks):
      if str(year) in self._stocks[i].getDate():
        objects.append()
    print objects


#unit testing
if __name__=='__main__':
  
