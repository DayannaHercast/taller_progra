# Version de python 3.13.1

import random
import time


# =============================================
# FUNCIÓN PRINCIPAL
# =============================================
def funcion_principal():
    print("✨ ¡BIENVENIDO A Dö ká böwö: En busca de la luz! ✨\n")
    print("¡Prepárate para una aventura épica defendiendo culturas ancestrales!\n")
    print("🔥 ¡ALERTA! Las comunidades indígenas están en peligro... ")
    print(
        "⛪ Misioneros con ideas extrañas y 💰 empresas mineras codiciosas "
        "amenazan su existencia!"
    )

    print("¡El CONSEJO (tú) es su última esperanza!")
    print("💥 La misión: Fortalecer AUTONOMÍA 🛡️ y ACERVO CULTURAL 📚 o SERÁ EL",
          "FIN!\n")

    print("🎮 MECÁNICAS DEL JUEGO:")
    print("1.Elige cuántas comunidades salvarás (¡sé sabio!)")
    print(
        "2.Cada comunidad tiene AUTONOMÍA y ASERVO CULTURAL - ¡ambas deben"
        "sobrevivir!"
    )
    print("3.Cada turno es una batalla: tú fortaleces, ellos atacan 💢")
    print("4.Si algún valor llega a CERO... 💀 la comunidad es eliminada")
    print("5.Si TODAS caen... ¡GAME OVER!\n")

    print("¡EL DESTINO DE LOS PUEBLOS ORIGINARIOS ESTÁ EN TUS MANOS!")
    print("\n¿Aceptas el desafío? (1 para SÍ, 0 para RENDIRSE)")
    # Validación de la entrada
    iniciar = input("Ingrese su decisión: ")
    resultado = validar_inicio(iniciar)
    if resultado == 1:
        return comenzar_juego(resultado)
    elif resultado == 0:
        return 0
    else:
        return funcion_principal()


# =============================================
# FUNCION PARA VALIDAR EL INICIO DEL JUEGO
# =============================================
def validar_inicio(numero):
    """
    Funcion que valida si un caracter es "1" o "0" y devuelve el entero.
    E: un caracter "1" o "0"
    S: un entero 1 o 0
    R: tine que ser un caracter "1" o "0"
    """
    if numero == "1":
        print("\n¡VALIENTE DECISIÓN COMENCEMOS!\n")
        return 1
    elif numero == "0":
        print("\nEl consejo ABANDONO a los pueblos originarios...\n")
        return 0
    else:
        time.sleep(2)
        print("\n¡UPS! Solo se permite 1 (para valientes) o 0 (para cobardes)\n")
        time.sleep(2)
        return None


# =============================================
# FUNCION PARA COMENZAR EL JUEGOj
# =============================================
def comenzar_juego(iniciar):
    """
    Función que permite iniciar el juego
    E: Un número entero (0 o 1)
    S: Ejecuta el juego o finaliza
    R: iniciar debe ser 0 o 1
    """
    if type(iniciar) != int:
        print("El número debe ser entero.")

    else:
        return comenzar_juego_aux(iniciar)


def comenzar_juego_aux(iniciar):
    """FUNCION AUXILIAR"""
    cantidad_comunidades = input(
        "Ingrese la cantidad de comunidades a apoyar (entre 1 y 8): "
    )
    resultado = validar_comunidades(cantidad_comunidades)
    if resultado >= 1 and resultado < 9:
        return generar_comunidades(resultado)
    else:
        time.sleep(1)
        print(
            "\n***¡ALERTA! ⚠ Tiene que ser un número del 1 al 8 ¡Elige de "
            "nuevo!***\n"
        )
        return comenzar_juego_aux(1)


