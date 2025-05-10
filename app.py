from flask import Flask, render_template, request
import pandas as pd     #importar pandas al proyecto
import re
import matplotlib.pyplot as plt
import io           #renderizar gráficos
import base64

from datetime import datetime

app = Flask(__name__)
# Flask app.route decorador paa mapear la ruta URL / a esta función

paciente= {}
@app.route("/")
def home():
    return "Holaa, Flask" 

#Ejemplo con paso de valor
@app.route("/hello/<name>")
def hello_there(name):
    now= datetime.now()
    formatted_now= now.strftime("%A, %d, %B, %y at %X")
    return f"Hello Mr.  {name}! the time is: {formatted_now}"


@app.route("/producto/<int:id>")
def mostrar_producto(id):
    return f"El id de producto es: {id}"


@app.route("/temperatura/<float:grados>")
def mostrar_temperatura(grados):
    return f"la temperatura es:  {grados} °C"


@app.route("/sumar/<int:a>/<int:b>")
def sumar (a, b):
    resultado= a+ b
    return f"la suma de {a} y {b} es:  {resultado}"


@app.route("/pagina1/")
def page():
    return render_template("index.html")


#OPERACIONES CON PLANTILLAS

#1
@app.route("/bienvenida/<nombre>")
def bienvenida(nombre):
 return render_template("index.html", nombre=nombre)


#2
@app.route("/servicios")
def servicios():
 lista_servicios = ["Consulta", "Odontología", "Laboratorio", "Urgencias"]
 return render_template("index.html", servicios=lista_servicios)


# 3
@app.route("/fecha")
def mostrar_fecha():
 fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
 return render_template("index.html", fecha=fecha)


# 4
@app.route("/paciente")
def paciente():
 datos_paciente = {
 "nombre": "Carlos Gómez",
 "edad": 35,
 "servicio": "Consulta General",
 "fecha": "28/04/2025"
 }
 return render_template("index.html", paciente=datos_paciente)


# 5
@app.route("/pacientes")
def lista_pacientes():
 pacientes = [
 {"nombre": "Ana Ruiz", "edad": 30, "servicio": "Odontología"},
 {"nombre": "Luis Martínez", "edad": 45, "servicio": "Pediatría"},
 {"nombre": "Laura Gómez", "edad": 28, "servicio": "Laboratorio"}
 ]
 return render_template("index.html", pacientes=pacientes, paciente= paciente)


@app.route("/proyecto/")
def proy():
   return render_template("index1.html")


@app.route("/pagina2")
def pagina2():
   return render_template("index2.html", paciente= paciente)


#>>>>---------------------------------------------------->
@app.route('/grafico1/')
def grafico1():
#Datos para el gráfico
    x=[1,2,3,4,5]
    y=[10,14,16,20,25]
#Creación del gráfico
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title('crecimiento de ventas')
    plt.xlabel('Mes')
    plt.ylabel('Ventas')
#Guardar gráfico en un buffer
    buf= io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
#codificar imagen en base64
    imagen_base64= base64.b64encode(buf.getvalue()).decode('utf8')
    return render_template('index1.html', imagen= imagen_base64)


#>>>>---------------------------------------------------->

@app.route('/grafico_pie/')
def grafico_pie():
#Datos para el gráfico
    etiquetas= ['Python', 'Java', 'C++', 'JacaScript']
    tamanios= [40, 25, 20, 15]
   
#Creación del gráfico
    plt.figure(figsize=(6, 6))
    plt.pie(tamanios, labels= etiquetas, autopct='%1.1f%%', startangle=90)
    plt.title('Preferencia de Lenguarajes de programación')
    
#Guardar gráfico en un buffer
    buf= io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
#codificar imagen en base64
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    return render_template('index1.html', imagen= imagen)



