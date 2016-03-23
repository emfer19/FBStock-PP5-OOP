#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 3/21/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

class Stock:
  """Collects and organizes stock data into:
      - Date
      - Opening Value
      - High Value
      - Low Value
      - Closing Value
      - Volume"""

  def __init__(self, date, openingV, highV, lowV, closingV, volume):
    """create stock with given date, opening value, high value,
       low value, closing value, and volume."""

    self._date=date
    self._openingV=float(openingV)
    self._highV=float(highV)
    self._lowV=float(lowV)
    self._closingV=float(closingV)
    self._volume=float(volume)

  def setDate(self, date):
    """Assign the received date of the Stock"""
    self._date=date

  def getDate(self):
    """Return the date of the Stock"""
    return self._date

  def setOpeningVal(self, openingV):
    """Assign the received opening value of the Stock"""
    self._openingV=float(openingV)

  def getOpeningVal(self):
    """Return the opening value of the Stock"""
    return self._openingV

  def setHighVal(self, highV):
    """Assign the received high value of the Stock"""
    self._highV=float(highV)

  def getHighVal(self):
    """Return the high value of the Stock"""
    return self._highV

  def setLowVal(self, lowV):
    """Assign the low value of the Stock"""
    self._lowV=float(lowV)

  def getLowVal(self):
    """Return the low value of the Stock"""
    return self._lowV

  def setClosingVal(self, closingV):
    """Assign the closing value of the Stock"""
    self._closingV=float(closingV)

  def getClosingVal(self):
    """Return the closing value of the Stock"""
    return self._closingV

  def setVolume(self, volume):
    """Assign the volume of the Stock"""
    self._volume=float(volume)

  def getVolume(self):
    """Return the volume of the Stock"""
    return self._volume

  def __str__(self):
    """Return a string containing all the Stock data"""
    display='Here is the stock for '+str(self._date)
    display+='\nOpening\tClosing\tHigh\tLow\tVolume'
    display+='\n'+str(self._date)+'\t'+str(round(self._openingV,2))
    display+='\t'+str(round(self._highV,2))+'\t'+str(round(self.lowV,2))
    display+='\t'+str(round(self._closingV,2))+'\t'+str(self._volume)

#end of class

#class unit test
if __name__=='__main__':
  aStock=Stock()
  aStock.setDate('3/1/2016')
  print aStock.getDate()

  aStock.setOpeningVal(5.6)
  print aStock.getOpeningVal()

  aStock.setHighVal(100)
  print aStock.getHighVal()

  aStock.setLowVal(18)
  print aStock.getLowVal()

  aStock.setClosingVal(19)
  print aStock.getClosingVal()

  aStock.setVolume(18)
  print aStock.getVolume()

  print aStock
