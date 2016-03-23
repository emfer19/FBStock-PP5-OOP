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
