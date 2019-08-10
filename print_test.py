# Pass it as a tuple:
name = "Anoop CH"
score = 9.0

print("Total score for %s is %s" % (name, score))

# Pass it as a dictionary:
print("Total score for %(n)s is %(s)s" % {'n': name, 's': score})

# There's also new-style string formatting, which might be a little easier to read:
# Use new-style string formatting:
print("Total score for {} is {}".format(name, score))

# Use new-style string formatting with numbers (useful for reordering or printing the same one multiple times):
print("Total score for {0} is {1}".format(name, score))

# Concatenate strings:
print("Total score for " + str(name) + " is " + str(score))

# The clearest two, in my opinion: Just pass the values as parameters:
print("Total score for", name, "is", score)

# Use the new f-string formatting in Python 3.6:
print(f'Total score for {name} is {score}')
