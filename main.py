hesapA = {
    'ad' : 'Taner Egehan',
    'hesapNo': '123456789',
    'bakiye' : 3000,
    'ekHesap': 2000
}


hesapB = {
    'ad' : 'Caner Egehan',
    'hesapNo': '123123123123123',
    'bakiye' : 2000,
    'ekHesap': 1000
}
def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mi (evet/hayır)')

            if ekHesapKullanimi == 'evet':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye']= 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)

            else:
                print(f'{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bulunmaktadir')
        else:
            print('üzgünüz bakiye yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f'{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} TL bulunmaktadır. Ek hesap limitinizde ise {hesap["ekHesap"]} TL bulunmaktadır..')


paraCek(hesapA,3000)
bakiyeSorgula(hesapA)

print('***********************************')

paraCek(hesapA,2000)
