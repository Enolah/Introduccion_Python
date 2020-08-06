# Vamos a crear un programa que permita gestionar la lista de pacientes que está esperando al médico.
# Cuando llega un nuevo paciente se añade al final de la lista.
# El médico siempre atiende al primer paciente de la lista.

def llega_nuevo_paciente(lista_pacientes, nuevo_paciente):
    """ Añade un nuevo paciente al final de la lista de pacientes.
    """
    lista_pacientes.append(nuevo_paciente)

def medico_atiende_paciente(lista_pacientes):
    """ Elimina el primer paciente de la lista.
    Si la lista está vacía no hace nada.
    """
    if len(lista_pacientes) > 0:
        del lista_pacientes[0]

def imprime_numero_de_pacientes(lista_pacientes):
    """ Imprime por consola el número de pacientes en la lista.
    """
    print("Pacientes esperando:", len(lista_pacientes))

def imprime_lista(lista_pacientes):
    """ Imprime la lista de pacientes
    """
    print("Lista de pacientes esperando:")
    for paciente in lista_pacientes:
        print(paciente)

# Creamos una nueva lista de pacientes
lista_pacientes = []

# Llegan unos cuantos pacientes
llega_nuevo_paciente(lista_pacientes, "Marcos Santos")
llega_nuevo_paciente(lista_pacientes, "Eva González")
llega_nuevo_paciente(lista_pacientes, "Pablo Sánchez")
llega_nuevo_paciente(lista_pacientes, "Ana Pérez")

# Estado actual de la lista de espera
imprime_numero_de_pacientes(lista_pacientes)
imprime_lista(lista_pacientes)

# El médico atiende a un par de ellos
medico_atiende_paciente(lista_pacientes)
medico_atiende_paciente(lista_pacientes)

# Estado actual de la lista de espera
imprime_numero_de_pacientes(lista_pacientes)
imprime_lista(lista_pacientes)