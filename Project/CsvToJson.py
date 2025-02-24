import csv
import json
import re

# 날짜 포맷을 "2025년 3월 11일(화) 오후 6시"에서 "2025-03-11"로 변환하는 함수
def format_date(date_string):
    match = re.match(r'(\d{4})년 (\d{1,2})월 (\d{1,2})일', date_string)
    if match:
        year = match.group(1)
        month = str(int(match.group(2))).zfill(2)  # 두 자릿수로 월 만들기
        day = str(int(match.group(3))).zfill(2)    # 두 자릿수로 일 만들기
        return f"{year}-{month}-{day}"  # "YYYY-MM-DD" 형식
    return None

def format_apply(date_string):
    match = re.match(r'(\d{4}).(\d{1,2}).(\d{1,2})', date_string)
    if match:
        year = match.group(1)
        month = str(int(match.group(2))).zfill(2)  # 두 자릿수로 월 만들기
        day = str(int(match.group(3))).zfill(2)    # 두 자릿수로 일 만들기
        return f"{year}-{month}-{day}"  # "YYYY-MM-DD" 형식
    return None

# CSV를 JSON으로 변환하는 함수
def csvTojson():
    # CSV 파일 경로
    csv_file = 'mycode\Project\concert.csv'
    # 출력할 JSON 파일 경로
    json_file = 'mycode\Project\\templates\concert.json'

    # CSV 파일 읽기
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]

    # 날짜 변환
    for concert in data:
        if '예매날짜' in concert:
            concert['예매날짜'] = format_date(concert['예매날짜'])
        if '등록일' in concert:
            concert['등록일'] = format_apply(concert['등록일'])

    # JSON 파일로 저장
    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"JSON 파일이 생성되었습니다: {json_file}")

csvTojson()