# 기본 이미지로 파이썬 3.9을 사용
FROM python:3.9

# 작업 디렉터리 설정
WORKDIR /app

# 의존성 파일들을 컨테이너에 복사
COPY app.py .

# 필요한 패키지 설치
RUN pip install flask

# 서버 실행
CMD ["python", "app.py"]
