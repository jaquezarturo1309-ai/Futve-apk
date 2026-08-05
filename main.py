# ==========================================
# SIMULADOR DE MODO CARRERA: LIGA FUTVE 26/27
# Motor de consola / Base para Godot o Python
# ==========================================

import random
import sys

class Jugador:
    def __init__(self, nombre, posicion, media):
        self.nombre = nombre
        self.posicion = posicion
        self.media = media

class Equipo:
    def __init__(self, nombre, division, presupuesto):
        self.nombre = nombre
        self.division = division  # 1 o 2
        self.presupuesto = presupuesto
        self.puntos = 0
        self.goles_favor = 0
        self.goles_contra = 0
        self.plantilla = []

    def agregar_jugador(self, jugador):
        self.plantilla.append(jugador)

class ModoCarreraFUTVE:
    def __init__(self):
        self.dt_nombre = ""
        self.equipo_usuario = None
        self.temporada = "2026/2027"
        self.equipos_primera = []
        self.equipos_segunda = []
        self.inicializar_mundiales_y_locales()

    def inicializar_mundiales_y_locales(self):
        # Configuración de equipos Liga FUTVE y FUTVE 2
        nombres_primera = [
            "Caracas FC", "Deportivo Táchira", "Carabobo FC", "Metropolitanos FC",
            "Academia Puerto Cabello", "Zamora FC", "Estudiantes de Mérida", 
            "Portuguesa FC", "Deportivo La Guaira", "UCV FC", "Monagas SC", "Rayo Zuliano"
        ]
        
        nombres_segunda = [
            "Deportivo Lara", "Atlético Barinas", "Yaracuyanos FC", "Aragua FC",
            "Deportivo Miranda", "Bolívar SC", "Dynamo Puerto", "Mineros de Guayana"
        ]

        for nombre in nombres_primera:
            eq = Equipo(nombre, 1, 500000)
            eq.agregar_jugador(Jugador("Estrella 1", "DEL", 75))
            eq.agregar_jugador(Jugador("Mediocampista Base", "MED", 72))
            self.equipos_primera.append(eq)

        for nombre in nombres_segunda:
            eq = Equipo(nombre, 2, 150000)
            eq.agregar_jugador(Jugador("Juvenil Destacado", "DEL", 65))
            self.equipos_segunda.append(eq)

    def iniciar_juego(self):
        print("==================================================")
        print(f"      EA SPORTS FC 27 - MODO CARRERA FUTVE {self.temporada}")
        print("==================================================")
        self.dt_nombre = input("Ingrese el nombre de su Director Técnico: ")
        
        print("\nElige tu equipo para iniciar el Modo Carrera:")
        print("--- LIGA FUTVE (PRIMERA DIVISIÓN) ---")
        for i, eq in enumerate(self.equipos_primera):
            print(f"{i + 1}. {eq.nombre}")
            
        print("--- LIGA FUTVE 2 (SEGUNDA DIVISIÓN) ---")
        for i, eq in enumerate(self.equipos_segunda):
            print(f"{i + 13}. {eq.nombre}")

        eleccion = int(input("\nIngrese el número de su equipo: "))
        if 1 <= eleccion <= 12:
            self.equipo_usuario = self.equipos_primera[eleccion - 1]
        elif 13 <= eleccion <= 20:
            self.equipo_usuario = self.equipos_segunda[eleccion - 13]
        else:
            self.equipo_usuario = self.equipos_primera[0]

        print(f"\n¡Bienvenido, DT {self.dt_nombre}! Has tomado las riendas del {self.equipo_usuario.nombre}.")
        self.menu_principal()

    .menu_principal(self):
    def menu_principal(self):
        while True:
            print(f"\n--- MENÚ PRINCIPAL | {self.equipo_usuario.nombre} ---")
            print("1. Ver Plantilla y Fichajes")
            print("2. Simular Próxima Jornada")
            print("3. Ver Tabla de Posiciones")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.ver_plantilla()
            elif opcion == "2":
                self.simular_jornada()
            elif opcion == "3":
                self.ver_tabla()
            elif opcion == "4":
                print("Guardando partida... ¡Hasta pronto!")
                sys.exit()

    def ver_plantilla(self):
        print(f"\n--- PLANTILLA: {self.equipo_usuario.nombre} ---")
        print(f"Presupuesto actual: ${self.equipo_usuario.presupuesto}")
        for j in self.equipo_usuario.plantilla:
            print(f"- {j.nombre} ({j.posicion}) | Media: {j.media}")

    def simular_jornada(self):
        print("\nSimulando partido de la jornada...")
        goles_favor = random.randint(0, 3)
        goles_contra = random.randint(0, 3)
        
        print(f"Resultado final: {self.equipo_usuario.nombre} {goles_favor} - {goles_contra} Rival")
        
        self.equipo_usuario.goles_favor += goles_favor
        self.equipo_usuario.goles_contra += goles_contra
        
        if goles_favor > goles_contra:
            self.equipo_usuario.puntos += 3
            print("¡Victoria sumada! 3 puntos a la tabla.")
        elif goles_favor == goles_contra:
            self.equipo_usuario.puntos += 1
            print("Empate. 1 punto sumado.")
        else:
            print("Derrota en esta jornada.")

    def ver_tabla(self):
        print(f"\n--- TABLA DE POSICIONES (Temporada {self.temporada}) ---")
        print(f"{'EQUIPO':<30} | {'PTS':<5} | {'GF':<5} | {'GC':<5}")
        print("-" * 50)
        
        # Mostrar equipos de primera división ordenados por puntos
        equipos_ordenados = sorted(self.equipos_primera, key=lambda x: x.puntos, reverse=True)
        for eq in equipos_ordenados:
            print(f"{eq.nombre:<30} | {eq.puntos:<5} | {eq.goles_favor:<5} | {eq.goles_contra:<5}")

if __name__ == "__main__":
    juego = ModoCarreraFUTVE()
    juego.iniciar_juego()
      
