import random

class Dice :
    dice = [0, 0, 0, 0, 0]

    def roll(self) :
        for i in range(5):
            self.dice[i] = random.randint(1, 6)
        self.dice.sort()

    def keep(self, a) :
        num = list(map(int, a.split(",")))
        for i in range(len(num)):
            self.dice[num[i]-1] = random.randint(1, 6)
        self.dice.sort()

class Scoreboard :
    d = Dice()

    def __init__(self):
        self.board = {"aces": -1, "deuces": -1, "threes": -1, "fours": -1, "fives": -1, "sixes": -1, "four_of_kind": -1, "full_house": -1,
            "small_straight": -1, "large_straight": -1, "yacht": -1, "choice": -1}
        self.sum = 0
    def combination(self, str) :
        num = 0
        if str == "aces" :
            for i in range(5):
                if self.d.dice[i] == 1:
                    num += 1
        elif str == "deuces" :
            for i in range(5):
                if self.d.dice[i] == 2:
                    num += 2
        elif str == "threes" :
            for i in range(5):
                if self.d.dice[i] == 3:
                    num += 3
        elif str == "fours" :
            for i in range(5):
                if self.d.dice[i] == 4:
                    num += 4
        elif str == "fives" :
            for i in range(5):
                if self.d.dice[i] == 5:
                    num += 5
        elif str == "sixes" :
            for i in range(5):
                if self.d.dice[i] == 6:
                    num += 6
        elif str == "four_of_kind":
            tmp = [0,0,0,0,0,0]
            for i in range(5):
                tmp[self.d.dice[i]-1] += 1
            for i in range(6):
                if tmp[i] >= 4 :
                    for i in range(5):
                        num += self.d.dice[i]
        elif str == "full_house":
            tmp = [0,0,0,0,0,0]
            for i in range(5):
                tmp[self.d.dice[i]-1] += 1
            for i in range(6):
                if tmp[i] == 3 :
                    for i in range(6):
                        if tmp[i] == 2 :
                            for i in range(5):
                                num += self.d.dice[i]
                elif tmp[i] == 5:
                    for i in range(5):
                                num += self.d.dice[i]
        elif str == "small_straight" :
            tmp = [0,0,0,0,0,0]
            for i in range(5):
                tmp[self.d.dice[i]-1] += 1
            if tmp[2] >= 1 and tmp[3] >= 1:
                if tmp[0] >= 1 and tmp[1] >= 1:
                    num = 15
                elif tmp[1] >= 1 and tmp[4] >= 1:
                    num = 15
                elif tmp[4] >= 1 and tmp[5] >= 1:
                    num = 15
        elif str == "large_straight" :
            tmp = [0,0,0,0,0,0]
            for i in range(5):
                tmp[self.d.dice[i]-1] += 1
            if tmp[1] == 1 and tmp[2] == 1 and tmp[3] == 1 and tmp[4] == 1:
                if tmp[0] == 1 or tmp[5] == 1:
                    num = 30
        elif str == "yacht":
            tmp = [0,0,0,0,0,0]
            for i in range(5):
                tmp[self.d.dice[i]-1] += 1
            for i in range(6):
                if tmp[i] == 5 :
                   num = 50
        elif str == "choice" :
            for i in range(5):
                num += self.d.dice[i]
        return num
    def sumis(self) :
        self.sum += self.board["aces"]
        self.sum += self.board["deuces"]
        self.sum += self.board["threes"]
        self.sum += self.board["fours"]
        self.sum += self.board["fives"]
        self.sum += self.board["sixes"]
        if self.sum >= 63 :
            print("aces ~ sixes의 점수 합계가 63점 이상\n*** 보너스 점수 35점 추가 ***")
            self.sum += 35
        else :
            print("aces ~ sixes의 점수 합계가 63점 미만\n 보너스 점수 없음")
        self.sum += self.board["four_of_kind"]
        self.sum += self.board["full_house"]
        self.sum += self.board["small_straight"]
        self.sum += self.board["large_straight"]
        self.sum += self.board["yacht"]
        self.sum += self.board["choice"]

class Player :
    name = " "
    def __init__(self, name):
        self.name = name
        self.scoreboard = Scoreboard()
    def put(self):
        while True :
            enter = input("어떤 조합으로 점수를 기록하시겠습니까?\n입력 : ")
            if (enter in self.scoreboard.board):
                if (self.scoreboard.board[enter] == -1):
                    self.scoreboard.board[enter] += self.scoreboard.combination(enter)+1
                    print("{0}에 {1}점 등록".format(enter, self.scoreboard.combination((enter))))
                    break
                else :
                    print("해당 조합은 이미 사용하였습니다.")
                    continue
            else :
                print("그런 조합은 없습니다.")
                continue

    def turn(self, dice):
        dice.roll()
        print(dice.dice)
        for i in range(2) :
            enter = input("주사위를 다시 굴린다 = 1\n이대로 한다 = 2\n입력 : ")
            if enter == '1' :
                dice.keep(input("몇 번째 주사위를 다시 굴리겠습니까? (1~5번째 주사위 중 하나 선택, 여러 개를 동시에 입력 시 쉼표)\n입력 : "))
                print(dice.dice)
            elif enter == '2' :
                break
        print("{0}\n * -1은 빈 칸".format(self.scoreboard.board))
        self.put()

class Game:
    player = []
    dice = Dice()
    def __init__(self):
        self.start()

    def start(self):
        print("게임을 시작합니다.")
        for i in range(int(input("플레이할 플레이어 수 : "))) :
            self.registration()
        self.showPlayer()
        for i in range(12 * len(self.player)):
            print("{0}의 차례".format(self.player[i % len(self.player)].name))
            self.player[i % len(self.player)].turn(self.dice)
        print("게임이 종료되었습니다.")
        for i in range(len(self.player)) :
            self.player[i].scoreboard.sumis()
            print("{0}의 총점 : {1}".format(self.player[i].name, self.player[i].scoreboard.sum))
        self.whoWin()
        enter = input("게임을 다시 플레이 하시겠습니까? (Y/N)\n입력 : ")
        if enter == "Y" :
            self.start
        else :
            return 0

    def registration(self):
        self.player.append(Player(input("플레이어 닉네임 : ")))

    def showPlayer(self):
        for i in range(len(self.player)) :
            print(self.player[i].name)
        
    def whoWin(self) :
        max = 0
        maxIndex = 0
        for i in range(len(self.player)) :
            if self.player[i].scoreboard.sum > max :
                max = self.player[i].scoreboard.sum
                maxIndex = i
        print("승자는...\n\n총점 {0}점을 획득한 {1}!".format(max, self.player[maxIndex].name))

game = Game()