import grpc
from concurrent import futures
import addressbook_pb2
import addressbook_pb2_grpc

class AddressBookServer(addressbook_pb2_grpc.AddressBookServiceServicer):
    def __init__(self):
        self.book = addressbook_pb2.AddressBook()
    def AddPerson(self, request, context):
        print(f"[Server] Adding person: {request.name}")

        new_person = self.book.people.add()
        new_person.CopyFrom(request)

        return addressbook_pb2.Response(message="Person added successfully", success=True)


    def GetAddressBook(self, request, context):
        print("[Server] Retrieving address book")
        return self.book

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    addressbook_pb2_grpc.add_AddressBookServiceServicer_to_server(AddressBookServer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
