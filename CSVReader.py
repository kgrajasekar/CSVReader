# using_lambdas.py

class CSVReader:
    def __init__(self, filename, HasHeader):
        self.filename=filename
        self.RowCount=0
        self.ColCount=0
        self.HasHeader=HasHeader
        self.ColHeader=[]
        self.csvData=[]
        self.ReadCSV()

    def ReadCSV(self):
        self.csvData = []
        row = []
        field = ""
        inQuotedField = False
        laspos = 0
        with open(self.filename, "r") as fs:
            while True:
                tx = fs.read(2)
                if tx == '':
                    #print('End Of File')
                    break
                else:
                    current = tx[0]
                    next = (" " if (0 == (len(tx) - 1)) else tx[(0 + 1)])
                    if (laspos != fs.tell()):
                        laspos = fs.tell()
                        fs.seek(fs.tell()-1)

                    if (((current == "\\") and (next == "\"")) and inQuotedField):
                        fs.seek(fs.tell()+1)
                        field += next
                    elif (((current == "\\") and (next == ",")) and (not inQuotedField)):
                        fs.seek(fs.tell()+1)
                        field += next
                    elif ((((((current != "\"") and (current != ",")) and (current != "\r")) and (current != "\n"))) or (((current != "\"") and inQuotedField))):
                        field += current
                    elif ((current == " ") or (current == "\t")):
                        continue
                    elif (current == "\""):
                        if (inQuotedField and (next == "\"")):
                            fs.seek(fs.tell()+1)
                            field += current
                        elif inQuotedField:
                            row.append(field)
                            if (next == ","):
                                fs.seek(fs.tell()+1)
                            field = ""
                            inQuotedField = False
                        elif (((field != "") and (not inQuotedField)) and (next == ",")):
                            field += current
                        else:
                            inQuotedField = True
                    elif (current == ","):
                        row.append(field)
                        field = ""
                    elif (current == "\n"):
                        row.append(field)
                        self.csvData.append(row)
                        field = ""
                        row=[]
                    #print(file_eof)
        self.RowCount =len(self.csvData)
        self.ColCount = 0 if self.RowCount==0 else len(self.csvData[0])
        self.ColHeader = [] if self.RowCount==0 else self.csvData[0]
        #return parsedCsv   

    def GetRow(self,rowindex,value=None):
        return self.csvData[rowindex] if self.RowCount > rowindex else value

    def InsertRow(self,rowIndex,rowArray):
        pass #return self.csvData[rowindex] if self.RowCount > rowindex else None

    def AddCol(self,colName,value=""):
        if self.ColHeader.index(colname)==-1:
            firstcolumn=True
            for r in self.csvData:
                if firstcolumn==False:
                    r.append(value)
                else:
                    firstcolumn=False
                    r.append(colname)
                    self.ColHeader.append(colname)
            return True
        else:
            return False
    def RemoveCol(self,colName):
        pass #return self.csvData[rowindex] if self.RowCount > rowindex else None

    def InsertCol(self,colIndex,colName,value=""):
        
        pass #return self.csvData[rowindex] if self.RowCount > rowindex else None

    def GetData(self,rowindex,colname,value=None):
        rowdata = self.GetRow(rowindex)
        if rowdata!=None:
            colindex = colname if isinstance(colname, int) else self.ColHeader.index(colname)
            if colindex>=0:
                return rowdata[colindex]
        return value

    def SetData(self,rowindex,colname,value=""):
        rowdata = self.GetRow(rowindex)
        #rowdata = self.csvData[rowindex] if self.RowCount<rowindex else None
        if rowdata!=None:
            colindex = colname if isinstance(colname, int) else self.ColHeader.index(colname)
            if colindex>=0:
                rowdata[colindex]=value
                return True
        return False

    def Save(self):
        return self.SaveAs(self,self.filename)

    def SaveAs(self,filename):
        dq='"'
        sep=','
        ln='\n'
        with open(filename, "w") as fs:
            for r in self.csvData:
                firstColumn = True
                for c in r:
                    if firstColumn==False:
                        fs.write(sep)
                    if c.find(dq)==-1 and c.find(sep)==-1:
                        fs.write(c)
                    else:
                        d=dq+c.replace(dq, '\"\"' )+dq
                        fs.write(d)
                    firstColumn=False
                fs.write(ln)
        return True
        
# a main function that uses our factorial function defined above
def main():
    #print("I am the factorial helper")
    #print("you can call factorial(number) where number is any integer")
    #print("for example, calling factorial(5) gives the result:")
    #print(factorial(5))
    #csvObj=CSVReader(r"C:\Users\kgraj\Downloads\rule_check\test.csv")
    #csvObj.ReadCSV()
    print(csvObj.filename)
    print('rowcount  ->',csvObj.RowCount)
    print('colcount  ->',csvObj.ColCount)
    print('rowHeader ->',csvObj.ColHeader)
    print('GetRow    ->',csvObj.GetRow(1))
    print('GetRow    ->',csvObj.GetRow(2))
    print('GetRow    ->',csvObj.GetRow(3))
    print('GetRow    ->',csvObj.GetRow(4))
    print('GetRow    ->',csvObj.GetRow(5))
    print('GetRow    ->',csvObj.GetRow(6))
    print('GetDataInt->',csvObj.GetData(1,2))
    print('GetDataStr->',csvObj.GetData(1,"text_with_node"))
    print('AddCol->',csvObj.GetData(1,"Test1"))
    print('AddCol->',csvObj.GetData(1,"Test1","0"))
    print('SaveAs->',csvObj.SaveAs(r"C:\Users\kgraj\Downloads\rule_check\test2.csv"))
    
# this executes when the module is invoked as a script at the command line
if __name__ == '__main__':
    main()
    #main2()
    
