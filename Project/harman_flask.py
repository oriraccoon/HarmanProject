from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# 파일 경로
json_file_path = 'static//concert.json'

@app.route("/")
def index():
    return render_template("cal.html")

# 기존 이벤트 불러오기
@app.route("/get_events")
def get_events():
    try:
        with open(json_file_path, 'r', encoding='UTF-8') as file:
            events = json.load(file)
        return jsonify(events)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

# 체크 상태 저장 → concert.json에 반영
@app.route("/save_checked_state", methods=["POST"])
def save_checked_state():
    try:
        updated_events = request.get_json()

        # 기존 데이터 불러오기
        with open(json_file_path, 'r', encoding='UTF-8') as file:
            original_data = json.load(file)

        # 이름 기준으로 checked 상태 업데이트
        for orig_event in original_data:
            for updated_event in updated_events:
                if orig_event["﻿이름"] == updated_event["name"]:  # BOM 문자 주의
                    orig_event["checked"] = updated_event["checked"]

        # 업데이트된 데이터 저장
        with open(json_file_path, 'w', encoding='UTF-8') as file:
            json.dump(original_data, file, ensure_ascii=False, indent=4)

        return jsonify({"message": "체크 상태가 저장되었습니다!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
