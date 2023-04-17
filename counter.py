
class Counter:


    def __init__(self):
        self.real_score = Real_Score()



    def getrealscore(self):
        return self.real_score


    def addten(self):
        self.real_score += 10
        return self.real_score

    def addthreehundred(self):
        self.real_score += 300
        return self.real_score

