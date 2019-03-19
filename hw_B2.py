with open('rosalind_revc.txt') as file:
    a=file.read()
    b=a.replace('A', 't')
    d=b.replace('T', 'a')
    e=d.replace('G', 'c')
    f=e.replace('C', 'g')
    g=f.upper()
print(g[::-1])
