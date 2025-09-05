import threading  # Importa o módulo para trabalhar com threads
import time       # Importa o módulo para simular tempo de processamento

def imprimir_1_a_10():
    """
    Função que imprime os números de 1 a 10.
    Utiliza time.sleep() para simular tempo de processamento entre as impressões.
    """
    for i in range(1, 11):  # Loop de 1 até 10 (inclusive)
        print(f"Thread-1: {i}")  # Imprime o número atual com identificação da thread
        time.sleep(0.2)          # Pausa de 0.2 segundos para simular processamento

def imprimir_50_a_60():
    """
    Função que imprime os números de 50 a 60.
    Utiliza time.sleep() para simular tempo de processamento entre as impressões.
    """
    for i in range(50, 61):  # Loop de 50 até 60 (inclusive)
        print(f"Thread-2: {i}")  # Imprime o número atual com identificação da thread
        time.sleep(0.2)           # Pausa de 0.2 segundos para simular processamento

# Criação dos objetos Thread, associando cada um à sua função alvo
thread1 = threading.Thread(target=imprimir_1_a_10)
thread2 = threading.Thread(target=imprimir_50_a_60)

# Inicia as duas threads. Elas começam a executar suas funções simultaneamente.
thread1.start()
thread2.start()

# Aguarda ambas as threads terminarem antes de finalizar o programa principal.
# Isso garante que o programa só termina após as duas sequências serem impressas.
thread1.join()
thread2.join()

print("Programa finalizado. Ambas as threads terminaram.")  #