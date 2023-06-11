# from datetime import datetime
# import time

# print(35*"=","WELCOME TO GRMART",35*"=")
# name=input("enter your name :")
# lists='''
# 1.	Mango          =    RS 80/kg
# 2.	Banana         =    Rs 40/DZ
# 3.	Grapes         =    Rs 60/kg
# 4.	Berries        =    Rs 70/kg
# 5.	Apples         =    Rs 200/kg
# 6.	Citrus fruits  =    Rs 50/kg
# 7.	Peaches        =    Rs 100/kg
# 8.	Coconut        =    Rs 30/ps
# 9.	Pears          =    Rs 90/kg
# 10.	Pineapples     =    Rs 30/ps
# '''
# # print(lists)
# price=0
# pricelist=[]
# totalprice=0
# finalprice=0
# ilist=[]
# qlist=[]
# plist=[]

# items={'Mango':80,'Banana':40,'Grapes':60,'Berries':70,'Apples':200,'Citrus fruits':50,'Peaches':100,'Coconut':30,'Pears':90,'Pineapples':30 }

# option=int(input("For list of items press 1:"))
# if option==1:
#      print(lists)
#      for i in range(len(items)):
#           inp1=int(input("If you want to buy press 1 or 2 for exit:"))
#           if inp1==2:
#                break
#           if inp1==1:
#                item=input("Enter your items :")
#                QTY=int(input("Enter your QTY :"))
#                if item in items.keys():
#                     price=QTY*(items[item])
#                     # print(price)                    
#                     pricelist.append((item,QTY,items,price))
#                     totalprice+=price
#                     ilist.append(item)
#                     qlist.append(QTY)
#                     plist.append(price)
#                     gst=(totalprice*5)/100
#                     final_amount=gst+totalprice
#                else:
#                     print("what you enter item is not avaliable")
#           else:
#                print("what you entered is wrong number")
#           int=input("can i print your bill yes or no :")
#           if input=='yes':
#                pass
#           if final_amount!=0:
#                print(50*"=","GRMart",50*"=")
#                print(50*"=","Bangalore",50*"=")
#                print("name:",name,50*" ","Date:",datetime.now())
#                print(110*"-")
#                print("S.no",25*" ","Item",25*" ","QTY",26*" ","price")
               
#           for i in range (len(pricelist)):
#                print(i,28*" ",ilist[i],23*" ",plist[i],23*" ",qlist[i])
#                print(110*"-")
#                print(75*" ",'Total Amount :','RS',totalprice)
#                print(77*" ",'GST Amount :','RS',gst)  
#                print(110*"-")             
#                print(75*" ",'final_amount :','RS',final_amount)
#                print(110*"-")
#                print(35*" ","Thanks for visiting to GRMart",35*" ")
#                print(110*"-")







# print(35*"=","WELCOME TO GRMART",35*"=")
# import datetime
# currentTime = datetime.datetime.now()
# currentTime.hour
# gender=int(input('''
# 1.Male
# 2.Female
# 3.Others
# '''))
# name=input("enter your name :")
# if gender==1:
#      if currentTime.hour < 12:
#           print('Good morning',name,'sir')
#      elif 12 <= currentTime.hour < 18:
#           print('Good afternoon',name,'sir')
#      else:
#           print('Good evening sir.')
# elif gender==2:
#      if currentTime.hour < 12:
#           print('Good morning Madam.')
#      elif 12 <= currentTime.hour < 18:
#           print('Good afternoon,Madam.')
#      else:
#           print('Good evening Madam.')
# else:
#      if currentTime.hour < 12:
#           print('Good morning.')
#      elif 12 <= currentTime.hour < 18:
#           print('Good afternoon.')
#      else:
#           print('Good evening.')
# lists='''
# Mango          =    RS 80/kg
# Banana         =    Rs 40/DZ
# Grapes         =    Rs 60/kg
# Berries        =    Rs 70/kg
# Apples         =    Rs 200/kg
# Citrus fruits  =    Rs 50/kg
# Peaches        =    Rs 100/kg
# Coconut        =    Rs 30/ps
# Pears          =    Rs 90/kg
# Pineapples    =    Rs 30/ps
# '''
# # print(lists)
# price=0
# pricelist=[]
# totalprice=0
# finalprice=0
# ilist=[]
# qlist=[]
# plist=[]

# items={'Mango':80,'Banana':40,'Grapes':60,'Berries':70,'Apples':200,'Citrus fruits':50,'Peaches':100,'Coconut':30,'Pears':90,'Pineapples':30 }

