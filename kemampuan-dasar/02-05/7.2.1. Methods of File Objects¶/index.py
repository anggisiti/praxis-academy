f.read()

f.read()

f.readline()
f.readline()

f.readline()

for line in f:
     print(line, end='')

f.write('This is a test\n')

value = ('the answer', 42)
f.write(b'0123456789abcdef')

f.seek(5)      # Go to the 6th byte in the file

f.read(1)


