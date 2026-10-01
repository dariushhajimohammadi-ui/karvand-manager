# # ---------------------4----------------------
# #برای گرفتن یک عدد شانسی
# from random import randint
# pc_ch = randint(0,20)
# # حلقه به تعداد فرصت های بازی
# for i in range(1,6):
#     print(f'lap{i}of{'5'}')
#     print('-'*40)
#     py_ch = int(input('enter your choice:'))
#     if py_ch < pc_ch:
#         print("guess higher")
#     elif py_ch > pc_ch:
#         print("guess lower")
#     elif pc_ch == py_ch:
#         print('you won')
#         break
# # زمانی که توی تعداد مجاز برنده نشه
# else:
#     print(f'you lost nummber is{pc_ch}')
# ---------------------5-----------------------
# book ={}
# while True :
#     print('-'*40)
#     print('1)add \n2)search \n3)show \n4)exit')
#     ch = input('enter your choice: ')
#     # در صورت انتخاب نکردن عدد
#     if  not ch.isnumeric:
#         print('error choice num')
#         continue
#     # شرط انتخاب مورد ها
#     match int(ch):
#         # برای اضافه کردن کتاب و نویسنده 
#         case 1 :
#             print('-'*40)
#             name_book= input('enter neme book: ')
#             name_Author = input("enter Author's Name: ")
#             book[name_book] = name_Author
#         # پیدا کردن نویسنده یک کتاب 
#         case 2:
#             print('-'*40)
#             name_book= input('enter neme book:')
#             print(book.get(name_book,'not found'))
#         # نمایش تمام کتاب ها 
#         case 3:
#             print('-'*40)
#             print(book)
#         # خروج از برنامه 
#         case 4:
#             print('-'*40)
#             print('good bye')
#             break
#         # برای وارد کردن عددهایی به جز ۱-۴
#         case _:
#             print('-'*40)
#             print('error choice 1 or 2 or 3 or 4')
#             continue
# ---------------------------6---------------------------
Store_Products ={}
while True:
    print('-'*40)
    print('1)add \n2)sell \n3)search \n4)show \n5)save \n6)report \n7)exit')
    ch = input('enter your choice: ')
    # در صورت انتخاب نکردن یک عدد 
    if  not ch.isnumeric():
        print('error choice num')
        continue
    #برای پاک کردن چیز های که  موجودی شون صفر شده   
    for i in list(Store_Products.keys()): 
        if Store_Products[i] <= 0:
            del Store_Products[i]
    # شرط انتخاب مورد ها 
    match int(ch):
        # کردن یک کالای جدید یا بیشتر کردن کالای موجودadd
        case 1:
            print('-'*40)
            name = input('enter Product Name: ')
            quantity = int(input('enter Product Quantity: '))
            if name in Store_Products:
                Store_Products[name] = Store_Products[name] + quantity
                continue
            Store_Products[name] = quantity
        # فروش یک کالای موجود
        case 2:
            print('-'*40)
            name = input('enter Product Name: ')
            quantity = int(input('enter Product Quantity: '))
            if name in Store_Products:
                if quantity <= Store_Products[name] :
                    Store_Products[name] = Store_Products[name] - quantity
                    print(f'{quantity} units sold')
                    print(f'{Store_Products[name]} Remaining Quantity')
                    continue
                else:
                    print('This product is not available in this quantity.')
                    continue
            print('This product is not available in the store.')
        #   گشتن دنبال یک کالا و در صورت وجود نمایش میزان موجودی
        case 3:
            print('-'*40)
            name = input('enter Product Name: ')
            print(Store_Products.get(name,'not found'))
        # نمایش کل موجودی 
        case 4:
            print('-'*40)
            for i in Store_Products:
                print(i,'-',Store_Products[i])
        # txt ذخیره کردن توی یک فایل 
        case 5:
            print('-'*40)
            with open('store.txt','a') as f:
                for i in Store_Products: 
                    f.write(i+'-'+str(Store_Products[i])+'\n')
            print('save')
        # تعداد کالا های موجود و مجموع کالاها و کالای دارای بیشترین موجودی و کمترین موجودی
        case 6:
            print('-'*40)
            name_min=''
            name_max = ''
            mx = 0
            total = 0
            m = []
            for i in Store_Products: 
                if Store_Products[i] > 0:
                    print(i ,'-',Store_Products[i])
                if Store_Products[i]> mx:
                    mx = Store_Products[i]
                    name_mx = i 
                total += Store_Products[i]
            mn = mx 
            for i in Store_Products:
                if Store_Products[i] < mn:
                    mn = Store_Products[i]
                    name_min = i
            print(f'Product with the highest stock level {name_mx} - {mx}')
            print(f'Product with the highest stock level {name_min} - {mn}')
            print('total =',total)  
        #خروج از برنامه    
        case 7:
            print('-'*40)
            print('good bye')
            break
        # درصورت انتخاب اشتباه 
        case _:
            print('-'*40)
            print('error choice 1-7')
            continue