#>>>>---------------------------------------------------->
@app.route('/grafico_ventas_productos/')
def grafico_ventas_productos():
    #Cargar archivo csv
    df= pd.read_csv('data/ventas_anuales.csv')

    #Agrupar por producto y sumar ventas
    resumen= df.groupby('Nombre Producto')['Ventas Totales'].sum().sort_values(ascending= False)

   
#Creación del gráfico
    plt.figure(figsize=(6, 3.5))
    resumen.plot(kind= 'bar', color='orange')
    plt.title('Ventas Totales por Producto')
    plt.xlabel('Producto')
    plt.ylabel('Ventas Totales')
    plt.xticks(rotation= 45)
    plt.tight_layout()
    
#Guardar gráfico en un buffer
    buf= io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
#codificar imagen en base64
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()
    return render_template('index1.html', imagen= imagen)


#>>>>---------------------------------------------------->  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method== 'POST':
        usuario= request.form['username']
        return f'Bienvenido, {usuario}'
    return '''
    <form method= "post">
    Usuario: <input type= "text" name="username">
    <br>
    <input type= "submit" value="Enviar">
    </form> '''


#>>>>---------------------------------------------------->

@app.route('/GraficoBarrasVertical')
def grafico_barras_vertical():
    
        categorias= ['Ene', 'Feb', 'Mar', 'Abr']
        valores= [15, 30, 45, 10]

        plt.figure(figsize=(6, 4))
        plt.bar(categorias, valores, color='peru')
        plt.title('Ventas por Mes')
        plt.xlabel('Mes')
        plt.ylabel('Ventas')
        
#Guardar gráfico en un buffer
        buf= io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
#codificar imagen en base64
        imagen = base64.b64encode(buf.getvalue()).decode('utf8')
        return render_template('index1.html', imagen= imagen)


#>>>>---------------------------------------------------->

@app.route('/GraficoBarrasHorizontal')
def grafico_barras_Horizontal():
    
        categorias= ['Ene', 'Feb', 'Mar', 'Abr']
        valores= [15, 30, 45, 10]

        plt.figure(figsize=(6, 4))
        plt.barh(categorias, valores, color='peru')
        plt.title('Ventas por Mes')
        plt.xlabel('Mes')
        plt.ylabel('Ventas')
        
#Guardar gráfico en un buffer
        buf= io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
#codificar imagen en base64
        imagen = base64.b64encode(buf.getvalue()).decode('utf8')
        return render_template('index1.html', imagen= imagen)


#>>>>---------------------------------------------------->

@app.route('/GraficoPersonalizado')
def grafico_Personalizado():
    
        meses= ['Ene', 'Feb', 'Mar', 'Abr', 'May']
        precios= [2000, 2200, 2100, 2500, 2400]

        plt.figure(figsize=(6, 4))
        plt.plot(meses, precios, linestyle='--', color='peru')
        plt.title('Evolución del precio')
        plt.xlabel('Mes')
        plt.ylabel('Precio en $')
        
#Guardar gráfico en un buffer
        buf= io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
#codificar imagen en base64
        imagen = base64.b64encode(buf.getvalue()).decode('utf8')
        return render_template('index1.html', imagen= imagen)


#>>>--------------------------------->  Imagen con plot
@app.route('/proyectoFinal/')
def integrarGraficos():
    
        año= ['2020', '2021', '2022', '2023', '2024', '2025']
        practicantes= [8, 12, 15, 22, 19, 32]

        plt.figure(figsize=(6, 4))
        plt.plot(año, practicantes, linestyle='--', color='peru')
        plt.title('Incremento de Practicantes -->')
        plt.xlabel('Año')
        plt.ylabel('Practicantes')

        buf= io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        imagen= base64.b64encode(buf.getvalue()).decode('utf8')


#>>>---------------------------------> Imagen dinámica
        labels= ["Enero", "Febrero", "Marzo", "Abril"]
        basico= [9, 6, 9, 2]
        premium= [1, 2, 2, 1]
        return render_template("index1.html", labels= labels, basico= basico, premium= premium, imagen= imagen)