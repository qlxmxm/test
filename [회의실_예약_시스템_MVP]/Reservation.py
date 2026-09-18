import json
import msvcrt

from ReservationValidator import ReservationValidator


class ReservationCancel(Exception):
    pass


class Reservation:

    def __init__(
        self,
        reservation_id,
        user_id,
        room_id,
        date,
        start_time,
        end_time,
        people_count,
        topic,
        participants,
        is_private,
        status
    ):
        self.reservation_id = reservation_id
        self.user_id = user_id
        self.room_id = room_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.people_count = people_count
        self.topic = topic
        self.participants = participants
        self.is_private = is_private
        self.status = status


class ReservationCreator:

    def __init__(self, reservation_list):
        self.reservation_list = reservation_list
        self.validator = ReservationValidator()
        self.file_path = "[회의실_예약_시스템_MVP]/reservations.json"

    # Esc 입력이 가능한 입력 함수
    def input_with_esc(self, message):

        print(message, end="", flush=True)

        input_value = ""

        while True:

            key = msvcrt.getwch()

            # Enter
            if key == "\r":
                print()
                return input_value

            # Esc
            if key == "\x1b":
                print("\n")
                raise ReservationCancel

            # Backspace
            if key == "\x08":

                if input_value:
                    input_value = input_value[:-1]
                    print("\b \b", end="", flush=True)

                continue

            # 일반 문자
            input_value += key
            print(key, end="", flush=True)

    def make_reservation(self, user, room_manager):

        try:

            print("\n===== 회의실 예약 =====")

            # 사용자 예약 개수 확인
            if not self.validator.validate_reservation_count(
                user.user_id,
                self.reservation_list
            ):
                return

            # 회의실 목록 출력
            room_manager.show_room_list()

            # 회의실 선택
            while True:

                room_input = self.input_with_esc(
                    "회의실 번호 : "
                )

                try:
                    room_id = int(room_input)

                except ValueError:
                    print("회의실 번호는 숫자로 입력해야 합니다.")
                    continue

                selected_room = None

                for room in room_manager.room_list:

                    if room.room_id == room_id:
                        selected_room = room
                        break

                if selected_room is not None:
                    break

                print("존재하지 않는 회의실입니다.")

            # 예약 정보 입력
            while True:

                # -------------------------
                # 예약 날짜
                # -------------------------
                while True:

                    date = self.input_with_esc(
                        "예약 날짜 (YYYY-MM-DD) : "
                    )

                    if self.validator.validate_date(date):
                        break

                # -------------------------
                # 시작 시간 / 종료 시간
                # -------------------------
                while True:

                    start_time = self.input_with_esc(
                        "시작 시간 (HH:MM) : "
                    )

                    if not self.validator.validate_start_time(
                        start_time
                    ):
                        continue

                    end_time = self.input_with_esc(
                        "종료 시간 (HH:MM) : "
                    )

                    if not self.validator.validate_end_time(
                        start_time,
                        end_time
                    ):
                        continue

                    break

                # -------------------------
                # 예약 인원
                # -------------------------
                while True:

                    people_input = self.input_with_esc(
                        "예약 인원 : "
                    )

                    try:
                        people_count = int(people_input)

                    except ValueError:
                        print("예약 인원은 숫자로 입력해야 합니다.")
                        continue

                    if self.validator.validate_people_count(
                        people_count,
                        selected_room
                    ):
                        break

                # -------------------------
                # 회의 주제
                # -------------------------
                while True:

                    topic = self.input_with_esc(
                        "회의 주제 : "
                    )

                    if self.validator.validate_topic(topic):
                        break

                # -------------------------
                # 참석자
                # -------------------------
                while True:

                    participants = self.input_with_esc(
                        "참석자 : "
                    )

                    if self.validator.validate_participants(
                        participants
                    ):
                        break

                # -------------------------
                # 비공개 여부
                # -------------------------
                while True:

                    private_input = self.input_with_esc(
                        "비공개 회의인가요? (Y/N) : "
                    )

                    if self.validator.validate_private(
                        private_input
                    ):
                        break

                is_private = private_input.upper() == "Y"

                # -------------------------
                # 예약 객체 생성
                # -------------------------
                reservation_id = len(
                    self.reservation_list
                ) + 1

                reservation = Reservation(
                    reservation_id,
                    user.user_id,
                    selected_room.room_id,
                    date,
                    start_time,
                    end_time,
                    people_count,
                    topic,
                    participants,
                    is_private,
                    "RESERVED"
                )

                # -------------------------
                # 예약 중복 확인
                # -------------------------
                overlap_reservation = (
                    self.validator.find_overlap(
                        reservation,
                        self.reservation_list
                    )
                )

                if overlap_reservation is not None:

                    print("\n===== 예약 시간 중복 =====")
                    print("이미 예약된 회의실입니다.")
                    print(
                        f"회의실 : "
                        f"{selected_room.room_name}"
                    )
                    print(
                        f"날짜 : "
                        f"{overlap_reservation.date}"
                    )
                    print(
                        f"시간 : "
                        f"{overlap_reservation.start_time} "
                        f"~ "
                        f"{overlap_reservation.end_time}"
                    )
                    print(
                        f"회의 주제 : "
                        f"{overlap_reservation.topic}"
                    )

                    print(
                        "\n예약 날짜부터 다시 입력해주세요.\n"
                    )

                    continue

                # -------------------------
                # 예약 완료
                # -------------------------
                self.reservation_list.append(
                    reservation
                )

                self.save_reservations()

                print("\n예약이 완료되었습니다.")
                print(
                    f"예약 번호 : "
                    f"{reservation.reservation_id}"
                )
                print(
                    f"회의실 : "
                    f"{selected_room.room_name}"
                )
                print(
                    f"일시 : "
                    f"{reservation.date} "
                    f"{reservation.start_time} "
                    f"~ "
                    f"{reservation.end_time}"
                )
                print(
                    f"예약 인원 : "
                    f"{reservation.people_count}명"
                )

                break

        except ReservationCancel:

            print("예약을 취소했습니다.")
            return
        
    def save_reservations(self):

        reservation_data_list = []

        for reservation in self.reservation_list:

            reservation_data = {
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
            }

            reservation_data_list.append(
                reservation_data
            )

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                reservation_data_list,
                file,
                ensure_ascii=False,
                indent=4
            )