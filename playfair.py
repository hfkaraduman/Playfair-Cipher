import cv2
import numpy as geek
import random

resim=cv2.imread("resim.bmp")


secret_key=geek.empty([16,16],dtype=int)

piksel_matris_blue=geek.empty([256,256],dtype=int)
piksel_matris_green=geek.empty([256,256],dtype=int)
piksel_matris_red=geek.empty([256,256],dtype=int)


randomlist = random.sample(range(0, 256), 256)


k=0
for i in range(0,16):
    for j in range(0,16):
        secret_key[i][j]=randomlist[k]
        k+=1


for i in range(0,256):
    for j in range(0,256):
        piksel=resim[i,j]
        piksel_matris_blue[i][j]=(piksel[0])
#print(piksel_matris_blue.size)



for i in range(0,256):
    for j in range(0,256):
        piksel=resim[i,j]
        piksel_matris_green[i][j]=(piksel[1])

for i in range(0,256):
    for j in range(0,256):
        piksel=resim[i,j]
        piksel_matris_red[i][j]=(piksel[2])

print("*****************************")
print(piksel_matris_blue)
print("*****************************")
print(piksel_matris_green)
print("*****************************")
print(piksel_matris_red)



def aynı_satır_mı(deger1,deger2):
    satır_no1=int
    sütun_no1=int
    satır_no2=int
    sütun_no2=int
    for i in range(0,16):
        for j in range(0,16):
            if(secret_key[i][j]==deger1):
                satır_no1=i
                sütun_no1=j
            if(secret_key[i][j]==deger2):
                satır_no2=i
                sütun_no2=j
    if(satır_no1==satır_no2):
        return 1
    else:
        return 0

def aynı_sütun_mu(deger1,deger2):
    satır_no1=int
    sütun_no1=int
    satır_no2=int
    sütun_no2=int
    for i in range(0,16):
        for j in range(0,16):
            if(secret_key[i][j]==deger1):
                satır_no1=i
                sütun_no1=j
            if(secret_key[i][j]==deger2):
                satır_no2=i
                sütun_no2=j
    if(sütun_no1==sütun_no2):
        return 1
    else:
        return 0





def sütun_değiştir_blue(deger1, deger2,satır,sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue
    if (satır_no1 == 15 and sütun_no1 == 15):
        piksel_matris_blue[satır][sütun] = secret_key[0][satır_no1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2 + 1][sütun_no2]
    elif (satır_no2 == 15 and sütun_no2 == 15):
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1 + 1][sütun_no1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[0][sütun_no2]
    elif (satır_no1 == 15):
        piksel_matris_blue[satır][sütun] = secret_key[0][satır_no1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2 + 1][sütun_no2]
    elif (satır_no2 == 15):
        piksel_matris_blue[satır][sütun] = secret_key[sütun_no1 + 1][satır_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[0][sütun_no2]
    else:
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1 + 1][sütun_no1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2 + 1][sütun_no2]


def değiştir_blue(deger1,deger2, piksel_matris_satır,piksel_matris_sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
    piksel_matris_blue[piksel_matris_satır][piksel_matris_sütun]=secret_key[satır_no1][sütun_no2]
    piksel_matris_blue[piksel_matris_satır][piksel_matris_sütun+1] = secret_key[satır_no2][sütun_no1]




def satır_degiştir_blue(deger1, deger2, satır, sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue

    if (sütun_no1 == 15):
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1][0]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2][sütun_no2 + 1]
    elif (sütun_no2 == 15):
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1][sütun_no1 + 1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2][0]
    elif(sütun_no1==15 and satır_no1==15):
        piksel_matris_blue[satır][sütun]=secret_key[0][sütun_no1]
        piksel_matris_blue[satır][sütun+1]=secret_key[satır_no2][sütun_no2+1]
    elif(sütun_no2==15 and satır_no2==15):
        piksel_matris_blue[satır][sütun]=secret_key[satır_no2][sütun_no1+1]
        piksel_matris_blue[satır][sütun+1]=secret_key[0][sütun_no2]
    else:
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1][sütun_no1+1]
        piksel_matris_blue[satır][sütun+1] = secret_key[satır_no2][sütun_no2+1]




