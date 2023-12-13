import tkinter as tk            
from tkinter import messagebox  
import tkinter.ttk as ttk       
import networkx as nx           
import matplotlib.pyplot as plt 
import heapq                  

# Clase para gestionar los datos de aeropuertos
class Aeropuerto:
    def __init__(self, nombre, ubicacion, codigo):      
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.codigo = codigo

    # Representar el aeropuerto como una cadena de texto
    def __str__(self):                                 
        return self.nombre                              
    
    # Comparar los nombres de los Aeropuertos
    def __lt__(self, other):
        return self.nombre < other.nombre

# Clase para gestionar los datos de las rutas
class Ruta:
    def __init__(self, origen, destino, distancia, tiempo):     
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.tiempo = tiempo

    # Representar la ruta como una cadena de texto
    def __str__(self):                                  
        return f"{self.origen} - {self.destino}" 
    
  
# Clase para la interfaz gráfica
class AeropuertoApp:
    def __init__(self):   
        # Atributos necesarios                          
        self.aeropuertos = []                       
        self.rutas = []                             
        self.aeropuerto_registrado = False
        self.ruta_creada = False

        # Ventana principal
        self.root = tk.Tk()                            
        self.root.title("Gestión de rutas de transporte aéreo")       
        self.root.configure(background='#2F2C2C')      
        self.root.geometry("800x600")                   

        # Crear un frame para los botones y centrarlo en la pantalla
        frame = tk.Frame(self.root, background='#605A58', padx=50, pady=30)
        frame.pack(expand=True)                        

        # Botones principales
        self.registrar_btn = tk.Button(frame, text="Registrar un aeropuerto", command=self.registrar_aeropuerto, width=30, height=3)
        self.crear_ruta_btn = tk.Button(frame, text="Crear una ruta", command=self.crear_ruta, width=30, height=3)
        self.editar_ruta_btn = tk.Button(frame, text="Editar una ruta", command=self.editar_ruta, width=30, height=3)
        self.visualizar_rutas_btn = tk.Button(frame, text="Visualizar las rutas", command=self.visualizar_rutas, width=30, height=3)
        self.buscar_ruta_distancia_btn = tk.Button(frame, text="Búsqueda de rutas por menor distancia", command=self.buscar_ruta_distancia, width=30, height=3)
        self.buscar_ruta_tiempo_btn = tk.Button(frame, text="Busqueda de rutas por menor tiempo", command=self.buscar_ruta_tiempo, width=30, height=3)

        # Centrar los botones horizontalmente, empaquetarlos dentro de la ventana principal
        self.registrar_btn.pack(pady=10)
        self.crear_ruta_btn.pack(pady=10)
        self.editar_ruta_btn.pack(pady=10)
        self.visualizar_rutas_btn.pack(pady=10)
        self.buscar_ruta_distancia_btn.pack(pady=10)
        self.buscar_ruta_tiempo_btn.pack(pady=10)

        # Centrar el frame verticalmente, place coloca el frame en la ventana principal
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Bucle principal de la interfaz
    def run(self):                  
        self.root.mainloop()   
        
    # Mostrar los botones del menu principal
    def mostrar_botones(self):  
        self.registrar_btn.pack(pady=10)
        self.crear_ruta_btn.pack(pady=10)
        self.editar_ruta_btn.pack(pady=10)
        self.visualizar_rutas_btn.pack(pady=10)
        self.buscar_ruta_distancia_btn.pack(pady=10)
        self.buscar_ruta_tiempo_btn.pack(pady=10)    

    # Ocultar los botones del menu princial
    def ocultar_botones(self):
        self.registrar_btn.pack_forget()
        self.crear_ruta_btn.pack_forget()
        self.editar_ruta_btn.pack_forget()
        self.visualizar_rutas_btn.pack_forget()
        self.buscar_ruta_distancia_btn.pack_forget()
        self.buscar_ruta_tiempo_btn.pack_forget()
        
    # Registro de aeropuertos
    def registrar_aeropuerto(self):
    
        self.ocultar_botones()

        # Ventana para registrar los aeropuertos
        registro_frame = tk.Frame(self.root, background='#9E9A99', padx=50, pady=30)
        registro_frame.pack(expand=True)           

        # Campos de entrada, donde el usuario va a escribir y digitar los datos
        nombre_label = tk.Label(registro_frame, text="Nombre:", pady=10, background='#9E9A99')
        nombre_entry = tk.Entry(registro_frame)
        ubicacion_label = tk.Label(registro_frame, text="Ubicación:", pady=10, background='#9E9A99')
        ubicacion_entry = tk.Entry(registro_frame)
        codigo_label = tk.Label(registro_frame, text="Código de Aeropuerto:", pady=10, background='#9E9A99')
        codigo_entry = tk.Entry(registro_frame)

        # Se empaquetan los campos de entrada y los mensajes en la ventana principal
        nombre_label.pack()
        nombre_entry.pack()
        ubicacion_label.pack()
        ubicacion_entry.pack()
        codigo_label.pack()
        codigo_entry.pack()

        # Función para realizar el registro del aeropuerto
        def registrar():
            nombre = nombre_entry.get()         
            ubicacion = ubicacion_entry.get()   
            codigo = codigo_entry.get()        

            # Verificar si ya existe un aeropuerto con el mismo nombre
            aeropuerto_existente = next((a for a in self.aeropuertos if a.nombre == nombre), None)      
            if aeropuerto_existente:
                messagebox.showerror("Error", "Ya existe un aeropuerto con el mismo nombre.")  
                return

            # Crear objeto Aeropuerto y agregarlo a la lista
            aeropuerto = Aeropuerto(nombre, ubicacion, codigo)
            self.aeropuertos.append(aeropuerto)         
            self.aeropuerto_registrado = True         
            messagebox.showinfo("Registro exitoso", "El aeropuerto se registró correctamente.")

            # Limpiar los campos de entrada
            nombre_entry.delete(0, tk.END)
            ubicacion_entry.delete(0, tk.END)
            codigo_entry.delete(0, tk.END)

            # Destruir el frame actual de registro
            registro_frame.destroy()
            self.mostrar_botones()

        # Botón para realizar el registro
        registrar_btn = tk.Button(registro_frame, text="Registrar", command=registrar, pady=10, padx=30)
        registrar_btn.pack(pady=10)

        # Botón para cancelar el registro
        cancelar_btn = tk.Button(registro_frame, text="Cancelar", command=lambda: cancelar_registro(registro_frame), pady=10, padx=30)
        cancelar_btn.pack(pady=10)
        
        def cancelar_registro(frame):
            frame.destroy()
            self.mostrar_botones()

    # Creación de rutas
    def crear_ruta(self):

        if self.aeropuerto_registrado:          
    
            self.ocultar_botones()

            # Crear un frame para el formulario de creación de ruta
            ruta_frame = tk.Frame(self.root, background='#9E9A99', padx=50, pady=30)
            ruta_frame.pack(expand=True)

            # Campos de entrada
            origen_label = tk.Label(ruta_frame, text="Aeropuerto de origen:", pady=10, background='#9E9A99')
            origen_combo = ttk.Combobox(ruta_frame, values=[str(aeropuerto) for aeropuerto in self.aeropuertos])
            
            # Seleccionar el primer aeropuerto por defecto
            origen_combo.current(0)

            # Sellecionar un aeropuerto
            destino_label = tk.Label(ruta_frame, text="Aeropuerto de destino:", pady=10, background='#9E9A99')
            destino_combo = ttk.Combobox(ruta_frame, values=[str(aeropuerto) for aeropuerto in self.aeropuertos])
            destino_combo.current(0) 

            # Campos de entrada para la distancia y el tiempo
            distancia_label = tk.Label(ruta_frame, text="Distancia (en km):", pady=10, background='#9E9A99')
            distancia_entry = tk.Entry(ruta_frame)
            tiempo_label = tk.Label(ruta_frame, text="Tiempo de vuelo (en horas):", pady=10, background='#9E9A99')
            tiempo_entry = tk.Entry(ruta_frame)

            # Se empaquetan los mensajes y los campos de entrada
            origen_label.pack()
            origen_combo.pack()
            destino_label.pack()
            destino_combo.pack()
            distancia_label.pack()
            distancia_entry.pack()
            tiempo_label.pack()
            tiempo_entry.pack()

            # Creación de la ruta
            def crear():
                origen = self.aeropuertos[origen_combo.current()]       
                destino = self.aeropuertos[destino_combo.current()]     
                distancia = distancia_entry.get()                       
                tiempo = tiempo_entry.get()                            

                if origen == destino:              
                    messagebox.showwarning("Advertencia", "El origen y el destino son iguales. Por favor, elige ubicaciones distintas.")
                    return

                #Se crea un objeto ruta con los valores ingresados, y se agrega a la variable
                ruta = Ruta(origen, destino, distancia, tiempo)
                self.rutas.append(ruta)               
                messagebox.showinfo("Ruta Creada", f"Se ha creado la ruta: {ruta}")
                self.ruta_creada = True

                # Limpiar los campos de entrada
                distancia_entry.delete(0, tk.END)
                tiempo_entry.delete(0, tk.END)

                ruta_frame.destroy()
                self.mostrar_botones()

            # Botón para crear la ruta
            crear_btn = tk.Button(ruta_frame, text="Crear", command=crear, pady=10, padx=30)
            crear_btn.pack(pady=10)

            # Botón para cancelar la creación de la ruta
            cancelar_btn = tk.Button(ruta_frame, text="Cancelar", command=lambda: cancelar_creacion(ruta_frame), pady=10, padx=30)
            cancelar_btn.pack(pady=10)

            def cancelar_creacion(frame):
                frame.destroy()
                self.mostrar_botones()
            pass
        else:                   
            messagebox.showerror("Error", "Debe registrar al menos un aeropuerto antes de crear una ruta.")

    def editar_ruta(self):
        if self.ruta_creada:   
                    
            self.ocultar_botones()

            # Crear un frame para el formulario de edición de ruta
            ruta_frame = tk.Frame(self.root, background='#9E9A99', padx=50, pady=30)
            ruta_frame.pack(expand=True)

            # Lista desplegable para seleccionar una ruta existente
            ruta_label = tk.Label(ruta_frame, text="Selecciona una ruta:", pady=10, background='#9E9A99')
            ruta_combo = ttk.Combobox(ruta_frame, values=[str(r) for r in self.rutas])
            ruta_combo.current(0)
            ruta_label.pack()
            ruta_combo.pack()

            # Campos de entrada para editar los atributos de la ruta seleccionada
            distancia_label = tk.Label(ruta_frame, text="Distancia (en km):", pady=10, background='#9E9A99')
            distancia_entry = tk.Entry(ruta_frame)
            tiempo_label = tk.Label(ruta_frame, text="Tiempo de vuelo (en horas):", pady=10, background='#9E9A99')
            tiempo_entry = tk.Entry(ruta_frame)

            #Se empaqueta el mensaje y el campo de entrada en la ventana principal
            distancia_label.pack()
            distancia_entry.pack()
            tiempo_label.pack()
            tiempo_entry.pack()

            # Obtener la ruta seleccionada al hacer clic en el botón "Aplicar cambios"
            def aplicar_cambios():
                ruta_seleccionada = ruta_combo.get()        
                distancia = distancia_entry.get()           
                tiempo = tiempo_entry.get()                 

                # Buscar la ruta seleccionada en la lista de rutas
                ruta = next((r for r in self.rutas if str(r)
                            == ruta_seleccionada), None)        
                if not ruta:            
                    messagebox.showerror("Error", "No se encontró la ruta seleccionada.")
                    return

                # Actualizar los atributos de la ruta
                ruta.distancia = distancia
                ruta.tiempo = tiempo

                #Mensaje de éxito
                messagebox.showinfo("Edición exitosa", "Los cambios se aplicaron correctamente.")

                # Limpiar los campos de entrada
                distancia_entry.delete(0, tk.END)
                tiempo_entry.delete(0, tk.END)

                ruta_frame.destroy()
                self.mostrar_botones()

            # Botón para aplicar los cambios
            aplicar_btn = tk.Button(
                ruta_frame, text="Aplicar cambios", command=aplicar_cambios, pady=10, padx=30)
            aplicar_btn.pack(pady=10)

            # Botón para cancelar la edición de la ruta
            cancelar_btn = tk.Button(ruta_frame, text="Cancelar", command=lambda: cancelar_edicion(
                ruta_frame), pady=10,  padx=30)
            cancelar_btn.pack(pady=10)

            def cancelar_edicion(frame):
                frame.destroy()
                self.mostrar_botones() 
            ruta_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            pass
        else:          
            messagebox.showerror("Error", "Debe crear al menos una ruta para realizar ediciones.")

    # Mostrar el grafo creado
    def visualizar_rutas(self):
        if self.aeropuerto_registrado: 
             
            # Crear un grafo vacío
            G = nx.Graph() 

            # Agregar los aeropuertos como nodos al grafo
            for aeropuerto in self.aeropuertos:  
                G.add_node(aeropuerto.nombre)  

            # Agregar las rutas como aristas al grafo
            for ruta in self.rutas:  
                origen = ruta.origen.nombre  
                destino = ruta.destino.nombre 
                distancia = ruta.distancia 
                tiempo = ruta.tiempo
                G.add_edge(origen, destino, distance=distancia, time =tiempo )  

            # Dibujar el grafo
            plt.figure(figsize=(8, 6))  
            pos = nx.spring_layout(G)  
            nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', edge_color='gray')
            edge_labels = {edge: f"d={G[edge[0]][edge[1]]['distance']}, t={G[edge[0]][edge[1]]['time']}" for edge in G.edges}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

            # Mostrar el grafo en una nueva ventana
            plt.title("Visualizar Rutas")  
            plt.text(0, -0.1, "(d = distancia, t = tiempo)", transform=plt.gca().transAxes, ha='center')
            plt.axis('off')  
            plt.show() 
        else:  
            messagebox.showerror("Error", "Debe registrar al menos un aeropuerto para poder visualizar las rutas.")

    # Buscar la ruta con menor distancia entre aeropuertos
    def buscar_ruta_distancia(self):
        if self.aeropuerto_registrado:
            
            self.ocultar_botones()

            # Crear un marco para la búsqueda de rutas
            ruta_frame = tk.Frame(self.root, background='#9E9A99', padx=50, pady=30)
            ruta_frame.pack(expand=True)

            origen_label = tk.Label(ruta_frame, text="Aeropuerto de origen:", pady=10, background='#9E9A99')
            origen_combo = ttk.Combobox(ruta_frame, values=[str(aeropuerto) for aeropuerto in self.aeropuertos])
            origen_combo.current(0)

            destino_label = tk.Label(ruta_frame, text="Aeropuerto de destino:", pady=10, background='#9E9A99')
            destino_combo = ttk.Combobox(ruta_frame, values=[str(aeropuerto) for aeropuerto in self.aeropuertos])
            destino_combo.current(0)

            origen_label.pack()
            origen_combo.pack()
            destino_label.pack()
            destino_combo.pack()

            def buscar():
                # Obtener los aeropuertos de origen y destino seleccionados
                origen = self.aeropuertos[origen_combo.current()]
                destino = self.aeropuertos[destino_combo.current()]

                if origen == destino:
                    messagebox.showinfo("Búsqueda de Rutas", "El aeropuerto de origen y destino son iguales.")
                    return
                
                # Algoritmo de Dijkstra para encontrar el camino más corto
                distancia_minima = {aeropuerto: float('inf') for aeropuerto in self.aeropuertos}
                distancia_minima[origen] = 0
                ruta_anterior = {aeropuerto: None for aeropuerto in self.aeropuertos}

                cola_prioridad = [(0, origen)]
                while cola_prioridad:
                    distancia_actual, aeropuerto_actual = heapq.heappop(cola_prioridad)
                    if distancia_actual > distancia_minima[aeropuerto_actual]:
                        continue

                    for ruta in self.rutas:
                        # Comprobar rutas desde el aeropuerto actual
                        if ruta.origen == aeropuerto_actual:
                            distancia = float(ruta.distancia)
                            distancia_total = distancia_minima[aeropuerto_actual] + distancia

                            if distancia_total < distancia_minima[ruta.destino]:
                                # Actualizar la distancia mínima y la ruta anterior
                                distancia_minima[ruta.destino] = distancia_total
                                ruta_anterior[ruta.destino] = aeropuerto_actual
                                heapq.heappush(cola_prioridad, (distancia_total, ruta.destino))

                        # Comprobar rutas hacia el aeropuerto actual
                        if ruta.destino == aeropuerto_actual:
                            distancia = float(ruta.distancia)
                            distancia_total = distancia_minima[aeropuerto_actual] + distancia

                            if distancia_total < distancia_minima[ruta.origen]:
                                distancia_minima[ruta.origen] = distancia_total
                                ruta_anterior[ruta.origen] = aeropuerto_actual
                                heapq.heappush(cola_prioridad, (distancia_total, ruta.origen))

                camino = []
                aeropuerto_actual = destino
                while aeropuerto_actual:
                    # Reconstruir el camino desde el destino al origen
                    camino.insert(0, aeropuerto_actual)
                    aeropuerto_actual = ruta_anterior[aeropuerto_actual]

                if distancia_minima[destino] == float('inf'):
                    messagebox.showinfo("Búsqueda de Rutas", "No se encontró un camino válido.")
                else:
                    messagebox.showinfo("Búsqueda de Rutas", f"Camino más corto: {' -> '.join(str(a) for a in camino)}\nDistancia total: {distancia_minima[destino]} km")

                # Limpiar los campos de origen y destino
                origen_combo.delete(0, tk.END)
                destino_combo.delete(0, tk.END)

                # Eliminar el frame de búsqueda y mostrar los botones principales
                ruta_frame.destroy()
                self.mostrar_botones()

            # Botón para buscar la mejor ruta
            aplicar_btn = tk.Button(ruta_frame, text="Buscar mejor ruta", command=buscar, padx=30, pady=10)
            aplicar_btn.pack(pady=10)
            
            # Botón para cancelar la búsqueda
            cancelar_btn = tk.Button(ruta_frame, text="Cancelar", command=lambda: cancelar_busqueda(ruta_frame), pady=10, padx=30)
            cancelar_btn.pack(pady=10)

            def cancelar_busqueda(frame):
                frame.destroy()
                self.mostrar_botones()

            ruta_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            pass
        else:
            messagebox.showerror("Error", "Debe registrar al menos un aeropuerto antes de buscar rutas.")
            
    def buscar_ruta_tiempo(self):
        if self.aeropuerto_registrado:
            
            self.ocultar_botones()

            # Crear un marco para la búsqueda de rutas por tiempo
            ruta_frame = tk.Frame(self.root, background='#9E9A99', padx=50, pady=30)
            ruta_frame.pack(expand=True)

            # Crear etiquetas y cuadros combinados para origen y destino
            origen_label = tk.Label(ruta_frame, text="Aeropuerto de origen:", pady=10, background='#9E9A99')
            origen_combo = ttk.Combobox(ruta_frame, values=[str(aeropuerto) for aeropuerto in self.aeropuertos])
            origen_combo.current(0)

            destino_label = tk.Label(ruta_frame, text="Aeropuerto de destino:", pady=10, background='#9E9A99')
            destino_combo = ttk.Combobox(ruta_frame, values=[str(aeropuerto) for aeropuerto in self.aeropuertos])
            destino_combo.current(0)

            origen_label.pack()
            origen_combo.pack()
            destino_label.pack()
            destino_combo.pack()

            def buscar():
                # Obtener los aeropuertos de origen y destino seleccionados
                origen = self.aeropuertos[origen_combo.current()]
                destino = self.aeropuertos[destino_combo.current()]

                if origen == destino:
                    # Mostrar mensaje si el origen y el destino son iguales
                    messagebox.showinfo("Búsqueda de Rutas", "El aeropuerto de origen y destino son iguales.")
                    return
                
                # Algoritmo de Dijkstra para encontrar el camino más corto por tiempo
                tiempo_minimo = {aeropuerto: float('inf') for aeropuerto in self.aeropuertos}
                tiempo_minimo[origen] = 0
                ruta_anterior = {aeropuerto: None for aeropuerto in self.aeropuertos}

                cola_prioridad = [(0, origen)]
                while cola_prioridad:
                    tiempo_actual, aeropuerto_actual = heapq.heappop(cola_prioridad)
                    if tiempo_actual > tiempo_minimo[aeropuerto_actual]:
                        continue

                    for ruta in self.rutas:
                        if ruta.origen == aeropuerto_actual:
                            tiempo = float(ruta.tiempo)
                            tiempo_total = tiempo_minimo[aeropuerto_actual] + tiempo

                            if tiempo_total < tiempo_minimo[ruta.destino]:
                                tiempo_minimo[ruta.destino] = tiempo_total
                                ruta_anterior[ruta.destino] = aeropuerto_actual
                                heapq.heappush(cola_prioridad, (tiempo_total, ruta.destino))

                        if ruta.destino == aeropuerto_actual:
                            tiempo = float(ruta.tiempo)
                            tiempo_total = tiempo_minimo[aeropuerto_actual] + tiempo

                            if tiempo_total < tiempo_minimo[ruta.origen]:
                                tiempo_minimo[ruta.origen] = tiempo_total
                                ruta_anterior[ruta.origen] = aeropuerto_actual
                                heapq.heappush(cola_prioridad, (tiempo_total, ruta.origen))

                camino = []
                aeropuerto_actual = destino
                while aeropuerto_actual:
                    # Reconstruir el camino desde el destino al origen
                    camino.insert(0, aeropuerto_actual)
                    aeropuerto_actual = ruta_anterior[aeropuerto_actual]

                if tiempo_minimo[destino] == float('inf'):
                    messagebox.showinfo("Búsqueda de Rutas", "No se encontró un camino válido.")
                else:
                    # Mostrar el camino más corto y el tiempo total de vuelo
                    messagebox.showinfo("Búsqueda de Rutas", f"Camino más corto: {' -> '.join(str(a) for a in camino)}\nTiempo total de vuelo: {tiempo_minimo[destino]} horas")

                # Limpiar los campos de origen y destino
                origen_combo.delete(0, tk.END)
                destino_combo.delete(0, tk.END)

                # Eliminar el frame de búsqueda y mostrar los botones principales
                ruta_frame.destroy()
                self.mostrar_botones()

            # Botón para buscar la mejor ruta por tiempo
            aplicar_btn = tk.Button(ruta_frame, text="Buscar mejor ruta por tiempo", command=buscar, padx=30, pady=10)
            aplicar_btn.pack(pady=10)

            # Botón para cancelar la búsqueda
            cancelar_btn = tk.Button(ruta_frame, text="Cancelar", command=lambda: cancelar_busqueda(ruta_frame), pady=10, padx=30)
            cancelar_btn.pack(pady=10)

            def cancelar_busqueda(frame):
                frame.destroy()
                self.mostrar_botones()

            ruta_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        else:
            messagebox.showerror("Error", "Debe registrar al menos un aeropuerto antes de buscar rutas.")
     
# Instanciar la aplicación y ejecutarla
app = AeropuertoApp()
app.run()