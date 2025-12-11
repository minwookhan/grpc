from concurrent import futures

import grpc
import calc_pb2
import calc_pb2_grpc

class Calculator(calc_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return calc_pb2.CalcResponse(result=result)

    def Subtract(self, request, context):
        result = request.a - request.b
        return calc_pb2.CalcResponse(result=result)