for i in range(0,256):
    for j in range(0,256,2):
        if(piksel_matris_blue[i][j]==piksel_matris_blue[i][j+1]):
            continue
        elif(aynı_satır_mı(piksel_matris_blue[i][j],piksel_matris_blue[i][j+1])==1):
            satır_degiştir_blue(piksel_matris_blue[i][j],piksel_matris_blue[i][j+1],i,j)

        elif (aynı_sütun_mu(piksel_matris_blue[i][j], piksel_matris_blue[i][j+1]) == 1):
            sütun_değiştir_blue(piksel_matris_blue[i][j],piksel_matris_blue[i][j+1],i,j)
        else:
            değiştir_blue(piksel_matris_blue[i][j],piksel_matris_blue[i][j+1],i,j)

print("*****************************")
print("BLUE")
print(piksel_matris_blue)


print("****___________________________*******")

def sütun_değiştir_green(deger1, deger2,satır,sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue
    if (satır_no1 == 15 and sütun_no1 == 15):
        piksel_matris_green[satır][sütun] = secret_key[0][satır_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2 + 1][sütun_no2]
    elif (satır_no2 == 15 and sütun_no2 == 15):
        piksel_matris_green[satır][sütun] = secret_key[satır_no1 + 1][sütun_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[0][sütun_no2]
    elif (satır_no1 == 15):
        piksel_matris_green[satır][sütun] = secret_key[0][satır_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2 + 1][sütun_no2]
    elif (satır_no2 == 15):
        piksel_matris_green[satır][sütun] = secret_key[sütun_no1 + 1][satır_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[0][sütun_no2]
    else:
        piksel_matris_green[satır][sütun] = secret_key[satır_no1 + 1][sütun_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2 + 1][sütun_no2]


def değiştir_green(deger1,deger2, piksel_matris_satır,piksel_matris_sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
    piksel_matris_green[piksel_matris_satır][piksel_matris_sütun]=secret_key[satır_no1][sütun_no2]
    piksel_matris_green[piksel_matris_satır][piksel_matris_sütun+1] = secret_key[satır_no2][sütun_no1]




def satır_degiştir_green(deger1, deger2, satır, sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue

    if (sütun_no1 == 15):
        piksel_matris_green[satır][sütun] = secret_key[satır_no1][0]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2][sütun_no2 + 1]
    elif (sütun_no2 == 15):
        piksel_matris_green[satır][sütun] = secret_key[satır_no1][sütun_no1 + 1]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2][0]
    elif (sütun_no1 == 15 and satır_no1 == 15):
        piksel_matris_green[satır][sütun] = secret_key[0][sütun_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2][sütun_no2 + 1]
    elif (sütun_no2 == 15 and satır_no2 == 15):
        piksel_matris_green[satır][sütun] = secret_key[satır_no2][sütun_no1 + 1]
        piksel_matris_green[satır][sütun + 1] = secret_key[0][sütun_no2]
    else:
        piksel_matris_green[satır][sütun] = secret_key[satır_no1][sütun_no1+1]
        piksel_matris_green[satır][sütun+1] = secret_key[satır_no2][sütun_no2+1]

for i in range(0,256):
    for j in range(0,256,2):
        if(piksel_matris_green[i][j]==piksel_matris_green[i][j+1]):
            continue
        elif(aynı_satır_mı(piksel_matris_green[i][j],piksel_matris_green[i][j+1])==1):
            satır_degiştir_green(piksel_matris_green[i][j],piksel_matris_green[i][j+1],i,j)

        elif (aynı_sütun_mu(piksel_matris_green[i][j], piksel_matris_green[i][j+1]) == 1):
            sütun_değiştir_green(piksel_matris_green[i][j],piksel_matris_green[i][j+1],i,j)
        else:
            değiştir_green(piksel_matris_green[i][j],piksel_matris_green[i][j+1],i,j)

print("*****************************")
print("GREEN")
print(piksel_matris_green)

print("****___________________________*******")

def sütun_değiştir_red(deger1, deger2,satır,sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue
    if (satır_no1 == 15 and sütun_no1==15):
        piksel_matris_red[satır][sütun] = secret_key[0][satır_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2 + 1][sütun_no2]
    elif (satır_no2 == 15 and sütun_no2==15):
        piksel_matris_red[satır][sütun] = secret_key[satır_no1+1][sütun_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[0][sütun_no2]
    elif (satır_no1 == 15):
        piksel_matris_red[satır][sütun] = secret_key[0][satır_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2 + 1][sütun_no2]
    elif (satır_no2 == 15):
        piksel_matris_red[satır][sütun] = secret_key[sütun_no1 + 1][satır_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[0][sütun_no2]
    else:
        piksel_matris_red[satır][sütun] = secret_key[satır_no1 + 1][sütun_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2 + 1][sütun_no2]


def değiştir_red(deger1,deger2, piksel_matris_satır,piksel_matris_sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
    piksel_matris_red[piksel_matris_satır][piksel_matris_sütun]=secret_key[satır_no1][sütun_no2]
    piksel_matris_red[piksel_matris_satır][piksel_matris_sütun+1] = secret_key[satır_no2][sütun_no1]




def satır_degiştir_red(deger1, deger2, satır, sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue

    if (sütun_no1 == 15):
        piksel_matris_red[satır][sütun] = secret_key[satır_no1][0]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2][sütun_no2 + 1]
    elif (sütun_no2 == 15):
        piksel_matris_red[satır][sütun] = secret_key[satır_no1][sütun_no1 + 1]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2][0]
    elif (sütun_no1 == 15 and satır_no1 == 15):
        piksel_matris_red[satır][sütun] = secret_key[0][sütun_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2][sütun_no2 + 1]
    elif (sütun_no2 == 15 and satır_no2 == 15):
        piksel_matris_red[satır][sütun] = secret_key[satır_no2][sütun_no1 + 1]
        piksel_matris_red[satır][sütun + 1] = secret_key[0][sütun_no2]
    else:
        piksel_matris_red[satır][sütun] = secret_key[satır_no1][sütun_no1+1]
        piksel_matris_red[satır][sütun+1] = secret_key[satır_no2][sütun_no2+1]

for i in range(0,256):
    for j in range(0,256,2):
        if(piksel_matris_red[i][j]==piksel_matris_red[i][j+1]):
            continue
        elif(aynı_satır_mı(piksel_matris_red[i][j],piksel_matris_red[i][j+1])==1):
            satır_degiştir_red(piksel_matris_red[i][j],piksel_matris_red[i][j+1],i,j)

        elif (aynı_sütun_mu(piksel_matris_red[i][j], piksel_matris_red[i][j+1]) == 1):
            sütun_değiştir_red(piksel_matris_red[i][j],piksel_matris_red[i][j+1],i,j)
        else:
            değiştir_red(piksel_matris_red[i][j],piksel_matris_red[i][j+1],i,j)

print("*****************************")
print("RED")
print(piksel_matris_red)

şifreli_resim=geek.empty([256,256,3],dtype=int)
for i in range(0,256):
    for j in range(0,256):
        şifreli_resim[i][j][0]=125
        şifreli_resim[i][j][1] = 125
        şifreli_resim[i][j][2] = 125
        #şifreli_resim.itemset((i, j, 1), piksel_matris_green[i][j])
        #şifreli_resim.itemset((i, j, 2), piksel_matris_red[i][j])
for i in range(0,256):
    for j in range(0,256):
        şifreli_resim[i][j][0]=piksel_matris_blue[i,j]
        şifreli_resim[i][j][1] = piksel_matris_green[i,j]
        şifreli_resim[i][j][2] = piksel_matris_red[i,j]
        #şifreli_resim.itemset((i, j, 1), piksel_matris_green[i][j])
        #şifreli_resim.itemset((i, j, 2), piksel_matris_red[i][j])




cv2.imwrite("sifreliresim.bmp",şifreli_resim)
print("******************************************************************")

resim2=cv2.imread("sifreliresim.bmp")

for i in range(0,256):
    for j in range(0,256):
        piksel=resim2[i,j]
        piksel_matris_blue[i][j]=(piksel[0])

for i in range(0,256):
    for j in range(0,256):
        piksel=resim2[i,j]
        piksel_matris_green[i][j]=(piksel[1])

for i in range(0,256):
    for j in range(0,256):
        piksel=resim2[i,j]
        piksel_matris_red[i][j]=(piksel[2])









def de_sütun_değiştir_blue(deger1, deger2,satır,sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue
    if (satır_no1 == 0 and sütun_no1 == 0):
        piksel_matris_blue[satır][sütun] = secret_key[15][satır_no1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2 - 1][sütun_no2]
    elif (satır_no2 == 0 and sütun_no2 == 0):
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1 - 1][sütun_no1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[15][sütun_no2]
    elif (satır_no1 == 0):
        piksel_matris_blue[satır][sütun] = secret_key[15][satır_no1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2 - 1][sütun_no2]
    elif (satır_no2 == 0):
        piksel_matris_blue[satır][sütun] = secret_key[sütun_no1 - 1][satır_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[15][sütun_no2]
    else:
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1 - 1][sütun_no1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2 - 1][sütun_no2]


def de_değiştir_blue(deger1,deger2, piksel_matris_satır,piksel_matris_sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
    piksel_matris_blue[piksel_matris_satır][piksel_matris_sütun]=secret_key[satır_no1][sütun_no2]
    piksel_matris_blue[piksel_matris_satır][piksel_matris_sütun+1] = secret_key[satır_no2][sütun_no1]




def de_satır_degiştir_blue(deger1, deger2, satır, sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue

    if (sütun_no1 == 0):
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1][15]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2][sütun_no2 - 1]
    elif (sütun_no2 == 0):
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1][sütun_no1 - 1]
        piksel_matris_blue[satır][sütun + 1] = secret_key[satır_no2][15]
    elif(sütun_no1==0 and satır_no1==0):
        piksel_matris_blue[satır][sütun]=secret_key[15][sütun_no1]
        piksel_matris_blue[satır][sütun+1]=secret_key[satır_no2][sütun_no2-1]
    elif(sütun_no2==0 and satır_no2==0):
        piksel_matris_blue[satır][sütun]=secret_key[satır_no2][sütun_no1-1]
        piksel_matris_blue[satır][sütun+1]=secret_key[15][sütun_no2]
    else:
        piksel_matris_blue[satır][sütun] = secret_key[satır_no1][sütun_no1-1]
        piksel_matris_blue[satır][sütun+1] = secret_key[satır_no2][sütun_no2-1]




for i in range(0,256):
    for j in range(0,256,2):
        if(piksel_matris_blue[i][j]==piksel_matris_blue[i][j+1]):
            continue
        elif(aynı_satır_mı(piksel_matris_blue[i][j],piksel_matris_blue[i][j+1])==1):
            de_satır_degiştir_blue(piksel_matris_blue[i][j],piksel_matris_blue[i][j+1],i,j)

        elif (aynı_sütun_mu(piksel_matris_blue[i][j], piksel_matris_blue[i][j+1]) == 1):
            de_sütun_değiştir_blue(piksel_matris_blue[i][j],piksel_matris_blue[i][j+1],i,j)
        else:
            de_değiştir_blue(piksel_matris_blue[i][j],piksel_matris_blue[i][j+1],i,j)

print("*****************************")
print("BLUE")
print(piksel_matris_blue)

def de_sütun_değiştir_green(deger1, deger2,satır,sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue
    if (satır_no1 == 0 and sütun_no1 == 0):
        piksel_matris_green[satır][sütun] = secret_key[15][satır_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2 - 1][sütun_no2]
    elif (satır_no2 == 0 and sütun_no2 == 0):
        piksel_matris_green[satır][sütun] = secret_key[satır_no1 - 1][sütun_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[15][sütun_no2]
    elif (satır_no1 == 0):
        piksel_matris_green[satır][sütun] = secret_key[15][satır_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2 - 1][sütun_no2]
    elif (satır_no2 == 0):
        piksel_matris_green[satır][sütun] = secret_key[sütun_no1 - 1][satır_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[15][sütun_no2]
    else:
        piksel_matris_green[satır][sütun] = secret_key[satır_no1 - 1][sütun_no1]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2 - 1][sütun_no2]


def de_değiştir_green(deger1,deger2, piksel_matris_satır,piksel_matris_sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
    piksel_matris_green[piksel_matris_satır][piksel_matris_sütun]=secret_key[satır_no1][sütun_no2]
    piksel_matris_green[piksel_matris_satır][piksel_matris_sütun+1] = secret_key[satır_no2][sütun_no1]




def de_satır_degiştir_green(deger1, deger2, satır, sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue

    if (sütun_no1 == 0):
        piksel_matris_green[satır][sütun] = secret_key[satır_no1][15]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2][sütun_no2 - 1]
    elif (sütun_no2 == 0):
        piksel_matris_green[satır][sütun] = secret_key[satır_no1][sütun_no1 - 1]
        piksel_matris_green[satır][sütun + 1] = secret_key[satır_no2][15]
    elif(sütun_no1==0 and satır_no1==0):
        piksel_matris_green[satır][sütun]=secret_key[15][sütun_no1]
        piksel_matris_green[satır][sütun+1]=secret_key[satır_no2][sütun_no2-1]
    elif(sütun_no2==0 and satır_no2==0):
        piksel_matris_green[satır][sütun]=secret_key[satır_no2][sütun_no1-1]
        piksel_matris_green[satır][sütun+1]=secret_key[15][sütun_no2]
    else:
        piksel_matris_green[satır][sütun] = secret_key[satır_no1][sütun_no1-1]
        piksel_matris_green[satır][sütun+1] = secret_key[satır_no2][sütun_no2-1]




for i in range(0,256):
    for j in range(0,256,2):
        if(piksel_matris_green[i][j]==piksel_matris_green[i][j+1]):
            continue
        elif(aynı_satır_mı(piksel_matris_green[i][j],piksel_matris_green[i][j+1])==1):
            de_satır_degiştir_green(piksel_matris_green[i][j],piksel_matris_green[i][j+1],i,j)

        elif (aynı_sütun_mu(piksel_matris_green[i][j], piksel_matris_green[i][j+1]) == 1):
            de_sütun_değiştir_green(piksel_matris_green[i][j],piksel_matris_green[i][j+1],i,j)
        else:
            de_değiştir_green(piksel_matris_green[i][j],piksel_matris_green[i][j+1],i,j)

print("*****************************")
print("GREEN")
print(piksel_matris_green)


def de_sütun_değiştir_red(deger1, deger2,satır,sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue
    if (satır_no1 == 0 and sütun_no1 == 0):
        piksel_matris_red[satır][sütun] = secret_key[15][satır_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2 - 1][sütun_no2]
    elif (satır_no2 == 0 and sütun_no2 == 0):
        piksel_matris_red[satır][sütun] = secret_key[satır_no1 - 1][sütun_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[15][sütun_no2]
    elif (satır_no1 == 0):
        piksel_matris_red[satır][sütun] = secret_key[15][satır_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2 - 1][sütun_no2]
    elif (satır_no2 == 0):
        piksel_matris_red[satır][sütun] = secret_key[sütun_no1 - 1][satır_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[15][sütun_no2]
    else:
        piksel_matris_red[satır][sütun] = secret_key[satır_no1 - 1][sütun_no1]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2 - 1][sütun_no2]


def de_değiştir_red(deger1,deger2, piksel_matris_satır,piksel_matris_sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
    piksel_matris_red[piksel_matris_satır][piksel_matris_sütun]=secret_key[satır_no1][sütun_no2]
    piksel_matris_red[piksel_matris_satır][piksel_matris_sütun+1] = secret_key[satır_no2][sütun_no1]




def de_satır_degiştir_red(deger1, deger2, satır, sütun):
    satır_no1 = int
    sütun_no1 = int
    satır_no2 = int
    sütun_no2 = int
    for i in range(0, 16):
        for j in range(0, 16):
            if (secret_key[i][j] == deger1):
                satır_no1 = i
                sütun_no1 = j
                continue
            if (secret_key[i][j] == deger2):
                satır_no2 = i
                sütun_no2 = j
                continue

    if (sütun_no1 == 0):
        piksel_matris_red[satır][sütun] = secret_key[satır_no1][15]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2][sütun_no2 - 1]
    elif (sütun_no2 == 0):
        piksel_matris_red[satır][sütun] = secret_key[satır_no1][sütun_no1 - 1]
        piksel_matris_red[satır][sütun + 1] = secret_key[satır_no2][15]
    elif(sütun_no1==0 and satır_no1==0):
        piksel_matris_red[satır][sütun]=secret_key[15][sütun_no1]
        piksel_matris_red[satır][sütun+1]=secret_key[satır_no2][sütun_no2-1]
    elif(sütun_no2==0 and satır_no2==0):
        piksel_matris_red[satır][sütun]=secret_key[satır_no2][sütun_no1-1]
        piksel_matris_red[satır][sütun+1]=secret_key[15][sütun_no2]
    else:
        piksel_matris_red[satır][sütun] = secret_key[satır_no1][sütun_no1-1]
        piksel_matris_red[satır][sütun+1] = secret_key[satır_no2][sütun_no2-1]




for i in range(0,256):
    for j in range(0,256,2):
        if(piksel_matris_red[i][j]==piksel_matris_red[i][j+1]):
            continue
        elif(aynı_satır_mı(piksel_matris_red[i][j],piksel_matris_red[i][j+1])==1):
            de_satır_degiştir_red(piksel_matris_red[i][j],piksel_matris_red[i][j+1],i,j)

        elif (aynı_sütun_mu(piksel_matris_red[i][j], piksel_matris_red[i][j+1]) == 1):
            de_sütun_değiştir_red(piksel_matris_red[i][j],piksel_matris_red[i][j+1],i,j)
        else:
            de_değiştir_red(piksel_matris_red[i][j],piksel_matris_red[i][j+1],i,j)

print("*****************************")
print("GREEN")
print(piksel_matris_red)




deşifreli_resim=geek.empty([256,256,3],dtype=int)
for i in range(0,256):
    for j in range(0,256):
        deşifreli_resim[i][j][0]=125
        deşifreli_resim[i][j][1] = 125
        deşifreli_resim[i][j][2] = 125
        #şifreli_resim.itemset((i, j, 1), piksel_matris_green[i][j])
        #şifreli_resim.itemset((i, j, 2), piksel_matris_red[i][j])
for i in range(0,256):
    for j in range(0,256):
        deşifreli_resim[i][j][0]=piksel_matris_blue[i,j]
        deşifreli_resim[i][j][1] = piksel_matris_green[i,j]
        deşifreli_resim[i][j][2] = piksel_matris_red[i,j]

cv2.imwrite("desifreliresim.bmp",deşifreli_resim)






cv2.waitKey(0)
cv2.destroyAllWindows()





























































