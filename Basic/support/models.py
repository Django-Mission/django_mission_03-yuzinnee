from re import T
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()		#인증시스템에 있는 모델을 가져옴

# 질문 카테고리 답변 생성자 생성일시 최종수정자 최종수정일시
class Faq(models.Model):
# 질문
    question = models.TextField(verbose_name='제목', null=False)

#카테고리(일반 계정 기타)
    category_choice = (
        ('GE', '일반'),
        ('AC', '계정'),
        ('ET', '기타'),
    )
    category_list = models.CharField(verbose_name='카테고리', max_length=2, choices=category_choice, default='GE')

# 답변
    answer = models.TextField(verbose_name='답변', null=False)

# 생성자
    writer = models.ForeignKey(verbose_name='생성자', to=User, on_delete=models.CASCADE, null=True, blank=True)

# 생성일시
    created_date = models.DateTimeField(verbose_name='생성일시',auto_now_add=True,null=True)

#최종수정자
    last_modi_writer = models.ForeignKey(verbose_name='최종 수정자', to=User, on_delete=models.CASCADE, null=True, related_name='last_modi_writer_question')

# 최종수정일시
    updated_date = models.DateTimeField(verbose_name='최종 수정일시', auto_now=True, null=True)
    def __str__(self):
        return f'[{self.pk}]{self.question}'
# migration이 안되었던 이유는 null이나 default값이 설정되지 않았기 때문
# 가상홈에서 노란박스 오류가 뜨는 이유는 migrate가 안되었고 받은 정보값이 없어서(maybe)
# writer와 last_modi_writer간의 User 충돌 문제가 발생하여 related_name='last_modi_writer_question'를 추가했더니 오류가 사라짐