# =============================================
# FUNCION PARA VALIDAR LA CANTIDAD DE COMUNIDADES
# =============================================
def validar_comunidades(numero):
    """
    Funcion que valida si un caracter esta dentro del rango de "1" a "8" y
    devuelve el entero.
    E: un caracter entre "1" y "8"
    S: un numero entero en el rango de 1 a 8
    R: Tine que ser un caracter de "1" a "8"
    """
    if numero == "1":
        return 1
    elif numero == "2":
        return 2
    elif numero == "3":
        return 3
    elif numero == "4":
        return 4
    elif numero == "5":
        return 5
    elif numero == "6":
        return 6
    elif numero == "7":
        return 7
    elif numero == "8":
        return 8
    else:
        return 0


# =============================================
# FUNCION QUE DA EL NOMBRE DE LAS COMUNIDADES
# =============================================
def comunidad_random(numero_comunidades):
    """
    Genera una lista de comunidades aleatorias sin repetir,
    usando random.randint.
    E: número entero que indica cuántas comunidades se quieren seleccionar
    S: lista de comunidades aleatorias sin repetir
    R: el número debe estar entre 1 y 8
    """
    # Validación de tipos y rango de entrada
    if type(numero_comunidades) != int:
        return "numero_comunidades tiene que ser un entero"
    elif numero_comunidades > 8:
        return "numero_comunidades no puede ser mayor que 8"
    elif numero_comunidades < 1:
        return "numero_comunidades no puede ser menor que 1"
    else:
        # Lista de comunidades disponibles
        comunidades = [
            "Bribri",
            "Cabecar",
            "Ngäbe",
            "Maleku",
            "Huetar",
            "Brunka",
            "Chorotega",
            "Térraba",
        ]
        return comunidad_random_aux(numero_comunidades, comunidades, [])


def comunidad_random_aux(numero_c, comunidades, resultado):
    """
    FUNCIÓN AUXILIAR
    """
    if len(resultado) == numero_c:
        return resultado
    else:
        posicion = random.randint(0, 7)
        elegida = comunidades[posicion]

        # Si ya está en la lista, volvemos a intentar sin agregarla
        if esta_en_lista(elegida, resultado) == True:
            return comunidad_random_aux(numero_c, comunidades, resultado)
        else:
            # Si no está repetida, la agregamos y continuamos
            return comunidad_random_aux(numero_c, comunidades,
                                        resultado + [elegida])


def esta_en_lista(comunidad_nombre, lista):
    """
    Verifica si una comunidad ya está en la lista acumulada.
    E: comunidad (string), lista de comunidades ya agregadas
    S: True si la comunidad ya está en la lista, False si no
    R: comunidad debe ser string, lista no debe estar vacía
    """
    if type(comunidad_nombre) != str:
        return "La comunidad tiene que ser un string"
    elif len(lista) == 0:
        return False  # Lista vacía, no puede estar
    else:
        return esta_en_lista_aux(comunidad_nombre, lista, 0)


def esta_en_lista_aux(comunidad_nombre, lista, indice):
    """
    FUNCIÓN AUXILIAR
    """
    if indice == len(lista):
        return False  # Llegamos al final sin encontrarla
    elif comunidad_nombre == lista[indice]:
        return True  # Encontramos la comunidad repetida
    else:
        return esta_en_lista_aux(comunidad_nombre, lista, indice + 1)


# =============================================
# FUNCION QUE GENERA LAS COMUNIDADES
# =============================================
def generar_comunidades(numero):
    """
    Función que permite crear las comunidades
    E: Un número entero (1 o 8)
    S: Genera las n comunidades
    R: numero tiene que ser un entero y estar entre 1 y 8
    """
    if type(numero) != int:
        print("El número debe ser entero.")
        return comenzar_juego_aux(1)
    elif numero <= 0:
        time.sleep(1)
        print("\n***El número debe de ser entre 1 y 8.***\n")
        return comenzar_juego_aux(1)

    elif numero >= 9:
        time.sleep(1)
        print("\n***El número debe de ser entre 1 y 8.***\n")
        return comenzar_juego_aux(1)

    else:
        return generar_comunidades_aux(
            numero,
            comunidad_random(numero),
            0,
            [],
        )


