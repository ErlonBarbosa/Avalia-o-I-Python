from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='gisele*14',
    database='je_veiculos'
)

cursor = conexao.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM veiculos")
    veiculos = cursor.fetchall()
    return render_template('inicial.html', veiculos=veiculos)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_veiculo():
    if request.method == 'POST':
        vei_tipo = request.form['tipo']
        vei_cor = request.form['cor']
        vei_modelo = request.form['modelo']
        vei_marca = request.form['marca']
        vei_ano = request.form['ano_fabricacao']
        vei_estado = request.form['estado']
        vei_km_rodados = request.form['km_rodados']
        vei_leilao = request.form['passagem_leilao']
        vei_formas_pagamento = request.form['formas_pagamento']

        comando = "INSERT INTO veiculos (vei_tipo, vei_cor, vei_modelo, vei_marca, vei_ano, vei_estado, vei_km_rodados, vei_leilao, vei_formas_pagamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (vei_tipo, vei_cor, vei_modelo, vei_marca, vei_ano, vei_estado, vei_km_rodados, vei_leilao, vei_formas_pagamento)
        
        print("Valores a serem inseridos:")
        print(valores)  # Adicione esta linha para imprimir os valores

        cursor.execute(comando, valores)
        conexao.commit()

        return redirect('/')  # Redireciona para a página inicial após adicionar o veículo

    return render_template('adicionar.html')


@app.route('/lista')
def listar_veiculos():
    cursor.execute("SELECT * FROM veiculos")
    veiculos = cursor.fetchall()
    return render_template('lista.html', veiculos=veiculos)


@app.route('/excluir/<int:id_veiculo>', methods=['POST'])
def excluir_veiculo(id_veiculo):
    cursor.execute("DELETE FROM veiculos WHERE id=%s", (id_veiculo,))
    conexao.commit()
    return redirect('/') 


if __name__ == '__main__':
    app.run()
