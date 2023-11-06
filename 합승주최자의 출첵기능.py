# 주최자 클래스 정의
class Organizer:
    def __init__(self, name):
        self.name = name # 합승자 이름
        self.attendees = [] # 출석한 사람들의 리스트

    def __str__(self):
        return f"{self.name} (출석인원: {len(self.attendees)})"

    def check_attendance(self, person):
        # 출석한 사람을 리스트에 추가하고 메시지 출력
        self.attendees.append(person)
        print(f"{person}님이 {self.name}의 택시합승에 출석하셨습니다.")

# 테스트를 위한 임의의 주최자 객체 생성
organizer = Organizer("A")


# 테스트를 위한 임의의 출석자 리스트 생성
attendees = ["B", "C", "D"]

# 출석자들을 반복하며 출석체크
for person in attendees:
    organizer.check_attendance(person)


"""
근데 여기서 꼭 
합승을 4명만 한다는 보장이 없는데
이거 전에 2명이상 4명ㅇㅣ하 설정해야할 듯>
"""