# name = "홍길동"
# num1 = 100
# num2 = 80
# num3 = 95

# print("%s 합계 : %d" % (name,num1+num2+num3))
# print("%s 평균 : %.2f" % (name,(num1+num2+num3)/3))
# print("{} 합계 : {}".format(name, num1+num2+num3))
# print("{} 평균 : {:.2f}".format(name, (num1+num2+num3)/3))

# num1 = 12.12345
# num2 = 456.78940
# num3 = 2.252525

# print("{:.2f} , {:.2f} , {:.2f} \n".format(num1,num2,num3))


# print("\"")
# print("안녕하세요")
# print("안녕\t하세요")
# print("안녕\n하세요")


# print("(서울=연합뉴스) 장재은 기자 = 이스라엘의 친이란 무장세력 토벌에 이란이 점점 곤궁한 처지에 몰리고 있다. \n이스라엘의 과감한 군사 행동에 중동질서가 재편되는 조짐이지만 이란은 진퇴양난에 꺼내들 카드가 없어 속만 태우는 형국으로 관측된다.\n30일(현지시간) 외신을 종합하면 이스라엘과 이란 대리세력의 분쟁은 이스라엘의 압도적 승리 행진으로 요약된다.")


# print("""(서울=연합뉴스) 장재은 기자 = 이스라엘의 친이란 무장세력 토벌에 이란이 점점 곤궁한 처지에 몰리고 있다.
#       이스라엘의 과감한 군사 행동에 중동질서가 재편되는 조짐이지만 이란은 진퇴양난에 꺼내들 카드가 없어 속만 태우는 형국으로 관측된다.
      
#       30일(현지시간) 외신을 종합하면 이스라엘과 이란 대리세력의 분쟁은 이스라엘의 압도적 승리 행진으로 요약된다.
#       """)


print("""\
      (서울=연합뉴스) 장재은 기자 = 이스라엘의 친이란 무장세력 토벌에 이란이 점점 곤궁한 처지에 몰리고 있다.
      이스라엘의 과감한 군사 행동에 중동질서가 재편되는 조짐이지만 이란은 진퇴양난에 꺼내들 카드가 없어 속만 태우는 형국으로 관측된다.
      
      30일(현지시간) 외신을 종합하면 이스라엘과 이란 대리세력의 분쟁은 이스라엘의 압도적 승리 행진으로 요약된다.
      """)


num1 = 100
num2 = 80
num3 = 85
name = "홍길동"
avg = ":.2f".format((num1 + num2 +num3)/3)
avg2 = (num1 + num2 +num3)/3
print(f"{name} 평균 : {avg}")
print(f'{name} 평균 : {round(avg2, 2)}')

a = 1.314516
print(f"소수점 3자리 출력 : {a:.3f}")