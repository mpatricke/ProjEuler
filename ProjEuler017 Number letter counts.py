"""
Project Euler 017: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are:
    3 + 3 + 5 + 4 + 4 = 19 letters used in total. 

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""

wordLtrCount = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',00:'',100:'hundred',1000:'thousand','+':'and'}

def countLenUnits(n):
    numWord = wordLtrCount[n]
    return numWord

def countLenTens(n):
    nStr = str(n)

    if int(nStr[0]) == 0 or int(nStr[0]) == 1:
        numWord = wordLtrCount[n]

    else:
        numWordTens = wordLtrCount[int(nStr[0]+'0')]
        numWordUnits = wordLtrCount[int(nStr[1])]

        numWord = numWordTens + ' ' + numWordUnits

    return numWord
        
                                  
targetNum = 1000
sumTot = 0

for i in range(targetNum+1):
    iStr = str(i)
    numWordThou = ''
    numWordHun = ''
    numWordTens = ''
    numWordUnits = ''

    iStrxxx = 'xxxxxxx' + iStr
    iStrx = iStrxxx[-4:]

    if iStrx[0] != 'x':
        numWordThou = countLenUnits(int(iStrx[0])) + ' thousand'

    if iStrx[1] != 'x' and iStrx[1] != '0':
        numWordHun = countLenUnits(int(iStrx[1])) + ' hundred'

    if iStrx[2] != 'x' and iStrx[2] != '0':
        numWordTens = countLenTens(int(iStrx[-2:]))

    elif iStrx[2] == 'x' and iStrx[3] != '0':
        numWordUnits = countLenUnits(int(iStrx[3]))

    elif iStrx[2] == '0' and iStrx[3] != '0':
        numWordUnits = countLenUnits(int(iStrx[3]))

    if len(numWordThou + numWordHun) == 0 or len(numWordTens + numWordUnits) == 0:
        numWord = numWordThou + ' ' + numWordHun + numWordTens + ' ' + numWordUnits

    else:
        numWord = numWordThou + ' ' + numWordHun + ' and ' + numWordTens + ' ' + numWordUnits

    numWordComp = numWord.replace(" ","")
    sumTot += len(numWordComp)
    

print("For",targetNum," the letter count is",sumTot)
