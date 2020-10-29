f,d=list(map(int,input().split()))
for i in range(1,f,2):
  a=".|." * i
  print(a.center(d,"-"))
a="Welcome"
print(a.center(d,"-"))
for i in range(f - 2,0,-2):
  a=".|." * i
  print(a.center(d, "-"))
