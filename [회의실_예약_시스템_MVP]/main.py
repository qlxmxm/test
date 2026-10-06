from User import UserManager
from Room import RoomManager
from Reservation import ReservationCreator
from ReservationManager import ReservationManager


user_manager = UserManager()
room_manager = RoomManager()
reservation_manager = ReservationManager()

reservation_creator = ReservationCreator(
    reservation_manager.reservation_list
)


while True:
    print("\n==============================")
    print("      회의실 예약 시스템")
    print("==============================")
    print("1. 로그인")
    print("2. 회원가입")
    print("3. 종료")

    choice = input("메뉴 선택 : ")

    # 로그인
    if choice == "1":
        user = user_manager.login()

        if user is not None:
            print(f"{user.user_name}님 환영합니다.")

            while True:
                print("\n==============================")
                print("         사용자 메뉴")
                print("==============================")
                print("1. 회의실 찾기")
                print("2. 회의실 예약")
                print("3. 내 예약 조회")
                print("4. 예약 변경")
                print("5. 예약 취소")
                print("6. 로그아웃")

                user_choice = input("메뉴 선택 : ")

                if user_choice == "1":
                    room_manager.find_rooms(
                        reservation_manager.reservation_list
                    )

                elif user_choice == "2":
                    reservation_creator.make_reservation(
                        user,
                        room_manager
                    )

                elif user_choice == "3":
                    reservation_manager.show_my_reservations(user, room_manager)

                elif user_choice == "4":
                    reservation_manager.update_reservation(user, room_manager)

                elif user_choice == "5":
                    reservation_manager.cancel_reservation(user)

                elif user_choice == "6":
                    print("로그아웃합니다.")
                    break

                else:
                    print("잘못된 메뉴입니다.")

    # 회원가입
    elif choice == "2":
        user_manager.register()

    # 종료
    elif choice == "3":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다.")