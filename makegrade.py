score = raw_input('Enter score between 0.0 and 1.0')
try:
  floatScore = float(score)
  if floatScore > 1.0: print 'There is really no such thing as scoring 101 or more out of 100'
  elif floatScore >= 0.9: print 'A'
  elif floatScore >= 0.8: print 'B'
  elif floatScore >= 0.7: print 'C'
  elif floatScore >= 0.6: print 'D'
  elif floatScore >= 0.0: print 'F'
  else: print 'Really? A negetive number? Come On!'
except:
  print 'Enter a valid number next time!'
