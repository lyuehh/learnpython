def cheese_cracker(a,b):
  print "You have %d cheeses!" % a
  print "You have %d boxes of cr!" % b
  print "Ok..\n"

print "We can call the function"
cheese_cracker(20,30)

print "Call func with var"
a = 10
b = 20

cheese_cracker(a,b)

print "Call func in side"
cheese_cracker(10 + 20,5 + 6)

