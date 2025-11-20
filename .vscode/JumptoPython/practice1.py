#홍길동의 평균 점수 구하기
hong_scores = {"국어": 80, "영어": 75, "수학": 55}
total = sum(hong_scores.values())
average = total / len(hong_scores)
print("홍길동의 평균 점수:", average)