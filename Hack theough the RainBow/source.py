import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    
    Hashlib_dict=OrderedDict()
    Main=OrderedDict()
    ResultPassword=OrderedDict()
    def hash_sha256(name:str):
        hash_object=hashlib.sha256()
        hash_object.update(name.encode("utf-8"))
        code=hash_object.hexdigest()
        return code

    for i0 in range(1000,10000):
        code=hash_sha256(str(i0))
        Hashlib_dict[str(i0)]=code
        

    with open(file=input_file_name) as csv_file:
        file=csv.reader(csv_file)
        for line in file:
            Main[line[0]]=line[1]

    for key in list(Main.keys()):
        val=Main.get(key)
        for i1 in list(Hashlib_dict.values()):
            if i1 == Main.get(key):
                for i2,j0 in Hashlib_dict.items():
                    if j0==i1:
                        Password=i2
        ResultPassword[key]=Password

    with open(file=output_file_name, mode='w', newline="") as file:
        CsvFile=csv.writer(file)
        for key in list(ResultPassword.keys()):
            name=[]
            name.append(key)
            name.append(ResultPassword.get(key))
            CsvFile.writerow(name)
    
    return output_file_name

