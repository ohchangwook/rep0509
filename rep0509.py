a = input()
a = int(a)

coinlist=(500,100,50,10)
def minimumcoin(value,coinlist):
 count = 0
 residue = 1000-value
 for i in coinlist :
    count +=int(residue/1)
    residue-=int(residue/i)*i

 return count
 print(minimum-coin(a, coinlist))
