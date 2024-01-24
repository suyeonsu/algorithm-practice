class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder();
        for (char c: s.toCharArray()) {
            int pos = c;
            int cnt = 0;
            while (cnt < index) {
                pos++;
                if (pos > 'z') {
                    pos = 'a';
                }
                if (!skip.contains(String.valueOf((char)pos))) {
                    cnt++;
                }
            }
            answer.append((char)pos);
        }
        return answer.toString();
    }
}
