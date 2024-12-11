import sys
import pypyodbc as odbc
from ... import DB_Configs as DBC

def ExecSql(sql, params):
    try:
        conn = odbc.connect(DBC.conn_string)
    except Exception as e:
        print(e)
        print('task is terminated')
        sys.exit()
    else:
        cursor = conn.cursor()
  
    try:
        if params == []:
            cursor.execute(sql, params=None)        
        else:
            cursor.execute(sql, params=params)        
    except Exception as e:
        print(e.value)
        print('transaction rolled back')
        cursor.rollback()
    else:
        print('SQL executed successfully')
        cursor.commit()
        cursor.close()
    finally:
        if conn.connected == 1:
            print('connection closed')
            conn.close()

def ExecSql_Int(sql, params):
    res = None
    try:
        conn = odbc.connect(DBC.conn_string)
    except Exception as e:
        print(">>> " + e)
        sys.exit()
    else:
        cursor = conn.cursor()
  
    try:
        if params == []:
            cursor.execute(sql, params=None)  
        else:
            cursor.execute(sql, params=params)   

        results = cursor.fetchone()     
        # res = (cursor.fetchall())[0]
        if results != None:
            res = results[0]
            print(res)

    except Exception as e:
        print(">>> " + e.value)
        print('">>> " + transaction rolled back')
        cursor.rollback()
    else:
        print('SQL executed successfully')
        cursor.commit()
        cursor.close()
    finally:
        if conn.connected == 1:
            conn.close()

    return res
        