def generar_comunidades_aux(numero, comunidades, indice, todo):
    """FUNCION AUXILIAR"""
    if indice == numero:
        return guardar_datos(todo)
    else:
        nueva_comunidad = [
            [comunidades[indice]],  # Nombre
            [random.randint(1, 5)],  # Autonomía
            [random.randint(1, 5)],  # Acervo
        ]

        return generar_comunidades_aux(
            numero, comunidades, indice + 1, todo + [nueva_comunidad]
        )


# =============================================
# FUNCION QUE GUARDA LOS DATOS DE LAS COMUNIDADES
# =============================================
def guardar_datos(todos_datos):
    """
    Función que recibe la lista de comunidades y las reenvia turnos jugar.
    E: lista de listas generadas por generar_comunidades
    S: puede imprimirla, pasarla a otra función o procesarla
    """
    if type(todos_datos) != list:
        return "La programadora se equivocó"

    else:
        return guardar_datos_aux(todos_datos, 0, [])


def guardar_datos_aux(todos_datos, indice, resultado):
    """FUNCION AUXILIAR"""

    if indice == 1:
        return turnos_jugadores(todos_datos)

    else:
        return guardar_datos_aux(
            todos_datos, indice + 1, resultado + [todos_datos[indice]]
        )


# =============================================
# FUNCION QUE VERIFICA SI LAS COMUNIDADES ESTAN EN 0 O MENOR A 0 Y LAS ELIMINA
# =============================================
def verificar_comunidades(todos_datos):
    """
    Elimina las comunidades si están en 0 o menor a 0.
    Si todas se eliminan, retorna [].
    E: lista de listas recivido de funcion turnos jugadores
    S: si acervo o autonomia es menor a 0 se elimina la comunidad
    R: tiene que ser una lista
    """
    if type(todos_datos) != list:
        return "Tiene que ingresar una lista"
    else:
        return verificar_comunidades_aux(todos_datos, len(todos_datos), 0, [])


def verificar_comunidades_aux(todos_datos, largo_datos, indice, nuevos_datos):
    """FUNCION AUXILIAR"""
    if indice == largo_datos:
        return nuevos_datos

    comunidad_actual = todos_datos[indice]
    autonomia = comunidad_actual[1][0]
    acervo = comunidad_actual[2][0]

    if autonomia <= 0 or acervo <= 0:
        print(
            f"¡DESTINO TRÁGICO! La comunidad {comunidad_actual[0][0]} se disolvió..."
        )

        return verificar_comunidades_aux(
            todos_datos, largo_datos, indice + 1, nuevos_datos
        )
    else:
        return verificar_comunidades_aux(
            todos_datos, largo_datos, indice + 1, nuevos_datos + [comunidad_actual]
        )


# =============================================
# FUNCION PARA VALIDAR EN NUMERO DE PROYECTO
# =============================================
def validar_proyecto(numero):
    """
    Funcion que valida si un caracter esta dentro del rango de "1" a "2" y
    devuelve el entero.
    E: un caracter entre "1" y "2"
    S: un numero entero en el rango de 1 a 2
    R: Tine que ser un caracter de "1" a "2"
    """
    if type(numero) != str:
        return "Error tiene que ser un string"
    elif numero == "1":
        return 1
    elif numero == "2":
        return 2
    else:
        return 0


