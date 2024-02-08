def solution(s):
    answer = []
    for x in s.split(" "):
        if x == '':
            answer.append(' ')
        elif not x[0].isdigit():
            answer.append(x[0].upper() + x[1:].lower() + ' ')
        else:
            answer.append(x.lower() + ' ')
    return ''.join(answer)[:-1]
