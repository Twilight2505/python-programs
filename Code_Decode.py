x="djf"
y="dsh"
def encode(a):
    lt= str.split() 
    encoded=[]
    for val in lt:
        if (len(val)<3):
         encoded.append(val[::-1])
        elif(len(val)>=3):
            str2= val[1:len(val)]
            str1= val[0]
            encoded.append((x+str2+str1+y))
    return print(" ".join(encoded))



def decode(a):
   lt1= str.split()
   decoded=[]
   for val1 in lt1:
      if(len(val1)<3):
         decoded.append(val1[::-1])
      elif(len(val1)>=3):
         str3=val1.removeprefix(x)
         str4=str3.removesuffix(y)
         str5=str4[:-1]
         str6= str4[len(str4)-1:] 
         decoded.append(str6+str5)
   return print(" ".join(decoded))

permit=input("Do you want to decode or encode: ").lower()
if(permit=="encode"):
 str = input("Enter your sentence:")
 encode(str)
elif(permit=="decode"):
  str = input("Enter your sentence:")
  decode(str)
 


       
    

    