'''
Created on 09-nov-2020

@author: maxus
'''
cuentas = {"sevilla" : [300,450], "madrid" : [400,300], "segovia" : [500,350], "valencia" :
[450,300]} # el primer numero indica ingresos, el segundo gastos.
cuentasMadridYSegovia = cuentas["madrid"]+cuentas["segovia"]
cuentas["sevilla"] = cuentas["sevilla"] + [True]
sumaIngresos = cuentas["sevilla"][0]+cuentas["madrid"][0]+cuentas["segovia"][0]+cuentas["valencia"][0]
print(cuentasMadridYSegovia)
print(sumaIngresos)
print(cuentas)