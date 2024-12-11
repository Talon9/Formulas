import glob
import Classes.cImportFormula as NF
import Classes.cImportFormulaLines as IFL
         
for file in glob.glob(r'H:\FoodData\Cheesecake\*-1.txt'):
    with open (file, 'r') as f:

        fname = f.name
        fname = fname[1+fname.rfind("\\"):]
        F = NF.ImportFormula(importFormulaID=None, filename=fname, formulaNameOrig=fname)
        F.importFormulaID = F.get_ImportFormulaID( )[0]

        f_contentline = f.readline()
        i = 1
        while len(f_contentline)>0:
            newLine = f_contentline[:-1].strip()
            if len(newLine)>0:
                FL = IFL.ImportFormulaLines(importFormulaID=F.importFormulaID, 
                                             lnSeq=i, 
                                             lnTxt=f_contentline
                                             )
                IFL.ImportFormulaLines.FormulaLines_AddUpd()
                print(FL)
                i=i+1                
            f_contentline = f.readline()
        
        if F.importFormulaID > 0:
            print(F)
            print('-----------------------')

      



        # sql = "SELECT FormulaID FROM pyFormulas Where Filename = '" + f.name + "' "
        # id = DB.ExecSql_Int(sql, None)
        # print(f'ID: {id}')

        # if id is None:
        #     print(f'Load {f.name}')
        #     NewFormula.LoadFormulaName(f.name, f.name)
        
        # sql = "SELECT FormulaID FROM pyFormulas Where Filename = '" + f.name + "' "
        # id = DB.ExecSql_Int(sql, None)
        # print(f'ID: {id}')
        # print('')
        # print('')
        



