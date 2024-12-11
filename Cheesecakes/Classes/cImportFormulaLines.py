import sys
import pypyodbc as odbc
import DB   as DB
import DB_Configs
from dataclasses import dataclass, field
from Classes.cImportType import ImportType

@dataclass
class ImportFormulaLines:
    importFormulaID: int
    lnSeq: int
    lnTxt: str
    importTypeID: ImportType = 0
    importSeq: int = 0

    def FormulaLines_AddUpd(self):
        result = []
        try:
            conn = odbc.connect(DB_Configs.conn_string)
        except Exception as e:
            print(e)
            print('task is terminated')
            sys.exit()
        else:
            cursor = conn.cursor()

        try:
            cursor.execute('{CALL pr_IFL_AddUpd(?, ?, ?)}', params= [self.importFormulaID, self.lnSeq, self.lnTxt])    
            result = cursor.fetchone() 
        except Exception as e:
            print(e.value)
            print('transaction rolled back')
            cursor.rollback()
        else:
            print('records inserted successfully')
            cursor.commit()
            cursor.close()
        finally:
            if conn.connected == 1:
                print('connection closed')
                conn.close()

        return result
    
#---------------------------
