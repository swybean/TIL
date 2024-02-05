
# 현재 시각 입력
current_time = input().split()
current_hour = int(current_time[0])
current_minute = int(current_time[1])
current_second = int(current_time[2])


# 요리에 필요한 시간 입력
cooking_time = int(input())

# 종료되는 시각 계산
end_hour = (current_hour + (((current_minute * 60 + current_second + cooking_time) // 60)) // 60) % 24
end_minute = (current_minute + (cooking_time // 60)) % 60
end_second = ((current_second + cooking_time) % 60) 
# 결과 출력
print(f'{end_hour} {end_minute} {end_second}')




