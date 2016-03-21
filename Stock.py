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
    self._date=date
    self._openingV=openingV
    self._highV
