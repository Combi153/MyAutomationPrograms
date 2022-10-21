import pandas as pd
import openpyxl
from datetime import datetime, timedelta

class HeamsCheck(object):
    def __init__(self,filename,check_dict):
        self.filename=filename
        self.data_dict={}
        self.data_Dict=check_dict
        self.format='%Y.%m.%d. %H:%M'
        
    def fileread(self):
        with open ('/content/drive/MyDrive/Heams/file/{}.txt'.format(self.filename),'r',encoding='utf-8')as comment_file:
            copy=comment_file.read()
            copylist=copy.split('등록순최신순새로고침')
            self.copylist=copylist
        with open('/content/drive/MyDrive/Heams/member.txt','r',encoding='CP949')as member_file:
            self.member_list = [member_line.strip() for member_line in member_file]
        if 'Date' not in self.data_Dict:
            self.data_Dict['Date']=[]
            for i in self.member_list:
                self.data_Dict[i]=[]
    
    def writerCheck(self):
        writerCheck_list=self.copylist[0].split('\n') 
        writer_Name_Index=1+writerCheck_list.index('프로필 사진')
        self.writer_Name=writerCheck_list[writer_Name_Index][:-6]
        writer_uploadTime_Index=2+writerCheck_list.index('프로필 사진')
        uploadTime=writerCheck_list[writer_uploadTime_Index][:17]
        uploadTime_type=datetime.strptime(uploadTime,self.format)
        criteriaDate_upload=uploadTime[:11]
        self.criteriaDate_Time_upload=criteriaDate_upload+' 18:00'
        criteriaDate_upload_type=datetime.strptime(criteriaDate_upload,'%Y.%m.%d.')
        self.criteriaDate_Time_upload_type=datetime.strptime(self.criteriaDate_Time_upload,'%Y.%m.%d. %H:%M')
        self.data_Dict['Date'].append(criteriaDate_upload)
        
        if uploadTime_type <=self.criteriaDate_Time_upload_type:
            self.data_Dict[self.writer_Name].append('정상 업로드')
        else:
            self.data_Dict[self.writer_Name].append('업로드 지각')
            
    def commentCheck(self):
        commentCheck_list=self.copylist[1].split('댓글을 입력하세요')  
        commentCheck_list=commentCheck_list[0].split('프로필 사진')[1:]
        commentCheck_dict_time={}
        commentCheck_writername_list=[]
        criteriaTime_comment_type=self.criteriaDate_Time_upload_type+timedelta(days=1)
        for i in commentCheck_list:
            comment_writer=i[:7].strip()
            comment_write_time=i[-23:-5].strip()
            comment_write_time_type=datetime.strptime(comment_write_time, self.format)
            if comment_writer not in commentCheck_writername_list: 
                if comment_write_time_type > criteriaTime_comment_type:
                    commentCheck_writername_list.append(comment_writer)
                    self.data_Dict[comment_writer].append('힘즈 지각')
                elif comment_write_time_type <= criteriaTime_comment_type:
                    commentCheck_writername_list.append(comment_writer)
                    self.data_Dict[comment_writer].append('정상 작성')
            else:
                pass
        for i in self.member_list:
            if i != self.writer_Name and i not in commentCheck_writername_list:
                self.data_Dict[i].append('미작성자')
        
    def finesCalculation(self):
        category_list=['정상 작성','힘즈 지각','미작성자','정상 업로드','업로드 지각']
        for i in category_list:
            self.data_Dict['Date'].append(i)
        for j in list(self.data_Dict.keys())[1:]:
            for k in category_list:
                count=self.data_Dict[j].count(k)
                self.data_Dict[j].append(count)
        return self.data_Dict


file_count1=int(input('첫 번째 파일 이름을 넣어주세요 (예시 :1)'))
file_count2=int(input('마지막 파일 이름을 넣어주세요 (예시 :31)'))
file_count_list=[]
check_dict={}
try:
  for i in range(file_count1,file_count2+1):
    file_count_list.append(str(i))

  for i in file_count_list:
      start=HeamsCheck(i,check_dict)
      start.fileread()
      start.writerCheck()
      start.commentCheck()

  check_dict=start.finesCalculation()
  dataFrame_Check_dict=pd.DataFrame(check_dict)
  dataFrame_Check_dict.to_excel('/content/drive/MyDrive/Heams/Heams_Check.xlsx', index=0)
  print('작동 완료')

except Exception as e:
  print('오류 발생 재시도!',e)