# option=int(input('''
# 1.list of items
# 2.for exit
# '''))
# if option==1:
#      print(lists)
# for i in range(len(items)):
#      inp1=int(input("press-1 for continue press-2 for exit :"))
#      if inp1==2:
#           break
#      if inp1==1:
#           item=input("Enter your items :")
#           QTY=int(input("Enter your QTY :"))
#           if item in items.keys():
#                price=QTY*(items[item])
#                     # print(price)                    
#                pricelist.append((item,QTY,items,price))
#                totalprice+=price
#                ilist.append(item)
#                qlist.append(QTY)
#                plist.append(price)
#                gst=(totalprice*5)/100
#                final_amount=gst+totalprice
#           else:
#                print("what you enter item is not avaliable")
#      else:
#           print("what you entered is wrong number")

#      int=input('''
#      1.for billing
#      ''')
#      if input=='1':
#           pass 
#           if final_amount!=0:
#                print(50*"=","GRMart",50*"=")
#                print(50*"=","Bangalore",50*"=")
#                print("name:",name,50*" ","Date:",datetime.now())
#                print(110*"-")
#                print("S.no",25*" ","Item",25*" ","QTY",26*" ","price")
                         
#                for i in range (len(pricelist)):
#                     print(i,28*" ",ilist[i],23*" ",plist[i],23*" ",qlist[i])
#                     print(110*"-")
#                     print(75*" ",'Total Amount :','RS',totalprice)
#                     print(77*" ",'GST Amount :','RS',gst)  
#                     print(110*"-")             
#                     print(75*" ",'final_amount :','RS',final_amount)
#                     print(110*"-")
#                     print(35*" ","Thanks for visiting to GRMart",35*" ")
#                     print(110*"-")












from datetime import datetime
import time
import datetime
print(35*"=","WELCOME TO GRMART",35*"=")

currentTime = datetime.datetime.now()
currentTime.hour
gender=int(input(''' please enter your gender :
1.Male
2.Female
3.Others
'''))
name=input("enter your name :")
if gender==1:
     if currentTime.hour < 12:
          print('Good morning',name,'sir')
     elif 12 <= currentTime.hour < 18:
          print('Good afternoon',name,'sir')
     else:
          print('Good evening sir.')
elif gender==2:
     if currentTime.hour < 12:
          print('Good morning',name,'Madam')
     elif 12 <= currentTime.hour < 18:
          print('Good afternoon',name,'Madam')
     else:
          print('Good evening',name,'Madam')
else:
     if currentTime.hour < 12:
          print('Good morning',name)
     elif 12 <= currentTime.hour < 18:
          print('Good afternoon',name)
     else:
          print('Good evening',name)
lists='''
1.	Mango          =    RS 80/kg
2.	Banana         =    Rs 40/dzn
3.	Grapes         =    Rs 60/kg
4.	Berries        =    Rs 70/kg
5.	Apples         =    Rs 200/kg
6.	Citrus fruits  =    Rs 50/kg
7.	Peaches        =    Rs 100/kg
8.	Coconut        =    Rs 30/pcs
9.	Pears          =    Rs 90/kg
10.	Pineapples     =    Rs 30/ps
'''
# print(lists)
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items={'Mango':80,'Banana':40,'Grapes':60,'Berries':70,'Apples':200,'Citrus fruits':50,'Peaches':100,'Coconut':30,'Pears':90,'Pineapples':30 }

option=int(input("For list of items press 1:"))
if option==1:
     print(lists)
     for i in range(len(items)):
          inp1=int(input("If you want to buy press 1 or 2 for exit:"))
          if inp1==2:
               break
          if inp1==1:
               item=input("Enter your items :")
               QTY=int(input("Enter your QTY :"))
               if item in items.keys():
                    price=QTY*(items[item])
                    # print(price)                    
                    pricelist.append((item,QTY,items,price))
                    totalprice+=price
                    ilist.append(item)
                    qlist.append(QTY)
                    plist.append(price)
                    gst=(totalprice*5)/100
                    final_amount=gst+totalprice
               else:
                    print("what you enter item is not avaliable")
          else:
               print("what you entered is wrong number")
          int=input("can i print your bill yes or no :")
          if input=='yes':
               pass
          if final_amount!=0:
               print(50*"=","GRMart",50*"=")
               print(50*"=","Bangalore",50*"=")
               print("name:",name,50*" ","Date:",datetime.datetime.now())
               print(110*"-")
               print("S.no",25*" ","Item",25*" ","QTY",26*" ","price")
               
          for i in range (len(pricelist)):
               print(i,28*" ",ilist[i],23*" ",plist[i],23*" ",qlist[i])
               print(110*"-")
               print(75*" ",'Total Amount :','RS',totalprice)
               print(77*" ",'GST Amount :','RS',gst)  
               print(110*"-")             
               print(75*" ",'final_amount :','RS',final_amount)
               print(110*"-")
               print(35*" ","Thanks for visiting to GRMart",35*" ")
               print(110*"-")
