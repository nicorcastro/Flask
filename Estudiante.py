from db import db 

class Estudiante(db.Model):
    
    #Nombre tabla
    _tablename_="estudiante"
    
    #Conjunto de atributos que van a ser los campos de lña tabla 
        #Llave primaria
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    email=db.Column(db.String(70))
    codigo=db.Column(db.String(15))
    
    #Metodo constructor para mapear datos a los campos definidos
    def _init_(self, nombre, email, codigo):
        
        self.nombre=nombre
        self.email=email
        self.codigo=codigo