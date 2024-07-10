import grpc
import my_service_pb2
import my_service_pb2_grpc

def run():
    with grpc.insecure_channel('grpc-server-service:50051') as channel:
        stub = my_service_pb2_grpc.MyServiceStub(channel)
        response = stub.MyFunction(my_service_pb2.MyRequest(message='World'))
        print("Client received: " + response.reply)

if __name__ == '__main__':
    run()
