import tkinter as tk
from tkinter import Canvas

class Estudiante:
    def __init__(self, id_estudiante, nombre, edad, carrera):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

class NodoArbol:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.izquierda = None
        self.derecha = None

class ArbolEstudiantes:
    def __init__(self):
        self.raiz = None

    def insertar(self, estudiante):
        if self.raiz is None:
            self.raiz = NodoArbol(estudiante)
        else:
            self._insertar(self.raiz, estudiante)

    def _insertar(self, nodo, estudiante):
        if estudiante.id_estudiante < nodo.estudiante.id_estudiante:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(estudiante)
            else:
                self._insertar(nodo.izquierda, estudiante)
        elif estudiante.id_estudiante > nodo.estudiante.id_estudiante:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(estudiante)
            else:
                self._insertar(nodo.derecha, estudiante)
        else:
            pass

    def buscar(self, id_estudiante):
        return self._buscar(self.raiz, id_estudiante)

    def _buscar(self, nodo, id_estudiante):
        if nodo is None or nodo.estudiante.id_estudiante == id_estudiante:
            return nodo
        if id_estudiante < nodo.estudiante.id_estudiante:
            return self._buscar(nodo.izquierda, id_estudiante)
        else:
            return self._buscar(nodo.derecha, id_estudiante)

    def eliminar(self, id_estudiante):
        self.raiz = self._eliminar(self.raiz, id_estudiante)

    def _eliminar(self, nodo, id_estudiante):
        if nodo is None:
            return nodo
        if id_estudiante < nodo.estudiante.id_estudiante:
            nodo.izquierda = self._eliminar(nodo.izquierda, id_estudiante)
        elif id_estudiante > nodo.estudiante.id_estudiante:
            nodo.derecha = self._eliminar(nodo.derecha, id_estudiante)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._min_valor_nodo(nodo.derecha)
            nodo.estudiante = temp.estudiante
            nodo.derecha = self._eliminar(nodo.derecha, temp.estudiante.id_estudiante)
        return nodo

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def recorrido_inorden(self, nodo, lista_estudiantes):
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierda, lista_estudiantes)
            lista_estudiantes.append(nodo.estudiante)
            self.recorrido_inorden(nodo.derecha, lista_estudiantes)

    def listar_estudiantes(self):
        lista_estudiantes = []
        self.recorrido_inorden(self.raiz, lista_estudiantes)
        return lista_estudiantes

    def mostrar_arbol(self):
        if self.raiz is None:
            return None

        raiz = tk.Tk()
        raiz.title("Árbol Binario de Búsqueda")
        canvas = Canvas(raiz, width=800, height=600, bg='white')
        canvas.pack()

        def dibujar_nodo(nodo, x, y, dx):
            if nodo is not None:
                canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
                canvas.create_text(x, y, text=str(nodo.estudiante.id_estudiante), font=("Arial", 12))
                if nodo.izquierda is not None:
                    canvas.create_line(x, y, x-dx, y+60)
                    dibujar_nodo(nodo.izquierda, x-dx, y+60, dx//2)
                if nodo.derecha is not None:
                    canvas.create_line(x, y, x+dx, y+60)
                    dibujar_nodo(nodo.derecha, x+dx, y+60, dx//2)

        dibujar_nodo(self.raiz, 400, 50, 200)
        raiz.mainloop()

def main():
    arbol = ArbolEstudiantes()
    
    while True:
        print("\nMenú de Opciones:")
        print("1. Agregar Estudiante")
        print("2. Buscar Estudiante")
        print("3. Eliminar Estudiante")
        print("4. Listar Estudiantes")
        print("5. Exportar Lista de Estudiantes")
        print("6. Mostrar el Árbol")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        match(opcion):
        
            case '1':
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                nombre = input("Ingrese el nombre del estudiante: ")
                edad = int(input("Ingrese la edad del estudiante: "))
                carrera = input("Ingrese la carrera del estudiante: ")
                estudiante = Estudiante(id_estudiante, nombre, edad, carrera)
                arbol.insertar(estudiante)
                print("Estudiante agregado.")
            
            case '2':
                id_estudiante = int(input("Ingrese el ID del estudiante a buscar: "))
                nodo = arbol.buscar(id_estudiante)
                if nodo:
                    estudiante = nodo.estudiante
                    print(f"Estudiante encontrado: ID: {estudiante.id_estudiante}, Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Carrera: {estudiante.carrera}")
                else:
                    print("Estudiante no encontrado.")
            
            case '3':
                id_estudiante = int(input("Ingrese el ID del estudiante a eliminar: "))
                arbol.eliminar(id_estudiante)
                print("Estudiante eliminado.")
            
            case '4':
                lista_estudiantes = arbol.listar_estudiantes()
                for estudiante in lista_estudiantes:
                    print(f"ID: {estudiante.id_estudiante}, Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Carrera: {estudiante.carrera}")
            
            case '5':
                lista_estudiantes = arbol.listar_estudiantes()
                with open("lista_estudiantes.txt", "w") as f:
                    for estudiante in lista_estudiantes:
                        f.write(f"ID: {estudiante.id_estudiante}, Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Carrera: {estudiante.carrera}\n")
                print("Listado de estudiantes exportado a 'lista_estudiantes.txt'.")
            
            case '6':
                arbol.mostrar_arbol()
            
            case '7':
                break
            
            case __:
                print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
