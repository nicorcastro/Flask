from flask import Flask, render_template

class Programa:
    def_init_(self):
        self.app=Flask(_name_)
        self.app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///estudiantes.sqlite3"
        self.app.add_url_rule("/nuevo",view_func=self.agregar)
        
#Iniciar el servidor
self.app.run(debug=True)

def agregar(self):
    return render_template("nuevoEstudiante.html")