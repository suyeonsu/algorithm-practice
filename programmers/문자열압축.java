import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = Integer.MAX_VALUE;
        for (int k=1; k<=s.length(); k++) {
            List<String> l = new ArrayList<>();
            for (int i=0; i<s.length()-k+1; i+=k) {
                l.add(s.substring(i, i+k));
            }
            if (s.length()%k >= 1) {
                l.add(s.substring(s.length()-s.length()%k, s.length()));
            }
            
            String cur = l.get(0);
            int cnt = 1;
            StringBuilder sb = new StringBuilder();
            for (int i=1; i<l.size(); i++) {
                if (l.get(i).equals(cur)) {
                    cnt++;
                } else {
                    if (cnt > 1) {
                        sb.append(String.valueOf(cnt));
                    }
                    sb.append(cur);
                    cur = l.get(i);
                    cnt = 1;
                }
            }
            sb.append(cnt > 1 ? String.valueOf(cnt)+cur : cur);
            answer = Math.min(answer, sb.toString().length());
        }
        return answer;
    }
}
