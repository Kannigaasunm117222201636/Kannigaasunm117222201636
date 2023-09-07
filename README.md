- 👋 Hi, I’m @Kannigaasunm117222201636
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Kannigaasunm117222201636/Kannigaasunm117222201636 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
def print_Fibonacci_Numbers(n):
f1=0
f2=1
if(n<1):
 return n
for x in range (0,n):
  print (f2,end=" ")
  next=f1+f2
  f1=f2
  f2=next
num=int(input ("Enter The Number:"))
print_Fibonacci_Numbers(n)


