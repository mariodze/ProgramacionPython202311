import sqlite3

class Bd:
    def __init__(self,bdName='exampleBdv1'):
        self.bdName=f'{bdName}.db'
        try:
            self.conexion = sqlite3.connect(self.bdName)
        except Exception as E:
            print('error',e)
    #metodos
    def newTable(self,tabla,sentencia):
        try:
            query = "CREATE TABLE IF NOT EXISTS {} ({});".format(tabla,sentencia)
            print(query)
            cnn=self.conexion
            cursor=cnn.cursor()
            cursor.execute(query)
            cnn.commit()
        except Exception as e:
            print('error',e)
    
    def insertValueOne(self,tabla,sentencia):
        try:
            query=f"""
            INSERT INTO {tabla} VALUES{sentencia};
            """
            cnn=self.conexion
            cursor=cnn.cursor()
            cursor.execute(query)
            cnn.commit()    # confiramcion de mi cambio
        except Exception as e:
            print('error',e)
    def insertFromPrompt(self,tabla,sentencia,values):
        query=f"""
            INSERT INTO {tabla} VALUES({sentencia})
        """
        cnn=self.conexion
        cursor=cnn.cursor()
        cursor.execute(query,values)

    def lecturaTabla(self,tabla):
        try:
            query=f"SELECT * FROM {tabla};"
            print(query)
            cnn=self.conexion
            cursor=cnn.cursor()
            cursor.execute(query)
            data=cursor.fetchall()
            print(data)
            return data
        except Exception as e:
            print('error',e)
            
    def closedBd(self):
        self.conexion.close()
    

bd1=Bd('examplewithclass')
#bd1.newTable('useres','nombre varchar(100), dni varchar(100),edad integer')
#bd1.insertValueOne('useres',"('gian','887877',20)")
bd1.lecturaTabla('useres')
## 

## en casos como estos se vuelve impractico
"""def bdFx(bdName='exampleBdv2')
   bdName=f'${bdName}.db'
   conexion=sqlite3.connect(bdName)
   newTableFx(tabla,sentencia) 
   closedFx()

def newTableFx(tabla,sentencia):
    try:
        query=f"CREATE TABLE IF NOT EXISTS {tabla}(
            {sentencia}
        )
        
        cnn=self.conexion
        cursor=cnn.cursor()
        cursor.execute(query)
        cnn.commit()
    except Exception as E:
        print('error',e)

def closedFx(conexion):
    try:
        conexion.close()
    except Exception as E:
        print('error',e)


bdFx('ejemplo10')"""