import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from config.db import get_db_connection

def index(request):
    return render(request, 'sspApp/index.html')

def join_01(request):
    return render(request, 'sspApp/join_01.html')

def join_02(request):
    return render(request, 'sspApp/join_02.html')

@csrf_exempt
def check_business_number(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            business_number = data.get("business_number", "").strip()

            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute("SELECT id FROM companies WHERE business_number = %s;", (business_number,))
            result = cur.fetchone()

            cur.close()
            conn.close()

            if result:
                return JsonResponse({"exists": True, "message": "이미 등록된 회원입니다."})
            else:
                return JsonResponse({"exists": False, "message": "온라인 신청서 작성 화면으로 이동합니다."})

        except Exception as e:
            return JsonResponse({"exists": False, "message": str(e)}, status=500)

    return JsonResponse({"message": "잘못된 요청입니다."}, status=405)
