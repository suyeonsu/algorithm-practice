import java.util.*;

class Solution {
    
    static Map<String, Node> info;

    static class Node {
        String parent;
        int profit;

        Node(String parent) {
            this.parent = parent;
            this.profit = 0;
        }
    }

    static void dfs(String child, int money) {
        String parent = info.get(child).parent;
        int fee = (int)(money*0.1);
        info.get(child).profit += money-fee;
        if (!parent.equals("-") && fee > 0) {
            dfs(parent, fee);
        }
    }

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int[] answer = new int[enroll.length];
        info = new HashMap<>();
        for (int i=0; i<enroll.length; i++) {
            info.put(enroll[i], new Node(referral[i]));
        }

        for (int i=0; i<seller.length; i++) {
            dfs(seller[i], amount[i]*100);
        }

        for (int i=0; i<enroll.length; i++) {
            answer[i] = info.get(enroll[i]).profit;
        }

        return answer;
    }
}
