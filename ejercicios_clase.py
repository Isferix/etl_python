import bonobo
import time
import requests

# Install bonobo
#   pip3 install -U bonobo 
# Crear archivo "dot"
#   bonobo inspect --graph ejercicios_clase.py > ejercicios_clase.dot
# Graphviz online
#   http://dreampuf.github.io/GraphvizOnline/
# Graphviz (dot) extension
#    Abrir el archivo .dot y presionar CTRL + SHIF + V

archivo = open('ejercicios_clase.txt','w')
archivo.write('')
archivo.close()

def extract():
    # Realice un bucle que recorra una lista del 0 al 10 inclusive
    # En cada iteración de ese bucle realizar un "yield" del valor
    # tomado de la lista
    for i in range(11):
        yield i


def transform(x):
    # Por cada número que ingrese a transform
    # multiplicarlo por 5
    yield x*5


def load(result):
    # Cada resultado que ingrese a este punto
    # ingresarlo como una nueva linea a un archivo
    # de texto (usando open con 'a' y write)
    # o insertando a una base de datos a elección.
    # El objetivo es que quede almacenado en un archivo
    # o una base de datos la tabla del 5
    with open('ejercicios_clase.txt', 'a') as fi:
        fi.write(str(result)+'\n')

    print('Fin!')


def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(extract, transform, load)
    return graph


def get_services(**options):
    return {}


if __name__ == "__main__":
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
