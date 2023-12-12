
'''
* 리스트의 탐색과 정렬

1. index(): 리스트에서 특정 값이 저장된 인덱스를 반환.
2. count(): 리스트 내부에 저장된 특정 요소의 개수를 반환.
3. sort(): 리스트를 오름차 정렬.
4. reverse(): 리스트 데이터를 역순으로 배치
'''

poinst = [99, 14, 87, 100, 55, 100, 99, 100, 72]

perfect = poinst.count(100)
print(f'만점자는 {perfect}명 입니다.')

print(f'87점을 획득한 학생은 {poinst.index(87) +1 }번째 입니다.')

# 내장 함수 len(), max(), min()
print(f'학생 수는 {(poinst)} 명 입니다.')
print(f'최고 점수는 {max(poinst)}점 입니다.')
print(f'최저 점수는 {min(poinst)}점 입니다.')

# 오름 차 정렬 sort ()
print('-' * 40)
print(poinst)
poinst.sort(reverse=True) # 정렬하고 
# poinst.reverse() # 정렬이 아니라 단순 역순 배치 

print(poinst)

# 리스트 내의 요소의 단순 존재 유무를 검사하려면 in 키워드를 사용합니다.

food_menu = ['김밥','닭강정','라면','김말이']
name = input('음식명을 입력하세요: ')

if name in food_menu:
    print(f'{name} 음식이 주문되었습니다')
else :
    print(f'{name}은 없는 음식입니다.')
    