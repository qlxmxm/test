from datetime import datetime, timedelta


class ReservationValidator:

    # -------------------------
    # 날짜 검증
    # -------------------------
    def validate_date(self, date):

        try:
            datetime.strptime(
                date,
                "%Y-%m-%d"
            )

            return True

        except ValueError:
            print(
                "예약 날짜는 YYYY-MM-DD 형식으로 "
                "입력해야 합니다."
            )

            return False

    # -------------------------
    # 시작 시간 검증
    # -------------------------
    def validate_start_time(self, start_time):

        try:
            datetime.strptime(
                start_time,
                "%H:%M"
            )

            return True

        except ValueError:
            print(
                "시작 시간은 HH:MM 형식으로 "
                "입력해야 합니다."
            )

            return False

    # -------------------------
    # 종료 시간 검증
    # -------------------------
    def validate_end_time(
        self,
        start_time,
        end_time
    ):

        try:
            start = datetime.strptime(
                start_time,
                "%H:%M"
            )

            end = datetime.strptime(
                end_time,
                "%H:%M"
            )

        except ValueError:
            print(
                "종료 시간은 HH:MM 형식으로 "
                "입력해야 합니다."
            )

            return False

        # 종료 시간이 시작 시간보다 빠르거나 같은 경우
        if start >= end:

            print(
                "종료 시간은 시작 시간보다 "
                "늦어야 합니다."
            )

            return False

        # 최대 예약 시간 4시간
        if end - start > timedelta(hours=4):

            print(
                "한 번에 최대 4시간까지 "
                "예약할 수 있습니다."
            )

            return False

        return True

    # -------------------------
    # 예약 인원 검증
    # -------------------------
    def validate_people_count(
        self,
        people_count,
        room
    ):

        if people_count < room.min_capacity:

            print(
                f"최소 {room.min_capacity}명 이상 "
                "예약해야 합니다."
            )

            return False

        if people_count > room.max_capacity:

            print(
                f"최대 {room.max_capacity}명까지 "
                "예약할 수 있습니다."
            )

            return False

        return True

    # -------------------------
    # 사용자 예약 개수 검증
    # -------------------------
    def validate_reservation_count(
        self,
        user_id,
        reservation_list
    ):

        reservation_count = 0

        for reservation in reservation_list:

            # 취소된 예약은 제외
            if reservation.status == "CANCELED":
                continue

            # 해당 사용자의 예약인지 확인
            if reservation.user_id == user_id:
                reservation_count += 1

        if reservation_count >= 3:

            print(
                "사용자는 최대 3개의 예약까지만 "
                "할 수 있습니다."
            )

            return False

        return True

    # -------------------------
    # 예약 중복 확인
    # -------------------------
    def find_overlap(
        self,
        reservation,
        reservation_list
    ):

        for existing_reservation in reservation_list:

            # 취소된 예약은 제외
            if existing_reservation.status == "CANCELED":
                continue

            # 다른 회의실이면 제외
            if (
                existing_reservation.room_id
                != reservation.room_id
            ):
                continue

            # 다른 날짜면 제외
            if (
                existing_reservation.date
                != reservation.date
            ):
                continue

            # 시간 중복 확인
            if (
                reservation.start_time
                < existing_reservation.end_time
                and
                reservation.end_time
                > existing_reservation.start_time
            ):
                return existing_reservation

        return None

    # -------------------------
    # 회의 주제 검증
    # -------------------------
    def validate_topic(self, topic):

        if not topic.strip():

            print(
                "회의 주제를 입력해주세요."
            )

            return False

        return True

    # -------------------------
    # 참석자 검증
    # -------------------------
    def validate_participants(
        self,
        participants
    ):

        if not participants.strip():

            print(
                "참석자를 입력해주세요."
            )

            return False

        return True

    # -------------------------
    # 비공개 여부 검증
    # -------------------------
    def validate_private(
        self,
        private_input
    ):

        if private_input.upper() not in ["Y", "N"]:

            print(
                "Y 또는 N으로 입력해주세요."
            )

            return False

        return True