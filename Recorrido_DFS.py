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