escenario=["1","2","3","4","5","6","7","8","9","10",
           "11","12","13","14","15","16","17","18","19","20",
           "21","22","23","24","25","26","27","28","29","30",
           "31","32","33","34","35","36","37","38","39","40",
           "41","42","43","44","45","46","47","48","49","50",
           "51","52","53","54","55","56","57","58","59","60",
           "61","62","63","64","65","66","67","68","69","70",
           "71","72","73","74","75","76","77","78","79","80",
           "81","82","83","84","85","86","87","88","89","90",
           "91","92","93","94","95","96","97","98","99","100"]

reservas=[None]*100

def reservado_por():
    for i in range(len(escenario)):
        if reservas[i]!= None:
            print(f"{i+1} -  rut: {reservas[i]}  ") 

def mostrar_escenario():
    print(escenario, end=" , ")

def reservar(rut:str):

    mostrar_escenario()
    while True:
        escen=input("Indique el número de asiento a reservar: ")
        if escen.lower()=="x":
            return
        
        if escen in "123456789" and len(escen)==1 or len(escen)==2 or len(escen)==3 and escenario[(int(escen))-1]!="X":
            escenario[(int(escen))-1]="X"
            reservas[(int(escen))-1]=rut
            print("asiento reservado")
            return

        if escen==escen:
            print("Número ocupado")
            return


while True:

    print("""
    1.comprar entradas
    2.mostrar ubicaciones
    3.ver listado de asistentes
    4.mostrar ganancias
    5.salir
    """)
    op=input("ingrese una opcion: ")
    match op:
        case "1":
            rut=input("ingrese su rut: ")
            reservar(rut)
        case "2":
            mostrar_escenario()
        case "3":
            reservado_por()
        case "4":
            print("las ganancias de hoy son: ")
        case "5":
            print("""
            gracias por comprar por creativo.cl 
            se despide luis arevalo con fecha del 10/07/2023""")
            break
