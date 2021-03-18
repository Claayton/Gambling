from random import randint
cont = 0
while True:
    print(f'\033[7;30;47m{"PAR [0]":^25}\033[m\n\033[7;30;47m{"IMPAR [1]":^25}\033[m')
    usu_choose = int(input('Faça a sua escolha: \033[32m'))
    if usu_choose == 0:
        usu_choose = 'PAR'
        pc_choose = 'IMPAR'
    elif usu_choose == 1:
        usu_choose = 'IMPAR'
        pc_choose = 'PAR'
    else:
        print(f'\033[1;31;40m{"ESCOLHA INVALIDA!":^25}\033[m')
        break
    print(f'\033[mSua escolha: \033[32m{usu_choose}\033[m\nEscolha do PC: \033[32m{pc_choose}\033[m')
    print(f'\033[40m{" ":^25}\033[m')
    usu_number = int(input('Voce escolhe o numero: \033[32m'))
    pc_number = randint(0, 10)
    print(f'\033[mPC escolhe o numero: \033[32m{pc_number}\033[m')
    sum = usu_number + pc_number
    if sum % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print(f'A soma foi: \033[32m{sum}\033[m (\033[32m{result}\033[m)')
    if usu_choose == result:
        print(f'\033[1;32;40m{"GANHOU, JOGUE NOVAMENTE!":^25}\033[m')
        cont += 1
    else:
        print(f'\033[1;31;40m{"PERDEU OTARIO!":^25}\033[m')
        break
print(f'\033[32mVoce GANHOU {cont} vezes.\033[m')
