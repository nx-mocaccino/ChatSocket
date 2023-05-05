import socket
import time
from tools.reader import read_message
from tools.sender import send_message
PORT = 6969
BUFFER_SIZE = 1024
HEADER= 64
HOST = '127.0.0.1'
FORMAT = 'utf-8'
DISCONNET_MESSAGE = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def start():

    send_message('cliente', client)
    print('Bienvenido al asistente virtual por favor ingrese sus credenciales.')

    rut = input('usuario:')
    send_message(rut, client)

    password = input('constraseña:')
    send_message(password, client)

    response = int(read_message(client)) # Informacion or 0

    if response == 1:
        client_name = read_message(client)
    while response:
        
        print(f'\nAsistente: Hola {client_name}, en qué te podemos ayudar?.')

        print('     (1) Reiniciar Servicio Internet.')
        print('     (2) Reiniciar Clave Wi-Fi.')
        print('     (3) Contactar a un ejecutivo.')
        print('     (4) Salir.')
        request = input('Cliente: ') # Se ingresa la opción que se desea realizar
        
        if request == '1':
            print(f'Asistente: Estimado {client_name}, se ha reiniciado el servicio de internet.') 
            send_message(request, client)
            print(f'Asistente: Se ha reiniciado su Servicio de Internet.')
            
        elif request == '2':

            print(f'\nPor favor, ingresar una nueva contraseña.')
            new_password = input('Clave: ')
            repeat_password = input('Repetir Clave: ')

            while new_password != repeat_password:
                print('Las contraseñas no coinciden, por favor intente nuevamente.')
                print(f'Ingresar nueva contraseña:')
                new_password = input('Clave: ')
                repeat_password = input('Repetir Clave: ')

                   
            print(f'Asistente: Estamos actualizando su clave Wifi.')

            time.sleep(2)    
            send_message(request, client)
            send_message(new_password, client)
            
            print(f'Asistente: Clave actualizada.')

        elif request == '3':
            print(f'Asistente: Estimado cliente, se ha contactado a un ejecutivo.')

        elif request == '4':
            send_message(input('Asistente: Presionar espacio para terminar la conexión'), client)
            send_message(DISCONNET_MESSAGE, client)
            print(f'Asistente: Estimado cliente, se ha cerrado la sesión.')
            response = 0

start()
print('--------------------------------------------------------------------------------')