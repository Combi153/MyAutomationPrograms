from openpyxl import load_workbook

# data_only=True로 해줘야 수식이 아닌 값으로 받아온다.
load_wb = load_workbook("칼럼피드백.xlsx", data_only=True) #저장위치, 파일명 맞추기(예시 : "C:/Users/주찬민/Desktop/0601 칼럼피드백.xlsx")

# 시트 이름으로 불러오기
load_ws = load_wb['설문지 응답 시트1']

i = 2 ; Data = []
while True :
    # 읽어올 데이터가 없다면 
    if load_ws[f'C{i}'].value is None : break

    #시간 이름 제외 모든 데이터 저장
    for cell in load_ws[f'C{i}': f'N{i}']:
        Data.append( [row.value for row in cell] )
    i += 1

#파일 쓰기
j=0
for number in range(1,5):
    
    with open("{}번째 발표자.txt".format(number), "wt") as f:
        
        #칼럼에서 좋았던 점
        i=0
        f.write(load_ws[f'C{1}'].value + '\n')#열 제목
        for D in Data :
            if D[j] is None : continue #아무것도 안쓴 칸 넘기기
            if len(D[j]) <= 2 : continue #점 하나 찍거나 그런 이상한 것들 넘기기
            i+=1
            f.write(str(i)+' : ') #번호 매기기
            f.write(D[j] + '\n') #내용 적고 한 줄 띄기
            
        #칼럼에서 개선할 점
        i=0
        f.write('\n'+load_ws[f'D{1}'].value + '\n')
        for D in Data :
            if D[j+1] is None : continue
            if len(D[j+1]) <= 2 : continue
            i+=1
            f.write(str(i)+' : ')
            f.write(D[j+1] + '\n')
            
        #질문
        i=0
        f.write('\n'+load_ws[f'E{1}'].value + '\n')
        for D in Data :
            if D[j+2] is None : continue
            if len(D[j+2]) <= 2 : continue
            i+=1
            f.write(str(i)+' : ')
            f.write(D[j+2] + '\n')

    j+=3 #발표자 바꾸기 위한 더하기
