"""
    Para empezar con la programación de busqueda BFS, primero se debe de
    importar el módulo queue, que sirve para el uso de colas. 
"""
from queue import Queue 
"""
    Se crea la clase con nombre de grafo, con la que se podrá utilizar sus 
    funciones y su constructor para lo que deseamos. 
"""
class Grafo:
    """
        Iniciamos con el constructor, se logra identificarlo ya que siempre
        lleva el mismo nombre. Recibe dos parámetros sin contar el por defecto,
        recibe el número de nodos, y el valor si es diregido o no el grafo. 
    """
    def __init__(self, nummero_de_nodos, dirigido=True):
        '''Asignando valor al atributo numero_de_nodos'''
        """
            Se hace el llamado al valor de número de nodos asignandolo a un  rango,
            por otro lado se debe de saber si el grafo es dirigido o no, para ello
            se utiliza la linea 26
        """
        self.m_nummero_de_nodos = nummero_de_nodos
        self.m_nodos = range(self.m_nummero_de_nodos)
        self.m_dirigido = dirigido
		
        """
            Para acabar con el constructor de la clase, se crea una variable llamada
            m_lista_adyacente, la cual se encarga de crear un diccionario. Dicho
            diccionario implementará una lista adyacente. 
        """
        self.m_lista_adyacente = {nodo: set() for nodo in self.m_nodos} 
    """
        La primera función aparte del constructor será para agregar borde a los nodos. 
        Como parámetro se obtiene el nodo1 y el nodo 2 y el peso de la arista que une esos nodos.
        Para este caso el peso de la arista, es decir, el grsosor será por defecto de 1.
    """
    def agregar_borde(self, nodo1, nodo2, grosor=1):
        '''Agregando el borde'''
        """
            Si el grafo es dirigido se deberá agregar el boorde del nodo 1 que tiene la lista,
            al nodo 2 con su groso por defecto. Mientras que, si el grafo no es dirigido, 
            se agrega el borde en las dos direcciones.
        """
        self.m_lista_adyacente[nodo1].add((nodo2, grosor))
        #En caso de que el grafo no este dirigo.
        if not self.m_dirigido:
            self.m_lista_adyacente[nodo2].add((nodo1, grosor))

    """
        Continuamos con la función que se encargará de dibujar el grafo. Esta clase no tendrá
        ningun parámetro que recibir, simplemente se encuentra el por defecto. 
    """
    def dibujar_grafo(self):
        """
            Para dibujar se usa in ciclo for con una variable llamada llave, con la cual
            se recorrerá la lista adyacente de cada llave. Mientras existas llaves se imprime
            un mensaje con el número de nodos y la lista de dicha llave. 
        """
        for llave in self.m_lista_adyacente.keys():
            print("Nodo", llave, ": ", self.m_lista_adyacente[llave])