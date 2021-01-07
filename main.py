# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def errorhandler():
    return 'opcion invalida'

def salir ():
    exit()

def start():
    archivo = open('text.txt', 'r') #abir archivo
    i = 0
    acumulador = 0

    for j in range(4):
        if j == 0:
            palabra = 'ebay'
        elif j == 1:
            palabra = 'web'
        elif j == 2:
            palabra =  'website'
        elif j == 3:
            palabra = 'webpage'
        elif j == 4:
            palabra = 'webmaster'
        elif j == 5:
            palabra = 'else'
        elif j == 6:
            palabra = 'we'
        elif j == 7:
            palabra = 'webay'
        for line in archivo.readline():  #leer linea por linea
            lista_sin_puntos = line.split(' ')
            texto_sin_puntos =  ' '.join(lista_sin_puntos)
            lista_sin_comas = texto_sin_puntos.split(',')
            texto_sin_comas = ' '.join(lista_sin_comas)
            lista = texto_sin_comas.split()
            i = lista.count(palabra)
            acumulador = acumulador + 1

        if acumulador != 1:
            print(f'La palabra {palabra} se repite {acumulador} veces')
        else:
            print(f'La palabra {palabra} se repite {acumulador} vez')
    archivo.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu = True
    while True:
        print('Menu buscador de palabras\n')
        print('1.- buascar palabras, 2.-Salir')
        opp = int(input('Opcion: '))

        init = {
            1: start,
            2: salir
        }

        init.get(opp, errorhandler)()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
