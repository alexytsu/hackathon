from rest_framework.views import APIView
from rest_framework.response import Response
from restAPI.models import Test


class TestAPI(APIView):
    def get(self, request):
        idVal = int(request.data.get('id'))
        try:
            testObj = Test.objects.get(id=idVal)
            print(testObj.input)
            resp_dict =  {
                'status':'success',
                'message':'retrieved object',
                'data':{'id':testObj.id, 'input':testObj.input}
            }
            resp = Response()
            resp.status_code = 201
            resp.data = resp_dict
        except Exception as e:
            print(e)
            resp_dict =  {
                'status':'fail',
                'message': 'something went wrong',
                'data':{'id':testObj.id, 'input':testObj.input}
            }
            resp = Response()
            resp.status_code = 404
            resp.data = resp_dict
        return resp
        
    
    def post(self,request):
        print(request.data)
        inputVal = request.data.get('input')
        print("result",inputVal)
        try:
            newTest = Test(input=inputVal)
            newTest.input = inputVal
            newTest.save()
            resp_dict =  {
                'status':'success',
                'message':'Added test input successfully',
                'data':{'input':inputVal}
            }
            resp = Response()
            resp.status_code = 201
            resp.data = resp_dict
        except Exception as e:
            print(e)
            resp_dict =  {
                'status':'fail',
                'message':'Something went wrong',
                'data':{}
            }
            resp = Response()
            resp.status_code = 404
            resp.data = resp_dict
        
        return resp