# problemA_keyword.csv
2, for in for in if and break との類似度が0.5 以上
python_select2A.csv

- 2, for in for in if and break
    -  hashing，implementation，*1500
	- 2
- 108, while if break
    -  implementation    strings    *1000
	- 103
- 161, lambda for in while and if break for in
    -  binary search    brute force    greedy    two pointers    *1300
	- 153
- 198, for in if else break
    -  implementation    math    *1700
	- 178
- 232, for in while for in if break for in
    -  binary search    constructive algorithms    graphs    greedy    *1600
	- 206
- 277, lambda for in if else while for in if break else
    -  dfs and similar    dsu    *1400
	- 249
- 363, while if break
    -  implementation    *800
	- 326
- 447, while if in break
    -  implementation    *800
	- 403
- 641, for in if or break
    -  implementation    *1000
	- 565
- 673, for in if break
    -  implementation    *800
	- 592
- 708, while while and if break if
    -  constructive algorithms    greedy    implementation    strings    *1200
	- 619
- 754, if for in if break else
    -  constructive algorithms    greedy    implementation    *1200
	- 660
- 803, if else for in for in if break for in if for in
    -  constructive algorithms    *1400
	- 704
- 813, lambda for in if break
    -  implementation    *1100
	- 714
- 839, for in if break
    -  implementation    *900
	- 733
- 909, for in if break
    -  brute force    greedy    sortings    *1000
	- 791
- 910, while if break else
    -  dfs and similar    dp    greedy    implementation    *800
	- 794
- 929, for in if if break
    -  *special problem    greedy    implementation    *1400
	- 809
- 930, for in if if break
    -  dfs and similar    graphs    trees    *1500
	- 810
- 949, for in if if else else if else break if and for in else
    -  greedy    *1600
	- 825
- 967, lambda for in if break
    -  implementation    *1100
	- 841

## タグに関して

https://codeforces.com/blog/entry/14565

## 2, for in for in if and break

n,k,s=eval(input()),{},[]
for i in range(n):a,b=input().split(' ');k[a]=k.get(a,0)+int(b);s.append([a,k[a]])
n=max(k.values())
for i ,j in s:
    if k[i]==n and int(j)>=n:print(i);break

## 108, while if break

h,m=map(int,input().split(':'))
m+=h*60
while 1:
    m=(m+1)%1440  
    r=f'{m//60:02}:{m%60:02}'
    if r==r[::-1]:
        print(r)
        break

## 161, lambda for in while and if break for in

I = lambda: list(map(int, input().split()))
n, m, x, y = I()
a, b = I(), I()
l = []
j = 0
for i in range(n):
    while j < m and b[j] <= a[i] + y:
        if a[i] - x <= b[j]:
            j += 1
            l += [(i + 1, j)]
            break
        j += 1
print(len(l))
for i, j in l:
    print(i, j)

## 198, for in if else break

k, b, n, t = map(int, input().split())
z = int(1)
res = int(n)
 
for i in range(n):
	z = k*z + b
	if z <= t:
		res -= 1
	else:
		break
 
print(res)

## 232, for in while for in if break for in

n , k = 0 , int(input())
p=[['0']*100 for i in range(100)]
while k:
	for i in range(n):
		if i>k:
			break
		p[n][i]=p[i][n]='1'
		k=k-i
	n+=1
print(n)
for i in range(n): print(''.join(p[i][:n]))

## 277, lambda for in if else while for in if break else

I=lambda:list(map(int,input().split()))
n,m=I()
r=0
t=[]
for _ in range(n):
	l=I();
	if l[0]==0:r+=1
	else:t+=[set(l[1:])]
i=0
while i<len(t):
	for j in t[i+1:]:
		if t[i]&j:t[i]|=j;t.remove(j);break
	else:i+=1
print(max(0,len(t)-1)+r)

## 363, while if break

n=int(input())
while 1:
  x=n%10
  print(['O-','-O'][x>4]+'|'+x%5*'O'+'-'+(4-x%5)*'O')
  n//=10
  if n<1:break

## 447, while if in break

