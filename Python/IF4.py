year=int(input('input your birth year:'))
if(year-2000)%12==0:
 sign='Dragon'
elif(year-2000)%12==1:
    sign='Snake'
elif(year-2000)%12==2:
    sign='Horse'
elif(year-2000)%12==3:
    sign='Sheep'
elif(year-2000)%12==4:
    sign='Monkey'
elif(year-2000)%12==5:
    sign='Rooster'
elif(year-2000)%12==6:
    sign='Dog'
elif(year-2000)%12==7:
    sign='Pig'
elif(year-2000)%12==8:
    sign='Rat'
elif(year-2000)%12==9:
    sign='Ox'
elif(year-2000)%12==10:
    sign='Tiger'
else:
    sign='Hare'

print('Your Zodiac sign:',sign)

print('='*40)
day=int(input('Input birthday :'))
month=input('Input month of birth(e.g. march,july etc):')
if month=='december':
    astro_sign ='Sagitarius' if (day<22) else 'capricorn'
elif month == 'january':
    astro_sign ='Capricorn' if (day<20) else 'aquarius'
elif month == 'february':
    astro_sign ='aquarius' if (day<19) else 'pisces'
elif month == 'march':
    astro_sign ='pisces' if (day<21) else 'aries'
elif month == 'april':
    astro_sign ='aries' if (day<20) else 'taurus'
elif month == 'may':
    astro_sign ='taurus' if (day<21) else 'gemini'
elif month == 'june':
    astro_sign ='gemini' if (day<21) else 'cancer'
elif month == 'july':
    astro_sign ='cancer' if (day<23) else 'leo'
elif month == 'august':
    astro_sign ='leo' if (day<23) else 'virgo'
elif month == 'september':
    astro_sign ='virgo' if (day<23) else 'libra'
elif month == 'oktober':
    astro_sign ='libra' if (day<23) else 'scorpio'
elif month == 'november':
    astro_sign ='scorpio' if (day<22) else 'sagitarius'

print('Your Astrological sign is :',astro_sign)

print('='*40)
p=int(input('Masukkan panjang :'))
l=int(input('Masukkan lebar :'))
t=int(input('Masukkan tinggi :'))

V=p*l*t
L=2*(p*l+p*t+l*t)

print('Volume balok yang anda cari adalah:',V)
print('Luas  balok yang anda cari adalah:',L)

print('='*40)
tinggi=int(input('Masukkan tinggi badan anda :'))
brtideal=(tinggi-100)-((tinggi-100)*10/100)

print('Berat badan ideal kamu adalah:',brtideal)




