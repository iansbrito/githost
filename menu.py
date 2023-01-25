from flask import request
import json

def menu_pitagoras():
    opt_menu=str(input('''Digite qual lado deseja calcular:\n
     1 - Hipotenusa\n
     2 - Cateto Oposto\n
     3 - Cateto Adjacente\n
     0 - Sair\n>>>'''))

    if opt_menu in '1':
        dados=json.loads(request.data)
        a = str(dados.get('a'))
        b = str(dados.get('b'))
        ca = float(a)
        co = float(b)
        h=((co**2)+(ca**2))**(1/2)
        
        print(f'A hipotenusa é {h}')

    if opt_menu in '2':
        dados=json.loads(request.data)
        a = str(dados.get('a'))
        b = str(dados.get('b'))
        ca = float(a)
        h = float(b)
        co=((h**2)-(ca**2))**(1/2)
        print(f'O cateto oposto é {co}')

    if opt_menu in '3':
        dados=json.loads(request.data)
        a = str(dados.get('a'))
        b = str(dados.get('b'))
        co = float(a)
        h = float(b)
        ca=((h**2)-(ca**2))**(1/2)
        print(f'O cateto adjacente é {ca}')

    #if opt_menu not in ['1','2','3', '0']:


