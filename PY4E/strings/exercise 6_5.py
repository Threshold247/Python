text = "X-DSPAM-Confidence:    0.8475"

findPos = text.find(':')
print(findPos)
newtext = text[findPos+1:]
print(newtext)
textstrip = newtext.strip()
print(textstrip)
value = float(textstrip)
print(value)