# =============================================
# FUNCION TURNOS: QUE MANDA A LLAMAR A LAS OTRAS FUNCIONES PARA LOS TURNO 1
# SUMAR Y 2 RESTAR
# =============================================
def turnos_jugadores(todo_datos):
    """Función que maneja los turnos de los jugadores
    E: Lista con todos los datos de las comunidades
    S: Ejecuta los turnos de los jugadores y manda a llamar
    a las funciones de sumar y restar
    R: tiene que ser una lista
    """
    if type(todo_datos) != list:
        return "Error tiene que ser una lista"

    else:
        # Inicio de inputs de comunidades
        print("\n🔥 ¡COMUNIDADES EN PELIGRO! 🔥")
        print("=============================")
        print(tabla_datos_imprimir(todo_datos))
        time.sleep(1)
        print("¡MOMENTO DECISIVO!")
        print("El destino de los pueblos originarios depende del consejo...\n")
        time.sleep(1)
        comunidad = input("Escribe el número de la comunidad que recibira apoyo: ")
        resultado_comunidad = validar_comunidades(comunidad)

        if type(resultado_comunidad) != int:
            print("Error tiene que ingresar un numero entero")
            return turnos_jugadores(todo_datos)
        elif resultado_comunidad < 1 or resultado_comunidad > len(todo_datos):
            time.sleep(2)
            print(
                "\n***¡ALERTA! ⚠ Solo podemos proteger comunidades del 1 al",
                len(todo_datos),
                "¡Elige de nuevo!***",
            )
            time.sleep(2)
            return turnos_jugadores(todo_datos)

        # Inicio de inputs de proyectos
        time.sleep(1)
        print("\nPROYECTOS DISPONIBLES:\n")
        print("1. AUTONOMÍA 🛡️ (Defensa contra invasores)")
        print("2. ACERVO CULTURAL 📚 (Protege sabiduría ancestral)\n")
        proyecto = input("¿Qué proyecto reforzarás?: ")
        resultado_proyecto = validar_proyecto(proyecto)

        if type(resultado_proyecto) != int:
            return "Error tiene que ser entero"

        elif resultado_proyecto != 1 and resultado_proyecto != 2:
            time.sleep(1)
            print("\n***¡CRASH! ¡Solo 1 o 2 es permitido!***")
            time.sleep(2)
            return turnos_jugadores(todo_datos)

        else:
            return turnos_jugadores_aux(
                todo_datos, resultado_comunidad, resultado_proyecto, 2
            )


def turnos_jugadores_aux(todo_datos, comunidad, proyecto, turnos):
    """FUNCION AUXILIAR"""
    # Verificar si todas las comunidades han sido eliminadas
    comunidades_restantes = verificar_comunidades(todo_datos)
    if len(comunidades_restantes) == 0:
        print(tabla_datos_imprimir(comunidades_restantes))
        print("¡FIN DE UNA ERA! El último pueblo ha desaparecido")
        return " "

    elif turnos == 0:
        time.sleep(3)
        print("\nRESULTADOS DE LA RONDA:")
        return guardar_datos(comunidades_restantes)

    elif turnos == 2:
        time.sleep(1)
        print("\n===================================================")
        print("¡TURNO DEL CONSEJO!")
        print("===================================================\n")
        return turnos_jugadores_aux(
            elegir_sumar(todo_datos, comunidad, proyecto),
            comunidad,
            proyecto,
            turnos - 1,
        )
    else:
        time.sleep(1)
        print("===================================================")
        print("¡TURNO DE LOS ENEMIGOS!")
        print("====================================================\n")
        return turnos_jugadores_aux(
            elegir_restar(todo_datos), comunidad, proyecto, turnos - 1
        )


# =============================================
# FUNCION DEL TURNO 1 SUMAR PROYECTO
# =============================================
def elegir_sumar(todo_datos, comunidad, proyecto):
    """Función que elige un proyecto a apoyar de una comunidad
    E: una lista con todos los datos y el numero de comunidad a apoyar y
    el proyecto a apoyar
    S: Los datos con la suma  ya sea en acervo cultural o autonomia
    R: todo_datos tiene que ser una lista, comunidad un entero y
    proyecto tambien
    """
    if type(todo_datos) != list:
        return "Error tiene que ingresar una lista"
    elif type(comunidad) != int:
        return "Error tiene que ingresar un número entero"
    elif type(proyecto) != int:
        return "Error tiene que ingresar un número entero"

    elif comunidad < 1 or comunidad > len(todo_datos):
        return "Error"
    else:
        return elegir_proyecto_sumar_aux(todo_datos, comunidad, proyecto, 1)


