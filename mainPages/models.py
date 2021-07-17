from django.db import models
#from django.contrib.postgres.fields import ArrayField


# Create your models here.


class MainPage_section(models.Model) :
    MAINPAGE_SECTION = (
        ( 'a', '비트코인' ),
        ( 'b', '사랑' ),
        ( 'c', '운동' ),
        ( 'd', '취미' ),
        ( 'e', '학습' ),
        ( 'f', '전자기기' ),
        ( 'g', '어플리케이션' ),
        ( 'h', '기타' ),
    )

    section_title = models.CharField(max_length=256)

    # popular_board = ArrayField(models.CharField(max_length=200), blank=True) # post.all을 계산해서 top9을 데려와야 함. 
    # all_board = ArrayField(models.CharField(max_length=200), blank=True)# 실시간으로 post.all 받아와야 함.  


    def __str__(self):
        return self.section_title


'''

$ python manage.py shell
>>> from mainPages.models import MainPage_section
>>> MainPage_section.objects.all()
<QuerySet []>   # QuerySet은 데이터들을 담고 있는데 아직 아무것도 없는 것을 확인할 수 있습니다


MainPage_section.objects.create(section_title='금융')


>>> MainPage_section.objects.create(title='title1', content='hello1')
>>> MainPage_section.objects.get(id=1)
<Post: title1> # Post model의 __str__ 함수에 설정한 값이 출력됩니다.

>>> Post.objects.all()
<QuerySet [<Post: title1>]>
>>> exit()



'''


## 해야할 일 
## main page html 수정
## 각 섹션 링크 연결 

