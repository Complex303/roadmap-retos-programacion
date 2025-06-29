
"""
Un callback es una función que se pasa como argumento a otra función, 
para que esa otra función la ejecute en algún momento (como una "llamada de vuelta")."""


def saludar():
    print("¡Hola, Eddy!")

def ejecutar_callback(callback):
    print("Voy a llamar al callback ahora...")
    callback()  # Aquí se ejecuta la función que se pasó como argumento

# Llamamos a la función y le pasamos otra función como callback
ejecutar_callback(saludar)


""" * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado."""

import random      # Para generar tiempos de espera aleatorios
import time        # Para simular tiempos de espera usando sleep
import threading   # Para crear hilos que ejecuten procesos en paralelo


#dish_name: el nombre del plato confirm_callback, ready_callback, delivered_callback: funciones (callbacks) que se van a ejecutar en distintos momentos del pedido.
def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback):
    # Definimos una función interna que hace el proceso completo del pedido
    def process():
        # Paso 1: Confirmar el pedido llamando a la función confirm_callback
        confirm_callback(dish_name)
        
        # Esperamos de 1 a 10 segundos simulando que están preparando el pedido
        time.sleep(random.randint(1, 10))
        
        # Paso 2: Avisar que el pedido está listo
        ready_callback(dish_name)
        
        # Esperamos de 1 a 10 segundos simulando que están entregando el pedido
        time.sleep(random.randint(1, 10))
        
        # Paso 3: Avisar que el pedido ha sido entregado
        delivered_callback(dish_name)

    # Creamos un nuevo hilo para que este proceso se ejecute en paralelo con otros
    threading.Thread(target=process).start()
   


def confirm_order(dish_name: str):
    # Muestra un mensaje cuando se confirma el pedido
    print(f"Tu pedido {dish_name} ha sido confirmado")

def order_ready(dish_name: str):
    # Muestra un mensaje cuando el pedido está listo
    print(f"Tu pedido {dish_name} está listo")

def order_delivered(dish_name: str):
    # Muestra un mensaje cuando el pedido ha sido entregado
    print(f"Tu pedido {dish_name} ha sido entregado")


# Simulamos varios pedidos distintos, todos usando las mismas funciones callback
#Se hacen 4 pedidos diferentes.Todos pasan por el mismo proceso. Como se usan hilos, todos se procesan en paralelo y los mensajes pueden salir en diferente orden.
order_process("Pizza de Quezo", confirm_order, order_ready, order_delivered)
order_process("Pizza de Peperoni", confirm_order, order_ready, order_delivered)
order_process("Pizza de Barbacoa", confirm_order, order_ready, order_delivered)
order_process("Pizza de Jamon y Quezo", confirm_order, order_ready, order_delivered)