def elegir_proyecto_sumar_aux(todo_datos, comunidad, proyecto, turnos_restantes):
    """FUNCION AUXILIAR"""
    if turnos_restantes == 0:
        return todo_datos

    if proyecto == 1:
        time.sleep(2)
        print("¡MANDATO DEL CONSEJO! Priorizar la AUTONOMÍA")
        return elegir_proyecto_sumar_aux(
            suma_aleatoria_autonomia(todo_datos, comunidad),
            comunidad,
            proyecto,
            turnos_restantes - 1,
        )
    if proyecto == 2:
        time.sleep(2)
        print("¡MANDATO DEL CONSEJO! Priorizar el ACERVO CULTURAL")
        return elegir_proyecto_sumar_aux(
            suma_aleatoria_acervo(todo_datos, comunidad),
            comunidad,
            proyecto,
            turnos_restantes - 1,
        )


# =============================================
# SUMA DE PROYECTO: AUTONOMIA
# =============================================
def suma_aleatoria_autonomia(todo_datos, comunidad):
    """Funcion que suma a una comunidad en el proyecto de autonomia
    E:todos los datos, el numero de comunidad para sumar
    S:La suma en todo_datos en la comunidad elegida en autonomia
    R:Los datos tienen que ser tipo list
    """
    if type(todo_datos) != list:
        return "Error tiene que ser lista"
    elif comunidad < 1 or comunidad > len(todo_datos):
        return "Error tiene que ser un número entre 1 y 8"
    elif type(comunidad) != int:
        return "Error tiene que ser un número entero"
    else:
        return suma_aleatoria_autonomia_aux(
            todo_datos, len(todo_datos), 0, comunidad - 1,
            random.randint(1, 5), []
        )


def suma_aleatoria_autonomia_aux(
    todo_datos, largo_datos, indice, comunidad, nuevo_valor, resultado
):
    """FUNCION AUXILIAR"""
    if indice == largo_datos:
        nombre = todo_datos[comunidad][0][0]
        time.sleep(2)
        print(f"\n¡REFUERZO EXITOSO! 🛡️ +{nuevo_valor} para {nombre}")
        time.sleep(3)
        print("\nESTADO ACTUAL:\n")
        print(tabla_datos_imprimir(resultado))
        return resultado

    elif indice == comunidad:
        nueva_comunidad = [
            todo_datos[comunidad][0],  # Nombre
            [todo_datos[comunidad][1][0] + nuevo_valor],  # Autonomía (suma)
            todo_datos[comunidad][2],  # Acervo (sin cambios)
        ]
        return suma_aleatoria_autonomia_aux(
            todo_datos,
            largo_datos,
            indice + 1,
            comunidad,
            nuevo_valor,
            resultado + [nueva_comunidad],
        )  # Agregar comunidad modificada

    else:
        return suma_aleatoria_autonomia_aux(
            todo_datos,
            largo_datos,
            indice + 1,
            comunidad,
            nuevo_valor,
            resultado + [todo_datos[indice]],
        )  # Agregar comunidades no modificadas


# =============================================
# SUMA DE PROYECTO: ACERVO
# =============================================
def suma_aleatoria_acervo(todo_datos, comunidad):
    """Funcion que suma a una comunidad en el proyecto de acervo cultural
    E:todos los datos, el numero de comunidad para sumar
    S:La suma en todo_datos en la comunidad elegida en acervo cultural
    R:todo_datos tiene que ser tipo list
    """
    if type(todo_datos) != list:
        return "Error tiene que ser lista"
    elif comunidad < 1 or comunidad > len(todo_datos):
        return "Error tiene que ser un número entre 1 y 8"
    elif type(comunidad) != int:
        return "Error tiene que ser un número entero"
    else:
        return suma_aleatoria_acervo_aux(
            todo_datos, len(todo_datos), 0, comunidad - 1,
            random.randint(1, 5), []
        )


