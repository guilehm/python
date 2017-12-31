sal = float(input('Informe o salário:\nR$:'))
inss = sal * 0.11
if inss > 608.45:
    inss = 608.45
sal_calc = sal - inss
irrf = int(0)
outro_desc = float(input('\nOutros descontos:\nR$:'))

if sal_calc < 2826.65 and sal_calc > 1903.99:
    irrf = (sal_calc * 0.075) - 142.8
if sal_calc > 2826.65 and sal_calc <= 3751.05:
    irrf = (sal_calc * 0.15) - 354.8
if sal_calc >3751.05 and sal_calc <=4664.68:
    irrf = (sal_calc * 0.225) - 636.13
if sal_calc > 4664.68:
    irrf = (sal_calc * 0.275) - 869.36
if sal_calc <=2826.64:
    print('Salário isento de desconto de IRRF.')

sal_liq = sal_calc - irrf - outro_desc
    
print()
print('-'*27)
print('Salário bruto:   R$ {} '.format(round(sal,2)))
print('(-) IRRF:        R$ {} '.format(round(irrf,2)))
print('(-) INSS:        R$ {} '.format(round(inss,2)))
print('(-) Outros Desc. R$ {} '.format(round(outro_desc,2)))
print('Salário liquido: R$ {} '.format(round(sal_liq,2)))
print('-'*27)
