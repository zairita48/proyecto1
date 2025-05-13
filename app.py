from flask import Flask, render_template, request
import pandas as pd     #importar pandas al proyecto
import re
import matplotlib.pyplot as plt
import io           #renderizar gráficos
import base64

from datetime import datetime

app = Flask(__name__)
# Flask app.route decorador paa mapear la ruta URL / a esta función


@app.route("/")
def home():
    return "Holaa, Flask" 

@app.route("/pagina2")
def pagina2():
   return render_template("index2.html")


@app.route('/grafico_ventas/')
def grafico_ventas():
    #Cargar archivo csv
    df= pd.read_csv('data/Ventas.csv')

    #Agrupar por producto y sumar ventas
    df.groupby('Pago')['Costo'].plot(kind= 'bar', color='purple')
   
#Creación del gráfico
    plt.figure(figsize=(6, 3.5))
    plt.title('Modos de pago mas usados')
    plt.xlabel('Producto')
    plt.ylabel('Ventas Totales')
    
#Guardar gráfico en un buffer
    buf= io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
#codificar imagen en base64
    imagen1 = base64.b64encode(buf.getvalue()).decode('utf8')

    return render_template("index2.html", imagen1= imagen1)

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


#>>>--------------------------------->  Imagen con plot
@app.route('/proyectoFinal')
def integrarGraficos():
    
        año= ['2020', '2021', '2022', '2023', '2024', '2025']
        practicantes= [2, 4, 5, 9, 11, 12]

        plt.figure(figsize=(6, 4))
        plt.plot(año, practicantes, linestyle='--', color='peru')
        plt.title('Incremento -->')
        plt.xlabel('Año')
        plt.ylabel('Meses')

        buf= io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        imagen= base64.b64encode(buf.getvalue()).decode('utf8')

        df= pd.read_csv('data/Ventas.csv')

    #Agrupar por producto y sumar ventas
        df.groupby('Pago')['Costo'].plot(kind= 'bar', color='purple')
   
#Creación del gráfico
        plt.title('Modos de pago mas usados')
        plt.xlabel('Producto')
        plt.ylabel('Ventas Totales')
    
#Guardar gráfico en un buffer
        buf= io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
#codificar imagen en base64
        imagen1 = base64.b64encode(buf.getvalue()).decode('utf8')



#>>>---------------------------------> Imagen dinámica
        labels= ["Enero", "Febrero", "Marzo", "Abril"]
        basico= [9, 6, 9, 8]
        premium= [5, 8, 4, 7]
        return render_template("index1.html", labels= labels, basico= basico, premium= premium, imagen= imagen, imagen1= imagen1)