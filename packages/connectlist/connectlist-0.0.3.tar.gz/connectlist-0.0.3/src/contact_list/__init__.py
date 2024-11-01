import csv
def create(name):
    name=name+'.csv'
    try:
        file=open(name,'r')
        print('contact book  already exist')
    except Exception as e:
        file=open(name,'w')
        x=csv.writer(file)
        x.writerow(['name','specification','contact no'])
        file.close()
def write(fn,people='',specification='',contact_no=''):
    name=fn+'.csv'
    file=open(name,'a',newline='')
    x=csv.writer(file)
    x.writerow([people,specification,contact_no])
    file.close()
def  view(name):
     name=name+'.csv'
     file=open(name,'r')
     x=csv.reader(file)
     d=list(x)
     return d
def search(name,ser=''):
     name=name+'.csv'
     file=open(name,'r')
     x=csv.reader(file)
     d=list(x)
     res=[]
     for i in range (len(d)):
         for x in range (len(d[i])):      
             if d[i][x]==ser:
                 res.append(d[i])
                 
     return res
