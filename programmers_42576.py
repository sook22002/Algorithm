from asyncio.windows_events import NULL


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]	

def solution(p, c):
    participant.sort()
    completion.sort()
    get_c = {}
    for i in range(len(participant)):
        if i < len(completion):
            if participant[i] == completion[i]:
                get_c[participant[i]] = completion[i]
            else:
                answer = participant[i]
                break
        else: 
            get_c[participant[i]] = 0
        
    for k, v in get_c.items():
        if v == 0:
            answer = k

    
    return answer

print(solution(participant, completion))
a = 0