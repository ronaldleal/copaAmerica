from tabulate import tabulate
encabezado=["Codigo equipo", "Equipo", "Pais", "Jugadores"]
encabezadoEstadisticas=["PJ", "PG", "PE", "PP"]
selecciones=[]
isActivateMenu=True
isAddCodigoEquipo=True
op=0
while isActivateMenu==True:
    print("1. Equipo participante\n2. Registro de Estadisticas\n3. Busqueda de jugadores\n4. Listar equipos y Jugadores\n5. Tabla de posiciones\n5. Salir")
    op=int(input())
    if op==1:
        isAddCodigoEquipo=True
        while isAddCodigoEquipo==True:
            codigo=input("Ingrese el codigo del equipo :")
            nombre=input("Ingrese el nombre del equipo :")
            pais=input("Ingrese pais de origen : ")
            equipo=[codigo.upper(),nombre.upper(),pais]
            plantaJugadores=int(input("Ingrese canditad de jugadores: "))
            plantilla=list()
            for i in range (0,plantaJugadores):
                jugador=input(f'Ingrese el nombre de jugador {i+1}: ')
                plantilla.append(jugador)
            equipo.append(plantilla)    
            selecciones.append(equipo)
            print(selecciones)
            rta=input("Desea Ingresar otro Equipo S o N : ")
            if rta.upper()=="S":
                isAddCodigoEquipo=True
            elif rta.upper()=="N":
                isAddCodigoEquipo=False
            else:
                print("Respuesta no valida")
                isAddCodigoEquipo=True
    if op==2:
        print('***Registro de Partidos***')
        estadistica=list()
        cantEquipos=(len(selecciones))
        if cantEquipos <= 1:
            print('Ingrese un equipo por favor...')
        else:
            pg=0
            pe=0
            pp=0
            pj= (cantEquipos - 1)
            for seleccion in selecciones:
                pto=0
                estadistica=list()
                estadistica.append(pj)            
                print(pj)
                isPGValid=False
                while not isPGValid:
                    pg=int(input(f'Ingrese partidos Ganados de {seleccion[1]}: '))
                    isPGValid= (pg >= 0) and (pg <= pj) 

                    if not isPGValid:
                        print('Cantidad de partidos invalido, vuelva a intentar')
                    else:
                        estadistica.append(pg)
                        estadistica.append(pto)   
                        pto=pto + (pg*3)

                isPEValid=False
                while not isPEValid:
                    pe=int(input(f'Ingrese partidos Empatados de {seleccion[1]}: '))
                    isPEValid=(pe >= 0) and (pe <= pj) 
                    if not isPEValid:
                        print('Cantidad de partidos invalido, vuelva a intentar')
                    else:
                        estadistica.append(pe)
                        estadistica.append(pto)
                        pto=pto + (pe)
                
                isPPValid=False
                while not isPPValid:
                    pp=int(input(f'Ingrese partidos Perdidos de {seleccion[1]}: '))
                    isPPValid=(pp >= 0) and (pp <= pj)
                    if not isPPValid:
                        print('Cantidad de partidos invalido, vuelva a intentar') 
                        estadistica.append(pp)
                        estadistica.append(pto)
                        pto=pto + (pto*0)
                seleccion.append(estadistica)
    

    if op==3:
        print('***Busqueda de jugadores de un equipo***')
        isBusJugador=True
        while isBusJugador==True:
            word=input('Escriba el codigo del equipo : ')
            for i in range(0,len(selecciones)):
                if word in selecciones[i]:
                    print(f'El nombre del jugador es : {selecciones[i][0]}')
                    print(f'El jugador pertenece al equipo de : {selecciones[i][1]}')
                    break
                elif i==(len(selecciones)-1):
                    print('El jugador no pertenece a ningun equipo')
            isBusJugador=bool(input('Desea consultar otro jugador: S o N para salir'))

    if op==4:
        print('*** Registro de Equipos y jugadores')
        print(tabulate(selecciones, encabezado,tablefmt='github'))
        print(tabulate(estadistica, encabezadoEstadisticas,tablefmt='github'))

    if op==5:
        rta=input("Desea Abandonar el Programa S o N : ")
        if rta.upper()=="S":
            isActivateMenu=False
        elif rta.upper()=="N":
            isActivateMenu=True
        else:
            print("Respuesta no valida")
            isActivateMenu=True

# registre fechas una a una