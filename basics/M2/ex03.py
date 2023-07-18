import csv
class CsvReader():
    def __init__(self, filename=None, sep=’,’, header=False, skip_top=0, skip_bottom=0):
        # ... Your code here ...
        self.filename=filename
        self.sep=supe
        self.header=header
        self.skip_top=skip_top
        self.skip_bottom=skip_bottom
        self.file=None
        

    def __enter__(self):
        self.file=open(self.filename,'r')
        return self.file
    def __exit__(self):
        if self.file:
            self.file.close()
    def getdata(self):
        reader=scv.reader(self.file,delimenater=self.sep)
        arr= list(reader)
        arr=arr[self.skip_top:len(arr)-self.skip_bottom]
            
    def getheader(self):
        if self.header:
            return scv.reader(self.file,delimenater=self.sep)[0]
        else :
            return None