sentence = '从前有座山，'
def mountain():
    print('山里有座庙，')
class Temple:
    sentence = '庙里有个老和尚，'
    def reading(self):
        print('在讲一个长长的故事。')
for i in range(10):
    print(sentence)
    mountain()
    A = Temple()
    print(A.sentence)
    A.reading()
    print()