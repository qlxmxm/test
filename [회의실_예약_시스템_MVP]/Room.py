class Room:

    def __init__(self, room_id, room_name, min_capacity, max_capacity):
        self.room_id = room_id
        self.room_name = room_name
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity


class RoomManager:

    def __init__(self):
        self.room_list = []

        # 2인실 2개
        self.room_list.append(Room(1, "2인실 A", 1, 2))
        self.room_list.append(Room(2, "2인실 B", 1, 2))

        # 4인실 4개
        self.room_list.append(Room(3, "4인실 A", 1, 4))
        self.room_list.append(Room(4, "4인실 B", 1, 4))
        self.room_list.append(Room(5, "4인실 C", 1, 4))
        self.room_list.append(Room(6, "4인실 D", 1, 4))

        # 8인실 2개
        self.room_list.append(Room(7, "8인실 A", 1, 8))
        self.room_list.append(Room(8, "8인실 B", 1, 8))

        # 컴퍼런스실 1개
        self.room_list.append(Room(9, "컨퍼런스실", 10, 99))

    def show_room_list(self):
        print("\n===== 회의실 목록 =====")

        for room in self.room_list:

            if room.room_name == "컴퍼런스실":
                capacity_text = f"최소 {room.min_capacity}명"

            else:
                capacity_text = f"최대 {room.max_capacity}명"

            print(
                f"번호: {room.room_id} | "
                f"이름: {room.room_name} | "
                f"수용 인원: {capacity_text}"
            )

    def find_rooms(self, reservation_list):

        print("\n===== 현재 예약된 회의실 =====")

        for room in self.room_list:

            print(f"\n[{room.room_name}]")

            found = False

            for reservation in reservation_list:

                if reservation.status == "CANCELED":
                    continue

                if reservation.room_id != room.room_id:
                    continue

                found = True

                print(
                    f"{reservation.date[5:].replace('-', '/')} "
                    f"{reservation.start_time} ~ {reservation.end_time}"
                )

                if reservation.is_private:
                    print("회의 주제 : 비공개 회의")
                else:
                    print(f"회의 주제 : {reservation.topic}")

            if not found:
                print("현재 예약 없음")