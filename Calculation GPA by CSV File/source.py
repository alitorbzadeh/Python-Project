import csv
# For the average
from statistics import mean 
from collections import OrderedDict


def calculate_averages(input_file_name, output_file_name):
    grades=OrderedDict()
    with open(file=input_file_name) as csvfile:
        CsvGrade=csv.reader(csvfile)
        for row in CsvGrade:
            b=[int(x) for x in row[1:]]
            grades[row[0]]=mean(b)
    
    with open(file=output_file_name, mode='w', newline='') as result_csvfile:
        CsvWiter=csv.writer(result_csvfile)
        for i0 in grades.keys():
            EachGrade=[]
            EachGrade.append(i0)
            EachGrade.append(float(grades[i0]))
            CsvWiter.writerow(EachGrade)

    return output_file_name


def calculate_sorted_averages(input_file_name, output_file_name):
    grades=OrderedDict()
    with open(file=input_file_name) as csvfile:
        CsvGrade=csv.reader(csvfile)
        for row in CsvGrade:
            b=[int(x) for x in row[1:]]
            grades[row[0]]=mean(b)
        
    def Assending_grade(dict_input):
        def key_dict(dict,value):
            keys=[]
            for i in dict.items():
                if i[1]==value:
                    keys.append(i[0])
                    keys=(sorted(keys))
            return keys

        new_grade=dict()
        k=None
        for i in sorted(dict_input.values()):
            if i==k:
                k=i
                pass
            else:
                keys=key_dict(dict=dict_input,value=i)
                if len(keys)!=1:
                    for i2 in keys:
                        new_grade[i2]=i
                    k=i
                else:
                    new_grade[keys[0]]=i
                    k=i
        return new_grade
    
    sorted_avrage=Assending_grade(dict_input=grades)
    print(sorted_avrage)

    with open(file=output_file_name, mode='w', newline='') as result_csvfile:
        CsvWiter=csv.writer(result_csvfile)
        for i0 in sorted_avrage.keys():
            EachGrade=[]
            EachGrade.append(i0)
            EachGrade.append(float(sorted_avrage[i0]))
            CsvWiter.writerow(EachGrade)


def calculate_three_best(input_file_name, output_file_name):
    grades=OrderedDict()
    with open(file=input_file_name) as csvfile:
        CsvGrade=csv.reader(csvfile)
        for row in CsvGrade:
            b=[int(x) for x in row[1:]]
            grades[row[0]]=mean(b)
        
    def Assending_grade(dict_input):
        def key_dict(dict,value):
            keys=[]
            for i in dict.items():
                if i[1]==value:
                    keys.append(i[0])
                    keys=(sorted(keys))
            return keys

        new_grade=dict()
        k=None
        for i in sorted(dict_input.values()):
            if i==k:
                k=i
                pass
            else:
                keys=key_dict(dict=dict_input,value=i)
                if len(keys)!=1:
                    for i2 in keys:
                        new_grade[i2]=i
                    k=i
                else:
                    new_grade[keys[0]]=i
                    k=i
        return new_grade
    
    sorted_avrage=Assending_grade(dict_input=grades)
    best_three_grade=OrderedDict()
    for i2 in range(-1,-4,-1):
        best_three_grade[list(sorted_avrage.keys())[i2]]=sorted_avrage.get(list(sorted_avrage.keys())[i2])
    
    print(best_three_grade)

    with open(file=output_file_name, mode='w', newline='') as result_csvfile:
        CsvWiter=csv.writer(result_csvfile)
        for i0 in best_three_grade.keys():
            EachGrade=[]
            EachGrade.append(i0)
            EachGrade.append(float(best_three_grade[i0]))
            CsvWiter.writerow(EachGrade)


def calculate_three_worst(input_file_name, output_file_name):
    grades=OrderedDict()
    with open(file=input_file_name) as csvfile:
        CsvGrade=csv.reader(csvfile)
        for row in CsvGrade:
            b=[int(x) for x in row[1:]]
            grades[row[0]]=mean(b)
        
    def Assending_grade(dict_input):
        def key_dict(dict,value):
            keys=[]
            for i in dict.items():
                if i[1]==value:
                    keys.append(i[0])
                    keys=(sorted(keys))
            return keys

        new_grade=dict()
        k=None
        for i in sorted(dict_input.values()):
            if i==k:
                k=i
                pass
            else:
                keys=key_dict(dict=dict_input,value=i)
                if len(keys)!=1:
                    for i2 in keys:
                        new_grade[i2]=i
                    k=i
                else:
                    new_grade[keys[0]]=i
                    k=i
        return new_grade
    
    sorted_avrage=Assending_grade(dict_input=grades)
    worst_three_grade=OrderedDict()
    for i2 in range(3):
        worst_three_grade[list(sorted_avrage.keys())[i2]]=sorted_avrage.get(list(sorted_avrage.keys())[i2])
    
    print(worst_three_grade)

    with open(file=output_file_name, mode='w', newline='') as result_csvfile:
        CsvWiter=csv.writer(result_csvfile)
        for i0 in worst_three_grade.keys():
            EachGrade=[]
            EachGrade.append(float(worst_three_grade[i0]))
            CsvWiter.writerow(EachGrade)


def calculate_average_of_averages(input_file_name, output_file_name):
    grades=OrderedDict()
    with open(file=input_file_name) as csvfile:
        CsvGrade=csv.reader(csvfile)
        for row in CsvGrade:
            b=[int(x) for x in row[1:]]
            grades[row[0]]=mean(b)
    
    b=mean(list(grades.values()))

    with open(file=output_file_name, mode='w', newline='') as result_csvfile:
        CsvWiter=csv.writer(result_csvfile)
        EachGrade=[]
        EachGrade.append(b)
        CsvWiter.writerow(EachGrade)

    return output_file_name