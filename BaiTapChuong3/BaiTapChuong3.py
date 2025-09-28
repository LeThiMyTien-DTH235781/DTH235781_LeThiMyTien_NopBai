#CÂU 1
print("Chương trình kiểm tra năm nhuần")
year=int(input("Mời bạn nhập vào 1 năm:"))
if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
    print("Năm ", year, " là năm nhuần")
else:
    print("Năm ", year, " không nhuần")

 #CÂU 2
print("Chương trình đếm số ngày trong tháng")
month=int(input("Nhập vào 1 tháng:"))
if month in (1,3,5,7,8,10,12):
 print("Tháng ", month, " có 31 ngày")
elif month in (4,6,9,11):
 print("Tháng ", month, " có 30 ngày")
elif month==2:
 year=int(input("Mời bạn nhập vào năm:"))
 if (year % 4 ==0 and year % 100 != 0) or year % 400==0:
    print("Tháng ",month, " có 29 ngày")
 else:
    print("Tháng ", month, " có 28 ngày")
else:
 print("Tháng ", month, " không hợp lệ")

 #CÂU 3
 #ax^2+bx+c=0
from math import sqrt
print("Chương trình Giải Phương trình bậc 2")
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
if a == 0:
 #bx+c=0
 if b == 0 and c ==0:
    print("Vô số nghiệm")
 elif b==0 and c !=0:
    print("Vô nghiệm")
 else:
     x=-c/b
 print("No x=",x)
else:
 delta=b**2-4*a*c
 if delta <0 :
    print("Vô No")
 elif delta ==0:
    x=-b/(2*a)
    print("No kép x1=x2=",x)
 else:
    x1=(-b-sqrt(delta))/(2*a)
    x2=(-b+sqrt(delta))/(2*a)
    print("x1=",x1)
    print("x2=",x2)

#CÂU 4
x, y, z = 3, 5, 7

print("a:", x == 3)
print("b:", x < y)
print("c:", x >= y)
print("d:", x <= y)
print("e:", x != y - 2)
print("f:", x < 10)
print("g:", x >= 0 and x < 10)
print("h:", x < 0 and x < 10)
print("i:", x >= 0 and x < 2)
print("j:", x < 0 or x < 10)
print("k:", x > 0 or x < 10)
print("l:", x < 0 or x > 10)

#CÂU 5

#Kết quả 
#(a) i=5, j=5, k=7

#(b) i=3, j=5, k=5

#(c) i=7, j=3, k=7

#(d) i=5, j=3, k=3

#(e) i=5, j=3, k=5

#(f) i=7, j=7, k=3

#CÂU 6
def doc_so(n):
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi",
                 "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm",
                   "sáu", "bảy", "tám", "chín"]

    if n < 10:  # 1 chữ số
        return hang_don_vi[n].capitalize()
    elif n < 20:  # từ 10 đến 19
        if n == 10:
            return "Mười"
        else:
            return "Mười " + hang_don_vi[n % 10]
    else:  # 20 -> 99
        chuc = n // 10
        dv = n % 10
        if dv == 0:
            return hang_chuc[chuc].capitalize()
        else:
            return hang_chuc[chuc].capitalize() + " " + hang_don_vi[dv]

#CÂU 7
import datetime

def ngay_ke_tiep(d, m, y):
    try:
        today = datetime.date(y, m, d)
        tomorrow = today + datetime.timedelta(days=1)
        return tomorrow.strftime("%d/%m/%Y")
    except ValueError:
        return "Ngày không hợp lệ!"

#CÂU 8
def tinh_toan(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Lỗi: chia cho 0!"
    else:
        return "Phép toán không hợp lệ!"

#CÂU 9
def tim_quy(thang):
    if 1 <= thang <= 3:
        return "Quý 1"
    elif 4 <= thang <= 6:
        return "Quý 2"
    elif 7 <= thang <= 9:
        return "Quý 3"
    elif 10 <= thang <= 12:
        return "Quý 4"
    else:
        return "Tháng không hợp lệ!"

#CÂU 10
x=int(input("Nhập x:"))
n=int(input("Nhập N:"))
s=0
for i in range(1,n+1):
 tu=x**i
 mau=1
 for j in range(1,i+1):
    mau=mau*j
    s=s+(tu/mau)
    print("s({0},{1})={2}".format(x,n,s))

#CÂU 11
while True:
 n=int(input("Nhập 1 số nguyên dương"))
 dem=0
 for i in range(1,n+1):
     if n % i ==0 :
        dem+=1
 if dem==2:
    print(n,"Là số nguyên tố")
 else:
    print(n,"Không là số nguyên tố")
 hoi=input("Tiếp không Thím?(c/k):")
 if hoi is "k":
    break
print("BYE!")

#CÂU 12
for i in range(1,11):
 for j in range(2,10):
    line="{0}*{1:>2}={2:>2}".format(j,i,i*j)
    print(line,end='\t')
    print()

 #CÂU 13
 a = 0
while a < 100:
    print('*', end='')
    a += 1   # tăng biến a để thoát vòng lặp
print()
# 100 dấu *

#CÂU 14
a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end='')
        b += 1
    print()
    a += 1
# 2000 dấu *

#CÂU 15
#start: giá trị bắt đầu (mặc định = 0).

#stop: giá trị dừng (không bao gồm stop).

#step: bước nhảy (mặc định = 1).

#Nếu step > 0 → dãy tăng dần và dừng trước khi ≥ stop.

#Nếu step < 0 → dãy giảm dần và dừng trước khi ≤ stop.
#Tương đương range(0, 5, 1) Kết quả: [0, 1, 2, 3, 4]

#(b) range(5, 10)

# Bắt đầu từ 5, tăng 1 đến <10 [5, 6, 7, 8, 9]

#(c) range(5, 20, 3)

 #Bắt đầu 5, bước 3, dừng trước 20 [5, 8, 11, 14, 17]

#(d) range(20, 5, -1)

 #Bắt đầu 20, giảm 1, dừng trước khi ≤5  [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

#(e) range(20, 5, -3)
# Bắt đầu 20, giảm 3, dừng trước khi ≤5  [20, 17, 14, 11, 8]

# (f) range(10, 5)

# Mặc định step=1 (tăng dần), nhưng start=10 > stop=5 nên rỗng []

# (g) range(0)

# Tương đương range(0, 0, 1) → không có phần tử []

# (h) range(10, 101, 10)

# Bắt đầu 10, tăng 10, dừng trước 101 [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# (i) range(10, -1, -1)

# Bắt đầu 10, giảm 1, dừng trước khi ≤ -1  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# (j) range(-3, 4)

# Bắt đầu -3, tăng 1, dừng trước 4  [-3, -2, -1, 0, 1, 2, 3]

# (k) range(0, 10, 1)

# Bắt đầu 0, tăng 1, dừng trước 10[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#CÂU 16
for a in range(20, 100, 5):
    print('*', end='')
print()
# Có 16 dấu * được in ra.

# CÂU 17
n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
print("n =", n)

#CÂU 18
n = 5

n = 4  # chiều cao (theo đề minh họa)

# Hình 1: Vuông rỗng
print("Hình 1:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 2: Tam giác vuông
print("\nHình 2:")
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

# Hình 3: Tam giác vuông đối nhau
n = 5
# Tam giác vuông (cạnh góc vuông bên trái)
for i in range(1, n+1):
    print("* " * i)

# Tam giác vuông đối diện (cạnh góc vuông bên phải)
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)



#CÂU 19
import math

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for i in range(n+1):   # từ 0 đến n
    mu = 2*i + 1
    S += (x**mu) / math.factorial(mu)

print("S =", S)

