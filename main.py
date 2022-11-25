print("¡¡¡¡WELCOME!!!!!");
print("*********INGRESO DE DATOS PERSONALES**********");
nombre=input("INGRESE SU NOMBRE Y APELLIDO :");
nacimiento=int(input("INGRESE SU AÑO DE NACIMIENTO :"));
edad=(2022-nacimiento);
if(edad<=17):
    print( "DON :",nombre,"lo sentimos mucho pero es menor de edad :");
    print("¡¡¡Gracias por participar!!!");
elif(edad>=18):

    primer_sem=int(input("Ingrese las ventas del primer semestre:"));
    segundo_sem=int(input("Ingrese las vetas del segundo semestre :"));
    suma_semestre=(primer_sem+segundo_sem);
    print("*******RESULTADO DEL AÑO 2021********");
    if(primer_sem>segundo_sem):
        mensaje="1RO CON:",primer_sem;
    elif(segundo_sem>primer_sem):
        mensaje="2DO CON:",segundo_sem;
    else:
        mensaje="LOS DOS SEMESTRE VENDIERON IGUAL";
    if(suma_semestre<=100000):
        print("VENDEDOR DON :",nombre);
        print("VENTAS ANUALES :",suma_semestre);
        print("MEJOR SEMESTR :",mensaje);
        print("MEDALLA ACREDITADA:","Bronce");
        print("PREMIO:","Un dia libre");
    elif(suma_semestre>=100001 and suma_semestre<=500000 ):

            print("VENDEDOR DON :", nombre);
            print("VENTAS ANUALES :", suma_semestre);
            print("MEJOR SEMESTR :", mensaje);
            print("MEDALLA ACREDITADA:", "Plata");
            print("PREMIO:", "Un dia libre y un bono de Q250");
    elif(suma_semestre>=500001 and suma_semestre<=1000000):

            print("VENDEDOR DON :", nombre);
            print("VENTAS ANUALES :", suma_semestre);
            print("MEJOR SEMESTR :", mensaje);
            print("MEDALLA ACREDITADA:", "Oro");
            print("PREMIO:", "Un dia libre y un bono de Q500");
    elif(suma_semestre>=1000001):
        print("VENDEDOR DON :", nombre);
        print("VENTAS ANUALES :", suma_semestre);
        print("MEJOR SEMESTR :", mensaje);
        print("MEDALLA ACREDITADA:", "Diamente");
        print("PREMIO:", "Dos dias libres y un bono de Q100");
elif(edad==0):
    print("SU FECHA DE NACIMIENTO ES INCORECTA REINICIE EL PROGRAMA");





























