from sre_parse import Verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()     #인증시스템에 있는 모델을 가져옴

# 질문( 제목 카테고리/제목//이메일(답변수신을 이메일로 받겠습니다. 체크박스)//문자메시지(답변수신을 문자메시지로 받겠습니다. 체크박스)//내용//이미지(파일업로드하기))
class Inquiry(models.Model):
    
    status_choice = (
        ('ER', '문의 등록'),
        ('CA', '접수 완료'),
        ('AC', '답변 완료'),
    )
    status_list = models.CharField( max_length=10,verbose_name='상태', choices=status_choice, default='ER')

#제목카테고리와 제목
    #question = models.CharField(max_length=10, verbose_name='제목', null=False)
    category_choice = (
        ('NU', '선택해주세요.'),
        ('GE', '일반'),
        ('AC', '계정'),
        ('ET', '기타'),
    )
    category_list = models.CharField( max_length=10,verbose_name='카테고리', choices=category_choice, default='NU')
    question = models.CharField(max_length=50, verbose_name='제목', null=False)

# 이메일(체크박스만들기)
    user_email = models.EmailField(max_length=128, verbose_name='이메일',null=True)
    email_checkbox = models.BooleanField('답변수신을 이메일로 받겠습니다.', default=False)

# 문자메시지
    phone_number = models.CharField(max_length=11, verbose_name='문자메시지',null=True)
    phone_checkbox = models.BooleanField('답변수신을 문자로 받겠습니다.', default=False)
# 내용
    inquiry_content = models.TextField(verbose_name='내용',default='질문 내용을 입력하세요..')

# 이미지
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)

# 생성자
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='inquiry_writer', verbose_name='생성자', default='1')

# 생성일시
    created_date = models.DateTimeField(verbose_name='생성일시', auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.question}'



# 답변모델 필드 (답변내용 참조문의글 생성자 생성일시 최종수정자 최종수정일시)
class Answer(models.Model):
    answer_content = models.TextField(verbose_name='답변내용', null=False)

# 참조문의글
    wh_inquiry = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE,default='')

# 생성자
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='생성자', null=False, blank=False)

#생성일시
    created_date = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)

# 최종수정자
    last_modi_writer = models.ForeignKey(verbose_name='최종 수정자', to=User, on_delete=models.CASCADE, null=True, related_name='last_modi_writer_question')

# 최종수정일시
    updated_date = models.DateTimeField(verbose_name='최종 수정일', auto_now=True)




# 자꾸 오류떠서 계속해서 migrations-migrate반복,, 검색결과 migrations가 이미 정해져있으면 그런가봄.. 터미널 오류 계속 검색해서 해결함
# 체크박스는 models.BooleanField 로 생성

