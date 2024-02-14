def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        st = ''.join([x for x in st if x in skill])
        if skill.startswith(st):
            answer += 1
    return answer
