s=input("enter a string:")
v=0
if "@" and "." in s:
   k=s.index("@")
   h=s.index(".")
   if h>k:
      for i in range(0,k):
         if s[i].isalnum():
            v=1
            break
         else:
            v=0
      for i in range(k+1,h):
         if s[i].isalnum():
            v=1
            break
         else:
            v=0
      for i in range(h+1,len(s)):
         if s[i].isalnum():
            v=1
            break
         else:
            v=0
if v==0:
   print("invalid")
else:
   print("valid")
