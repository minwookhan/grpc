import grpc
import addressbook_pb2
import addressbook_pb2_grpc

def run():
    # 서버 연결
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = addressbook_pb2_grpc.AddressBookServiceStub(channel)

        # 1. 사람 데이터 생성 (튜토리얼 방식)
        person = addressbook_pb2.Person()
        person.id = 1234
        person.name = "홍길동"
        person.email = "hong@example.com"

        # repeated 필드(phones) 추가
        phone_mobile = person.phones.add()
        phone_mobile.number = "010-1234-5678"
        phone_mobile.type = addressbook_pb2.Person.MOBILE

        phone_home = person.phones.add()
        phone_home.number = "02-111-2222"
        phone_home.type = addressbook_pb2.Person.HOME

        # 2. 서버에 AddPerson 요청 보내기
        print(f"Sending person: {person.name}")
        response = stub.AddPerson(person)
        print(f"Server Response: {response.message}")

        print("-" * 20)

        # 3. 서버에서 전체 주소록 가져오기
        print("Fetching address book from server...")
        empty = addressbook_pb2.Empty()
        returned_book = stub.GetAddressBook(empty)

        # 결과 출력
        for p in returned_book.people:
            print(f"Name: {p.name}")
            print(f"ID: {p.id}")
            for phone in p.phones:
                print(f"  - Phone: {phone.number} ({phone.type})")

if __name__ == '__main__':
    run()
