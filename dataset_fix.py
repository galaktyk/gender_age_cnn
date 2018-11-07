import numpy as np
import csv

def create_anns_csv():

    gender_dict = {'m':'1 0','f':'0 1'}
    age_dict = {'(0, 2)':'1 0 0 0 0 0 0 0','(4, 6)':'0 1 0 0 0 0 0 0','(8, 12)':'0 0 1 0 0 0 0 0',\
                '(15, 20)':'0 0 0 1 0 0 0 0','(25, 32)':'0 0 0 0 1 0 0 0','(38, 43)':'0 0 0 0 0 1 0 0',\
                '(48, 53)':'0 0 0 0 0 0 1 0','(60, 100)':'0 0 0 0 0 0 0 1'}

    #folder  |  jpeg  |  id  |  age  |  gender  
    anns = np.loadtxt('anns/fold_frontal_4_data.txt',dtype=str, usecols = (0,1,2,3,4),delimiter='\t')

    f = open('anns/'+'anns_full.csv',  mode='a',newline='')
    writer=csv.writer(f)


    for row in anns:
        
        age = row[3]
        if age not in age_dict:
            continue
        row[3] = row[3].replace(', ','-')
        
        gender = row[4]
        if gender not in gender_dict:
            continue 



        row = np.append(row,gender_dict[gender])
        row = np.append(row,age_dict[age])

        writer.writerow(row)
        
    f.close()


if __name__ == '__main__':
    create_anns_csv()