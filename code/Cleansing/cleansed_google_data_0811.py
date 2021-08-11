
import os.path
import pandas as pd
import re

path = '../../resource/CrawlingData/'
detail_dir = ['clinic','fitness','hospital']
lenList=[]
total_csv =[]
for i in detail_dir:    #  파일 내에 있는 모든 csv파일명 가져옴
    file_list = os.listdir(path+i)
    file_list_py = [re.sub(".csv","",file) for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .csv인 경우
    # print(file_list_py)
    a=len(file_list_py)
    lenList.append(a)
    total_csv.append(file_list_py)
# print(total_csv)
# print(len(total_csv[2]))


# 1. 각 csv 파일 내 중복 , 더미데이터 제거
#clinic
new_clinic = list()
print(total_csv[0])
for i in total_csv[0]:
    data_csv = pd.read_csv("../../resource/CrawlingData/clinic/" + i+'.csv')
    print(i,"\tlength of raw data: ", len(data_csv), end='')
    data_csv = data_csv.drop_duplicates(['Url'])  # 중복 제거
    # new_data = data_csv.dropna(subset=['Category', 'Address'], how='all')  # 더미데이터 제거
    print("\tlength of new data : ", len(data_csv))
    data_csv = data_csv.reset_index(drop=True)
    new_clinic.append(data_csv)


# Fitness
new_fitness = list()
print(total_csv[1])
for j in total_csv[1]:
    data_csv = pd.read_csv("../../resource/CrawlingData/fitness/" + j+'.csv')
    print(j, "\tlength of raw data: ", len(data_csv), end='')
    data_csv = data_csv.drop_duplicates(['Url'])  # 중복 제거
    # new_data = data_csv.dropna(subset=['Category', 'Address'], how='all')  # 더미데이터 제거
    print("\tlength of new data : ", len(data_csv))
    data_csv = data_csv.reset_index(drop=True)
    new_fitness.append(data_csv)

# Hospital
new_hospital = list()
print(total_csv[2])
for j in total_csv[2]:
    data_csv = pd.read_csv("../../resource/CrawlingData/hospital/" + j+'.csv')
    print(j, "\tlength of raw data: ", len(data_csv), end='')
    data_csv = data_csv.drop_duplicates(['Url'])  # 중복 제거
    # new_data = data_csv.dropna(subset=['Category', 'Address'], how='all')  # 더미데이터 제거
    print("\tlength of new data : ", len(data_csv))
    data_csv = data_csv.reset_index(drop=True)
    new_hospital.append(data_csv)

#2 카테고리 키워드 제거
drop_list_hos = ['eye', 'dental', 'animal', 'psychiatric', 'family', 'skin', 'hair', 'psychiatrist', 'ophthalmology', "road cycling", 'dentist'
              , 'dental','psychiatrist','parking','electronics','chiropractor','skin','hair','visa', 'derma','mental','freight','taxi','bus','watch',
              'industrial','phone','college','pharmacy','guest','car','insurance','solar','alternative','auto','labor', 'dental','community','box',
              'architecture','coffee','school','manufacturer','homeopath','printing','dairy','dry','grocery','photo','education center','phone','bank',
              'linen','corporate office','motor','baby store','criminal','statue','herbal medicine','furniture','marrage','appliance store','costume',
              'publisher','telecommunicatons','garden','familypractice','railway','video arcade','panipury', 'tourist attraction', 'secondary','seal shop',
              'store','government office','veterinarian']

drop_list_clinic = ['skin care' ,'dermatology','hair transplantation','dental','eye','beauty salon','veterinarian','animal','veterinary','alternative',
              'pet','dentist','school','state government office','computer service','community health','psychologist','homeopath','shopping mall',
              'environmental health service','lawyer','car leasing','lasik','park','dermatologist','parking garage','church','bank','hotel',
              'water purification','dairy store','gas comapny','news','restaurant','plastic surgeon', 'non-profit organization','orthodontist',
              'optician','sexologist','drug store','speech','oral','car repair','day care center','tour','radiologist','pharmacy',
              'hair removal','caterer','corporate','library','general store','lodging','atm']

drop_list_fit = ['martial arts school','exercise equipment store','business center','fitness equipment','supplements','trainer','make-up','dance',
              'grocery store','recruiting','repair service','instructor','butcher shop','meditation center','sports nutrition','university',
              'health and beauty','design','wellness center','store','oxygen cocktail','manufacturer','park', 'fencing', 'consultant',
              'energy equipment','educational institution','playground','tempororily','religious institution' ]


# Clinic
print('-----------CLINIC------------')
cnt = 0
for data in new_clinic:
    row_list = []
    print('Before: ',len(data), end='\t')
    for row in data.index:
        category = str(data['Category'][row]).lower()
        for l in drop_list_clinic:
            if (l in category):
                row_list.append(row)
    data = data.drop(index=row_list, axis=0)
    print('After:', len(data))
    data.to_csv('../../resource/CleansedData/GoogleMap/Clinic/'+total_csv[0][cnt]+'_cleansed.csv',index=False)
    cnt += 1


# Fitness
print('-----------FITNESS------------')
cnt = 0
for data in new_fitness:
    row_list = []
    print('Before: ',len(data), end='\t')
    for row in data.index:
        category = str(data['Category'][row]).lower()
        for l in drop_list_fit:
            if (l in category):
                row_list.append(row)
    data = data.drop(index=row_list, axis=0)
    print('After:', len(data))
    data.to_csv('../../resource/CleansedData/GoogleMap/Fitness/' + total_csv[1][cnt]+'_cleansed.csv', index=False)
    cnt += 1


# Hospital
print('-----------HOSPITAL------------')
cnt = 0
for data in new_hospital:
    row_list = []
    print('Before: ',len(data), end='\t')
    for row in data.index:
        category = str(data['Category'][row]).lower()
        for l in drop_list_hos:
            if (l in category):
                row_list.append(row)
    data = data.drop(index=row_list, axis=0)
    print('After:', len(data))
    data.to_csv('../../resource/CleansedData/GoogleMap/Hospital/' + total_csv[2][cnt]+'_cleansed.csv', index=False)
    cnt += 1