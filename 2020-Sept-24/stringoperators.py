s = "Strings are awesome!"
print("Length of s = %d" % len(s))

print("The first occurence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("The first five characters are '%s'" % s[:5])#start
print("The next five characters are '%s'" % s[5:10])#5 to 10
print("The thirteen characters is '%s'" % s[12])#Just number 12
print("The characters with odd index are '%s'" % s[1::2])#(0-based indexing)
print("The last five characters are '%s'" % s[-5:])#5th-rom-last to end
#upper case
print("String in uppercase:%s" % s.upper())

#lower case
print("String in lowercase: %s" % s.lower())

if s.endswith("Str"):
    print("String starts with 'str'. Good!")

if s.endswith("ome!"):
    print("String ends with 'ome!'.Good!")


print("Split the words of the string: %s" % s.split(" "))
    
