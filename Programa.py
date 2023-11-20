from flask import Flask, render_template

class Programa: 

    def _init_(self):
        
        self.app=Flask(_name_)
        self.app.config['SQLALCHEMY_DATABSE_URI']="sqlite:///estudiantes.sqlite3"
        self.app.add_url_rule('/nuevo', view_func=self.agregar)
        
        #Iniciar Repositorio
        with self.app.app_context()
            db.
        
        self.app.run(debug=True)
        

    def agregar(self):
        return render_template('nuevoEstudinate.html')
        
miPrograma=Programa()