def computepay(h, r):
  if h > 40:
    return 40 * r + (h - 40) * r * 1.5
  return h * r

hrs = int(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))
print computepay(hrs, rate)
