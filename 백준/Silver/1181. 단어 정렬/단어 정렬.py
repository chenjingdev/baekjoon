n = int(input())  # 단어의 개수 N을 입력받음
words = set()  # 중복을 제거하기 위해 set 사용

for _ in range(n):
    word = input().strip()  # 단어 입력받기
    words.add(word)  # set에 단어 추가

# 조건에 맞게 정렬하기
# 첫 번째 조건: 길이가 짧은 것부터, 두 번째 조건: 사전 순으로
sorted_words = sorted(words, key=lambda x: (len(x), x))

# 정렬된 단어 출력
for word in sorted_words:
    print(word)
