import string
alpha=string.ascii_uppercase
l=alpha+alpha
k=[]
for x in range(0,26):
    for y in range(0,26):
        k.append(l[x+y])
mes=input("Enter your message:")
mes=mes.upper()
mes=mes.repalce(" ","")
key=input("Enter your Key:")
key=key.upper()
pkey=key
def encrypt(mes,pkey):
        if(len(key)<len(mes)):
            i=0
            while(len(pkey)!=len(mes)):
                pkey=pkey+key[i]
                i=i+1
                i=i%len(key)
        for x in range(0,len(mes)):
            pos=alpha.index(mes[x])+alpha.index(pkey[x])
            print(k[pos],end="")
def decrypt(mes,pkey):
      if(len(key)<len(mes)):
            i=0
            while(len(pkey)!=len(mes)):
                pkey=pkey+key[i]
                i=i+1
                i=i%len(key)
      for x in range(0,len(mes)):
            pos=alpha.index(mes[x])-alpha.index(pkey[x])
            print(k[pos],end="")
print("1.Encrypt 2.Decrypt")
choice=int(input("Enter your choice:"))
if(choice==1):
    encrypt(mes,pkey)
if choice==2:
    decrypt(mes,key)


