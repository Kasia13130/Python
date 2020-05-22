message = 'Document "cv.doc" was printed on printer: XEROX'

print(message.find(':'))
print(message[message.find(':')+2:])
print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])
print("\n")

q = "THE EYES"
print(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7])
print(q[0] + q[1] + q[2] + q[3] + q[4] + q[5] + q[6] + q[7])
print("\n")


qq = "a gentelman"
print(qq)
print(qq[3] + qq[6] + qq[7] + qq[2] + qq[0] + qq[4] + qq[5] + qq[1] + qq[8:])
print("\n")

something = "THE MORSE CODE"
print("here come dots")
print(something[1:3] + something[6] + something[8] + something[9:12] + something[4] + something[13] + " "
      + something[12] + something[11] + something[0] + something[7])
print("\n")

line = 'Program "Kropka nad i" nadamy o: 22:00'
print(line)
time = line[line.find(":")+2:]
print(time)
tmp = line[line.find('"'):22]
print(tmp)
print(tmp + "   " + time)
print("\n")

line2 = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
print(line2)
time2 = line2[line2.find(":")+2:]
print(time2)
tmp2 = line2[line2.find('"'):30]
print(tmp2)
print(tmp2 + "   " + time2)
