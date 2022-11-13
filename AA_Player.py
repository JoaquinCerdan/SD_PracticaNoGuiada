import socket
import sys

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
FIN = "FIN"

# AAEngineIP, AAEnginePort, ColasIP, ColasPort, AARegistryIP, AARegistryPort = 0


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
########## MAIN ##########


print("****** WELCOME TO OUR BRILLIANT SD UA CURSO 2020/2021 SOCKET CLIENT ****")

#Deberían ser 7, pero voy a poner 4 para probar la conexion

if  (len(sys.argv) == 4):
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR_AA_ENGINE = (SERVER, PORT)

    '''
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR_COLAS = (SERVER, PORT)

    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR_AA_REGISTRY = (SERVER, PORT)

    '''
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR_AA_ENGINE)
    print (f"Establecida conexión en [{ADDR_AA_ENGINE}]")

    '''

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR_COLAS)
    print (f"Establecida conexión en [{ADDR_COLAS}]")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR_AA_REGISTRY)
    print (f"Establecida conexión en [{ADDR_AA_REGISTRY}]")

    '''

    
    msg=sys.argv[3]
    while msg != FIN :
        print("Envio al servidor: ", msg)
        send(msg)
        print("Recibo del Servidor: ", client.recv(2048).decode(FORMAT))
        msg=input()

    print("############")
    print("##__MENU__##")
    print("############")
    print()

    print("1-Crear perfil")
    print("2-Editar perfil")
    print("3-Unirse a la partida")
    print()
    menu = input()

    




    print ("SE ACABO LO QUE SE DABA")
    print("Envio al servidor: ", FIN)
    send(FIN)
    client.close()
else:
    print ("Oops!. Parece que algo falló. Necesito estos argumentos: <AAEngineIP> <AAEnginePort> <ColasIP> <ColasPort> <AARegistryIP> <AARegistryPort>")
