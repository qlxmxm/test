import json


class ReservationManager:

    def __init__(self):
        self.reservation_list = []
        self.file_path = "[회의실_예약_시스템_MVP]/reservations.json"

        self.load_reservations()

    def show_my_reservations(self, user, room_manager):

        print("\n===== 내 예약 조회 =====")

        my_reservations = []

        for reservation in self.reservation_list:

            if reservation.user_id == user.user_id:
                my_reservations.append(reservation)

        if not my_reservations:
            print("예약 내역이 없습니다.")
            return

        for reservation in my_reservations:

            room_name = ""

            for room in room_manager.room_list:

                if room.room_id == reservation.room_id:
                    room_name = room.room_name
                    break

            print("\n------------------------------")
            print(f"예약 번호 : {reservation.reservation_id}")
            print(f"회의실 : {room_name}")
            print(
                f"일시 : {reservation.date} "
                f"{reservation.start_time} ~ {reservation.end_time}"
            )
            print(f"예약 인원 : {reservation.people_count}명")
            print(f"회의 주제 : {reservation.topic}")
            print(f"참석자 : {reservation.participants}")

            if reservation.is_private:
                print("비공개 회의 : Y")
            else:
                print("비공개 회의 : N")

            print(f"예약 상태 : {reservation.status}")

    def update_reservation(self, user, room_manager):

        my_reservations = []

        for reservation in self.reservation_list:

            if reservation.user_id == user.user_id:
                my_reservations.append(reservation)

        if not my_reservations:
            print("예약 내역이 없습니다.")
            return

        print("\n===== 예약 변경 =====")

        for reservation in my_reservations:

            print(
                f"예약 번호 : {reservation.reservation_id} | "
                f"{reservation.date} "
                f"{reservation.start_time} ~ "
                f"{reservation.end_time}"
            )

        try:
            reservation_id = int(
                input("변경할 예약 번호 : ")
            )
        except ValueError:
            print("예약 번호는 숫자로 입력해야 합니다.")
            return

        selected_reservation = None

        for reservation in my_reservations:

            if reservation.reservation_id == reservation_id:
                selected_reservation = reservation
                break

        if selected_reservation is None:
            print("해당 예약을 찾을 수 없습니다.")
            return

        if selected_reservation.status == "CANCELED":
            print("취소된 예약은 변경할 수 없습니다.")
            return

        date = input("새 날짜 (YYYY-MM-DD) : ")
        start_time = input("새 시작 시간 (HH:MM) : ")
        end_time = input("새 종료 시간 (HH:MM) : ")

        try:
            people_count = int(
                input("새 예약 인원 : ")
            )
        except ValueError:
            print("예약 인원은 숫자로 입력해야 합니다.")
            return

        selected_room = None

        for room in room_manager.room_list:

            if room.room_id == selected_reservation.room_id:
                selected_room = room
                break

        if selected_room is None:
            print("회의실을 찾을 수 없습니다.")
            return

        # 기본 검증
        if people_count < selected_room.min_capacity:
            print(
                f"최소 {selected_room.min_capacity}명 이상 예약해야 합니다."
            )
            return

        if people_count > selected_room.max_capacity:
            print(
                f"최대 {selected_room.max_capacity}명까지 예약할 수 있습니다."
            )
            return

        if start_time >= end_time:
            print("종료 시간은 시작 시간보다 늦어야 합니다.")
            return

        # 기존 값 저장
        old_date = selected_reservation.date
        old_start_time = selected_reservation.start_time
        old_end_time = selected_reservation.end_time
        old_people_count = selected_reservation.people_count
        old_topic = selected_reservation.topic
        old_participants = selected_reservation.participants
        old_is_private = selected_reservation.is_private

        # 임시로 변경
        selected_reservation.date = date
        selected_reservation.start_time = start_time
        selected_reservation.end_time = end_time
        selected_reservation.people_count = people_count

        # 중복 검사
        for reservation in self.reservation_list:

            if reservation.status == "CANCELED":
                continue

            if reservation.reservation_id == selected_reservation.reservation_id:
                continue

            if reservation.room_id != selected_reservation.room_id:
                continue

            if reservation.date != selected_reservation.date:
                continue

            if (
                selected_reservation.start_time < reservation.end_time
                and
                selected_reservation.end_time > reservation.start_time
            ):
                print("해당 시간에 이미 예약된 회의실입니다.")

                # 원래 값으로 복구
                selected_reservation.date = old_date
                selected_reservation.start_time = old_start_time
                selected_reservation.end_time = old_end_time
                selected_reservation.people_count = old_people_count

                return

        selected_reservation.topic = input(
            "새 회의 주제 : "
        )

        selected_reservation.participants = input(
            "새 참석자(,) : "
        )

        private_input = input(
            "비공개 회의인가요? (Y/N) : "
        )

        if private_input.upper() == "Y":
            selected_reservation.is_private = True
        else:
            selected_reservation.is_private = False

        self.save_reservations()

        print("예약이 변경되었습니다.")

    def cancel_reservation(self, user):

        my_reservations = []

        for reservation in self.reservation_list:

            if reservation.user_id == user.user_id:
                my_reservations.append(reservation)

        if not my_reservations:
            print("예약 내역이 없습니다.")
            return

        print("\n===== 예약 취소 =====")

        active_reservation = False

        for reservation in my_reservations:

            if reservation.status == "CANCELED":
                continue

            active_reservation = True

            print(
                f"예약 번호 : {reservation.reservation_id} | "
                f"{reservation.date} "
                f"{reservation.start_time} ~ "
                f"{reservation.end_time}"
            )

        if not active_reservation:
            print("취소할 예약이 없습니다.")
            return

        try:
            reservation_id = int(
                input("취소할 예약 번호 : ")
            )
        except ValueError:
            print("예약 번호는 숫자로 입력해야 합니다.")
            return

        selected_reservation = None

        for reservation in my_reservations:

            if reservation.reservation_id == reservation_id:
                selected_reservation = reservation
                break

        if selected_reservation is None:
            print("해당 예약을 찾을 수 없습니다.")
            return

        if selected_reservation.status == "CANCELED":
            print("이미 취소된 예약입니다.")
            return

        confirm = input(
            "정말 취소하시겠습니까? (Y/N) : "
        )

        if confirm.upper() != "Y":
            print("예약 취소를 취소했습니다.")
            return

        selected_reservation.status = "CANCELED"

        self.save_reservations()

        print("예약이 취소되었습니다.")

    def save_reservations(self):

        data = []

        for reservation in self.reservation_list:

            data.append({
                "reservation_id": reservation.reservation_id,
                "user_id": reservation.user_id,
                "room_id": reservation.room_id,
                "date": reservation.date,
                "start_time": reservation.start_time,
                "end_time": reservation.end_time,
                "people_count": reservation.people_count,
                "topic": reservation.topic,
                "participants": reservation.participants,
                "is_private": reservation.is_private,
                "status": reservation.status
            })

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def load_reservations(self):

        try:

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            from Reservation import Reservation

            for reservation_data in data:

                reservation = Reservation(
                    reservation_data["reservation_id"],
                    reservation_data["user_id"],
                    reservation_data["room_id"],
                    reservation_data["date"],
                    reservation_data["start_time"],
                    reservation_data["end_time"],
                    reservation_data["people_count"],
                    reservation_data["topic"],
                    reservation_data["participants"],
                    reservation_data["is_private"],
                    reservation_data["status"]
                )

                self.reservation_list.append(reservation)

        except FileNotFoundError:
            pass