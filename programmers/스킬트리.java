class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        for (String st: skill_trees) {
            String tmp = "";
            for (char x: st.toCharArray()) {
                if (skill.indexOf(x) != -1) {
                    tmp += x;
                }
            }
            if (skill.substring(0, tmp.length()).equals(tmp)) {
                answer++;
            }
        }
        return answer;
    }
}
