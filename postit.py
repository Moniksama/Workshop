from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()



def connectBD():
    return mysql.connect()

def readBD():
    conn = connectBD()
    cursor = conn.cursor()
    cursor.execute("SELECT * from post_it")
    return cursor.fetchall()

@app.route("/")
def postit():
    return render_template('postit.html')


@app.route("/postit/listar_notas")
def listar_notas():
    datos = readBD()
    return render_template('listar_notas.html', data=datos)


if __name__ == "__main__":
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'postit'
    app.config['MYSQL_DATABASE_Host'] = 'localhost'

    mysql.init_app(app)
    app.run()
