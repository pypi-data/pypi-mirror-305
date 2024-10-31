import random
import datetime

# 수업관리 (시간표조회)
def info(n):
    school = {
        '월요일': ['민정익 : 인공지능 기초수학', '스캇 : 글로벌 잉글리시'],
        '화요일': ['송주환 : 영상이해', '채플', '이근호 : 인공지능 기초와활용'],
        '수요일': ['김영수 : 소프트웨어적사고', '스캇 : 글로벌 잉글리시', '민정익 : 인공지능기초수학'],
        '목요일': ['송주환 : 영상이해', '이근호 : 인공지능기초와활용'],
        '금요일': ['김영수 : 소프트웨어적사고']}
    
    return school[n]


# 학생관리 (출석)
def attendance(): 
    rand = random.sample(list(range(0, 10)), 6)
    code = ''.join(map(str, rand))

    print('코드 :', code)
    put = input('출석코드를 입력해주세요')

    if put == code:
        return '출석체크가 완료되었습니다', True

    elif put != code:
        return '입력이 잘못되었습니다', False
    

# 학생관리 (과제 남은시간)
def time_left(name, year, month, day):
    now = datetime.datetime.now()
    dt = datetime.datetime(year, month, day)

    left = now - dt
    return f"{name}의 남은기간 : {left}"


# 학생관리 (과제 남은 시간 우선순위)
def time_sort(times, back = False):
    times =sorted( times, key = lambda x : (x[1], x[2], x[3]))

    if back:
        times.reverse()
    
    return times


# 팀플 역할고정
def team_build(n):
    
    uk = ['팀장', 'ppt', '자료조사', '코딩', '발표', '일정관리','테스터']
    
    while True:
        random.shuffle(uk)
        mem = uk[:len(n)]

        if '팀장' in mem :
            break

    fix = [f"{i} : {j}" for i,j in zip(n,mem)]

    return fix


# 성적관리 (평균)
def mean(s):
    meann = sum(s)/len(s)
    return f"성적평균 : {meann:.02f}", meann


# 성적관리 (최고점, 최저점, 평균)
def thrm():
    print('성적을 입력해주세요.')
    print('예시) 국어 75 수학 80 ...')

    grade = input().split()
    
    subject = [i for i in grade if i.isalpha()]
    score = [i for i in grade if i.isdigit()]

    if len(subject) != len(score):
        raise Exception('입력이 잘못되 었습니다.')
    
    high = None
    low = None

    for sub, sc in zip(subject, score):
        if (high is None) or (high[1] < sc):
            high = (sub, sc)
        
        if (low is None) or (sc < low[1]): 
            low = (sub, sc)

    score = list(map(int, score))
    meann = round(sum(score)/len(score), 2)

    return high, low, meann