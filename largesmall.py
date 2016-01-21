largest = None
smallest = None
_input = None
while _input != 'done':
  _input = raw_input('Enter a number or "done" to calculate: ')
  try:
    if _input != 'done':
      _input = int(_input)
      if _input > largest or largest is None:
        largest = _input
      if _input < smallest or smallest is None:
        smallest = _input
  except:
    print 'Invalid input'
print 'Maximum is', largest
print 'Minimum is', smallest