def suma_aleatoria_acervo_aux(
    todo_datos, largo_datos, indice, comunidad, nuevo_valor, resultado
):
    """FUNCION AUXILIAR"""
    if indice == largo_datos:
        nombre = todo_datos[comunidad][0][0]
        time.sleep(2)
        print(f"\n¡REFUERZO EXITOSO! 🛡️ +{nuevo_valor} para {nombre}")
        time.sleep(3)
        print("\nESTADO ACTUAL:\n")
        print(tabla_datos_imprimir(resultado))
        return resultado

    elif indice == comunidad:
        nueva_comunidad = [
            todo_datos[comunidad][0],  # Nombre
            todo_datos[comunidad][1],  # Autonomía
            [todo_datos[comunidad][2][0] + nuevo_valor],  # Acervo (suma)
        ]

        return suma_aleatoria_acervo_aux(
            todo_datos,
            largo_datos,
            indice + 1,
            comunidad,
            nuevo_valor,
            resultado + [nueva_comunidad],
        )  # Agregar comunidad modificada
    else:
        return suma_aleatoria_acervo_aux(
            todo_datos,
            largo_datos,
            indice + 1,
            comunidad,
            nuevo_valor,
            resultado + [todo_datos[indice]],
        )  # Agregar comunidades no modificadas


# =============================================
# FUNCION DEL TURNO 2 RESTAR PROYECTO
# =============================================
def elegir_restar(todo_datos):
    """Función que elige aleatoriamente qué proyecto restar (autonomía o
    acervo cultural)
    E: una lista de listas con los datos de todas las comunidades
    S: una nueva lista con los datos actualizados después de aplicar la resta
    al proyecto seleccionado
    R: el parámetro debe ser una lista no vacía
    """
    if type(todo_datos) != list:
        return "Error tiene que ser lista"

    else:
        # Número de turnos permitidos
        return elegir_proyecto_restar_aux(todo_datos, random.randint(1, 2), 1)


def elegir_proyecto_restar_aux(todo_datos, proyecto, turnos_restantes):
    """FUNCION AUXILIAR"""
    if turnos_restantes == 0:
        return todo_datos

    if proyecto == 1:
        time.sleep(2)
        print("¡LAS MINERAS ATACAN!\n")
        time.sleep(1)
        print("¡SACRILEGIO A LA AUTONOMÍA!")
        return elegir_proyecto_restar_aux(
            resta_aleatoria_autonomia(todo_datos), proyecto,
            turnos_restantes - 1
        )
    if proyecto == 2:
        time.sleep(2)
        print("¡LOS MISIONEROS ATACAN!\n")
        time.sleep(1)
        print("¡SACRILEGIO AL ACERVO CULTURAL!")
        return elegir_proyecto_restar_aux(
            resta_aleatoria_acervo(todo_datos), proyecto, turnos_restantes - 1
        )


# =============================================
# RESTA DE PROYECTO: AUTONOMIA
# =============================================
def resta_aleatoria_autonomia(todo_datos):
    """Función que resta un valor aleatorio al autonomia cultural de una
    comunidad seleccionada aleatoriamente
    E: una lista de listas con los datos de todas las comunidades
    S: una nueva lista con los datos actualizados donde una comunidad tuvo
    reducción en su autonomia
    R: el parámetro debe ser una lista no vacía
    """
    if type(todo_datos) != list:
        return "Error tiene que ser lista"

    else:
        return resta_aleatoria_autonomia_aux(
            todo_datos,
            len(todo_datos),
            0,
            random.randint(0, len(todo_datos) - 1),
            random.randint(1, 5),
            [],
        )


