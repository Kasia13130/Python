Tax = (4, 7, 8, 23)
print(Tax)

print(Tax[2])
print(Tax[-1])
print(Tax.index(7))
print(Tax.count(8))     # ile razy dany element pojawia sie w krotce
print(max(Tax))

# skonwertowanie krotki (tuple) na liste by moc edytowac elementy
TaxList = list(Tax)
print(TaxList)
TaxList.append(30)
print(TaxList)

# skonwertowanie listy z powrotem na krotke
NewTax = tuple(TaxList)
print(NewTax)

(tax1, tax2, tax3, tax4) = Tax
print(tax1, tax2, tax3, tax4)

a = 1
b = 10
print("a =", a, "\tb =", b)
# a = b
# b = a
print("a =", a, "\tb =", b)

# uzycie krotki
(a, b) = (b, a)
print("a =", a, "\tb =", b)


# cwiczenie
marketing = ["loyality program", "client promotion", "market research"]
print(marketing)
marketing.append("public relations")
print(marketing)
print(marketing[3])
marketing.insert(2, "investor relations")
print(marketing)
emailMarketing = marketing.copy()
print(emailMarketing)
emailMarketing.sort()
print(emailMarketing)

internalEmails = ["internal communication"]
print(internalEmails)

emailMarketing.extend(internalEmails)
print(emailMarketing)

emailTuple = tuple(emailMarketing)
print(emailTuple)