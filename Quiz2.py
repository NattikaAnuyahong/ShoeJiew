a = list()

def shop():
  print('..........................\n\n Jiew Happy Shoes\n..........................\n')
  print('Jiew Happy Shoes\n Nike[n]\n Adidas[a]\n Converse[c]\n Rebok[r]\n Exit[x] ')
  b = (input("Please select brand :"))

  if b =='n' :
    print('***********Nike**********')
    print(' 1) Nike Air Force 1 GORE-TEX Low\n 2) Nike Zoom Gravity\n 3) Jordan Mars 270')
    gen1(int(input("Please select Generation :")))

  elif b =='a' :
    print('***********Adidas**********')
    print(' 1) NMD_R1\n 2) SUPERSTAR\n 3) AW FUTURESHELL')
    gen2(int(input("Please select Generation :")))

  elif  b =='c' :
    print('***********Converse**********')
    print(' 1) CHUCK TAYLOR ALL STAR\n 2) JACK PURCELL\n 3) ALL STAR GLOW UP OX WHITE')
    gen3(int(input("Please select Generation :")))
  elif  b =='r' :
    print('***********Rebok**********')
    print(' 1) CHUCK TAYLOR ALL STAR\n 2) JACK PURCELL\n 3) ALL STAR GLOW UP OX WHITE')
    gen3(int(input("Please select Generation :")))
 
  elif  b =='x' : store() 

def gen1(n):
  if n == 1:
    a.append(['Nike Air Force 1 GORE-TEX Low','5500','-1100','4400'])  
    shop()

  elif n == 2:
    a.append(['Nike Zoom Gravity','3300','-660','2640'])
    shop()

  elif n == 3:
    a.append(['Jordan Mars 270:6100:-1220:4880'])
    shop()

def gen2(n):
  if n == 1:
    a.append(['NMD_R1','4600','-1380','3220'])
    shop()

  elif n == 2:
    a.append(['SUPERSTAR','4500','-1350','3150'])
    shop()

  elif n == 3:
    a.append(['AW FUTURESHELL','10000','-3000','7000'])
    shop()

def gen3(n):
  if n == 1:
    a.append(['CHUCK TAYLOR ALL STAR','4600','-1380','3220'])
    shop()

  elif n == 2:
    a.append(['JACK PURCELL','4500','-1350','3150'])
    shop()

  elif n == 3:
    a.append(['ALL STAR GLOW UP OX WHITE','10000','-3000','7000'])
    shop()

def gen4(n):
  if n == 1:
    a.append(['CHUCK TAYLOR ALL STAR','4600','-1380','3220'])
    shop()

  elif n == 2:
    a.append(['JACK PURCELL','4500','-1350','3150'])
    shop()

  elif n == 3:
    a.append(['ALL STAR GLOW UP OX WHITE','10000','-3000','7000'])
    shop()
        
def store():
  sum = 0
  print("                                                 ตารางเเสดงรายการสินค้า                                   ")
  print("-------------------------------------------------------------------------------------------------------------------------------")
  print("ที่           รุ่นรองเท้า                        ราคา                                    ส่วนลด                                  จ่ายจริง")
  print("-------------------------------------------------------------------------------------------------------------------------------")
  count = 0
  for i in a :
    count += 1 
    print(count,end="   ")
    for k in i :
      print(k.ljust(40),end="") 
    print()
  
  for i in range(len(a)) : sum=sum+int(a[i][3])
  print("--------------------------------------------------------------------------------------------------------------------------------")
  print("รวมทั้งสิ้น                                                                                                                     %d"%sum)
  print("--------------------------------------------------------------------------------------------------------------------------------")
  shop()
shop()