p,n=map(int,input().split())
r,s=0,{p}
while r<n:
  x=int(input())%p
  if x in s:break
  r+=1;s|={x}
print([-1,r+1][r<n])

## 641, for in if or break

n=int(input())
a=input()
d=*map(int,input().split()),
x=0
v=[1,-1]
for i in range(n+1):
  x+=v[a[x]=='<']*d[x]
  if x<0 or x>=n:break
print('IN'*(i>=n)+'FINITE')

## 673, for in if break

i=input
i()
l=0
for x in map(int,input().split()):
  if x>l+15:break
  l=x
print(min(90,l+15))

## 708, while while and if break if

s=list(input())
i=f=0
while(i<len(s)):
	while(i<len(s) and s[i]!='a'):
		s[i]=chr(ord(s[i])-1)
		f=1
		i+=1
	if(f):
		break
	i+=1
if(f==0):
	s[len(s)-1]='z'
print("".join(s))

## 754, if for in if break else

n = int(input())
A = list(map(int,input().split()))
sumA = sum(A)
if sumA:
	print('YES')
	print(1)
	print(1,n)
	exit()
for x in range(n):
	sumA  -= A[x]
	if sumA:
		print('YES')
		print(2)
		print(1,x+1)
		print(x+2,n)
		break
else:
	print('NO')

## 803, if else for in for in if break for in if for in

n,k=map(int,input().split())
if k>(n*n):
	print(-1)
else:
	mat=[[0]*n for i in range(n)]
	for i in range(n):
		if k==0:
			break
		mat[i][i]=1
		k-=1
		for j in range(i+1,n):
			if k>1:
				mat[i][j]=1
				mat[j][i]=1
				k-=2
#		print(mat,k)
	for i in mat:
		print(*i)

## 813, lambda for in if break

I=lambda: map(int, input().split())
I()
n, a=sum(I()), -1
for _ in range(*I()):
	l, r=I()
	if n<=r:
		a=max(n, l)
		break
print(a)

## 839, for in if break

_,k=map(int,input().split())
r,c=0,0
for x in map(int,input().split()):
  r+=1
  c+=x
  d=min(c,8)
  c-=d;k-=d
  if k<1:break
print([r,-1][k>0])

## 909, for in if break

f,s=input().split()
l=f[0]
for c in f[1:]:
	if c>=s[0]:break
	l+=c
print(l+s[0])

## 910, while if break else

n,d=map(int,input().split())
a=input()
x=0
r=0
while x!=n-1:
  y=a[:x+d+1].rfind('1')
  if y==x:
    r=-1
    break
  else:x=y
  r+=1
print(r)

## 929, for in if if break

n, k = input().split();
n=int(n)
k=int(k)
b=1;
arr = input()
l = list(map(int,arr.split(' ')))
s=l[0]
for i in range(1,n):
    if(l[i]-s>k):
       if(l[i]-l[i-1]>k):
           b=-1
           break
       s=l[i-1]
       b=b+1
print(b)

## 930, for in if if break

n, k = input().split();
n=int(n)
k=int(k)
b=1;
arr = input()
l = list(map(int,arr.split(' ')))
s=l[0]
for i in range(1,n):
    if(l[i]-s>k):
       if(l[i]-l[i-1]>k):
           b=-1
           break
       s=l[i-1]
       b=b+1
print(b)

## 949, for in if if else else if else break if and for in else

s=input()
l=[]
even=[]
odd=[]
f=1
for i in range(len(s)):
	if s[i]=='0':
		if len(even)!=0:
			ind=even.pop()
			l[ind].append(i+1)
			odd.append(ind)
		else:
			l.append([i+1])
			odd.append(len(l)-1)
	else:
		if len(odd):
			ind=odd.pop()
			l[ind].append(i+1)
			even.append(ind)
		else:
			f=0
			break
if f and len(even)==0:
	print(len(l))
	for x in l:
		print(len(x),*x)
else:
	print(-1)

## 967, lambda for in if break

R=lambda:map(int,input().split())
n,s=R()
r=0
for _ in[0]*n:
    h,m=R();t=60*h+m
    if t>r+s:break
    r=t+s+1
print(r//60,r%60)