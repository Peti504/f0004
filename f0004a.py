név = input('Kérlek ide add meg a neved. ')
kor = input('Ide kérem szépen a korodat. ') 
kor = int(kor) 
év = input('Milyen évet írunk?' )
év = int(év)
születési_év = év - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')