def resta_aleatoria_autonomia_aux(
    todo_datos, largo_datos, indice, comunidad, nuevo_valor, resultado
):
    """FUNCION AUXILIAR"""
    if indice == largo_datos:
        nombre = todo_datos[comunidad][0][0]
        time.sleep(2)
        print(f"\n¡ATAQUE ENEMIGO! 📚-{nuevo_valor} a {nombre}")
        time.sleep(3)
        print("\nESTADO ACTUAL:\n")
        print(tabla_datos_imprimir(resultado))
        return resultado

    elif indice == comunidad:

        nueva_comunidad = [
            todo_datos[comunidad][0],  # Nombre
            [todo_datos[comunidad][1][0] - nuevo_valor],  # Autonomía (resta)
            todo_datos[comunidad][2],  # Acervo (sin cambios)
        ]

        return resta_aleatoria_autonomia_aux(
            todo_datos,
            largo_datos,
            indice + 1,
            comunidad,
            nuevo_valor,
            resultado + [nueva_comunidad],  # Agregar comunidad modificada
        )
    else:
        return resta_aleatoria_autonomia_aux(
            todo_datos,
            largo_datos,
            indice + 1,
            comunidad,
            nuevo_valor,
            resultado + [todo_datos[indice]],
        )  # Agregar comunidades no modificadas


# =============================================
# RESTA DE PROYECTO: ACERVO
# =============================================
def resta_aleatoria_acervo(todo_datos):
    """Función que resta un valor aleatorio al acervo cultural de una
    comunidad seleccionada aleatoriamente
    E: una lista de listas con los datos de todas las comunidades
    S: una nueva lista con los datos actualizados donde una comunidad tuvo
    reducción en su acervo cultural
    R: el parámetro debe ser una lista no vacía
    """
    if type(todo_datos) != list:
        return "Error tiene que ser una lista"

    else:
        return resta_aleatoria_acervo_aux(
            todo_datos,
            len(todo_datos),
            0,
            random.randint(0, len(todo_datos) - 1),
            random.randint(1, 5),
            [],
        )


def resta_aleatoria_acervo_aux(
    todo_datos, largo_datos, indice, comunidad, nuevo_valor, resultado
):
    """FUNCION AUXILIAR"""
    if indice == largo_datos:
        nombre = todo_datos[comunidad][0][0]
        time.sleep(2)
        print(f"\n¡ATAQUE ENEMIGO! 📚-{nuevo_valor} a {nombre}")
        time.sleep(3)
        print("\nESTADO ACTUAL:\n")
        print(tabla_datos_imprimir(resultado))
        return resultado

    elif indice == comunidad:

        nueva_comunidad = [
            todo_datos[comunidad][0],  # Nombre
            todo_datos[comunidad][1],  # Autonomía
            [todo_datos[comunidad][2][0] - nuevo_valor],  # Acervo (resta)
        ]

        return resta_aleatoria_acervo_aux(
            todo_datos,
            largo_datos,
            indice + 1,
            comunidad,
            nuevo_valor,
            resultado + [nueva_comunidad],
        )  # Agregar comunidad modificada
    else:
        return resta_aleatoria_acervo_aux(
            todo_datos,
            largo_datos,
            indice + 1,
            comunidad,
            nuevo_valor,
            resultado + [todo_datos[indice]],
        )  # Agregar comunidades no modificadas


# =============================================
# TABLA QUE IMPRIME LOS DATOS DE LAS COMUNIDADES
# =============================================
def tabla_datos_imprimir(todo_datos):
    """Funcion que contiene la tabla de datos de las comunidades
    E:una lista con todos los datos
    S:una tabla con los datos(informacion)
    R:tiene que ser una lista
    """
    if type(todo_datos) != list:
        return "La programadora se equivoco"

    else:
        return tabla_datos_imprimir_aux(todo_datos, len(todo_datos), 0)


def tabla_datos_imprimir_aux(todo_datos, largo_todo, indice):
    """FUNCION AUXILIAR"""
    if indice == largo_todo:
        return " "

    else:
        print(
            f" 🛖 Comunidad #{indice+1} | {todo_datos[indice][0][0]} | 🛡️ "
            f"Autonomía: {todo_datos[indice][1][0]} | 📚 Acervo Cultural: "
            f"{todo_datos[indice][2][0]}\n"
        )
        return tabla_datos_imprimir_aux(todo_datos, largo_todo, indice + 1)


# Ejecutar juego
funcion_principal()