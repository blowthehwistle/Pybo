#pybo.db라는 database 파일을 루트 디렉터리에 저장 위한 코드
import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  #database 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False #이벤트 처리 옵션
