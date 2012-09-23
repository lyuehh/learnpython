poem = """
\t The lovely world
with logic so firmly planted
cannot discren...
"""
print "-------"
print poem
print "-------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
  jelly_beans = started * 500
  jars = jelly_beans / 1000
  ceates = jars / 100
  return jelly_beans, jars, ceates

start_point = 10000
beans, jars, ceates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans" % beans

print "xxxx"

