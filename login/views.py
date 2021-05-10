from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Loginuser

class RegisterUser(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        user_pw = request.data.get("user_pw")

        user = Loginuser.objects.first(user_id=user_id).first()
        if user is not None:
            return Response(dict(msg="동일한 아이디 있습니다."))

        Loginuser.objects.create(user_id=user_id, user_pw=user_pw)

        data = dict(
            user_id=user_id,
            user_pw=user_pw
        )

        return Response(data)
