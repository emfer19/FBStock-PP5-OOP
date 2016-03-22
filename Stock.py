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
    self._openingV=openingV
    self._highV=highV
    self._lowV=lowV
    self._closingV=closingV
    self._volume=volume

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
    self._lowV=lowV

  def getLowVal(self):
    """Return the low value of the Stock"""
    return self._lowV

  def setClosingVal(self, closingV):
    """Assign the closing value of the Stock"""
    self._closingV=closingV

  def getClosingVal(self):
    """Return the closing value of the Stock"""
    return self._closingV

  def setVolume(self, volume):
    """Assign the volume of the Stock"""
    self._volume=volume

  def getVolume(self):
    """Return the volume of the Stock"""
    return self._volume

  def __str__(self):
    """Return a string containing all the Stock data"""
    display='Date: 
