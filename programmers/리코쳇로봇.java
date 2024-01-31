import java.util.*;

class Solution {
    int[] dx = {0, -1, 0, 1};
    int[] dy = {-1, 0, 1, 0};
    int n, m;
    int[][] cnt;
    int rx, ry, gx, gy;
    
    public int solution(String[] board) {
        n = board.length;
        m = board[0].length();
        cnt = new int[n][m];
        for (int[] c: cnt) {
            Arrays.fill(c, Integer.MAX_VALUE);
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (board[i].charAt(j) == 'R') {
                    rx = i;
                    ry = j;
                    break;
                } else if (board[i].charAt(j) == 'G') {
                    gx = i;
                    gy = j;
                    break;
                }
            }
        }

        Queue<List<Integer>> dq = new LinkedList<>();
        dq.offer(Arrays.asList(rx, ry, 0));
        cnt[rx][ry] = 0;
        while (!dq.isEmpty()) {
            List<Integer> cur = dq.poll();
            int x = cur.get(0);
            int y = cur.get(1);
            int c = cur.get(2);
            if (x == gx && y == gy) {
                cnt[x][y] = Math.min(cnt[x][y], c);
                break;
            }
            for (int i=0; i<4; i++) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                while (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx].charAt(ny) != 'D') {
                    nx += dx[i];
                    ny += dy[i];
                }
                nx -= dx[i];
                ny -= dy[i];
                if (cnt[nx][ny] > c+1) {
                    cnt[nx][ny] = c+1;
                    dq.offer(Arrays.asList(nx, ny, c+1));
                }
            }
        }
        return cnt[gx][gy] != Integer.MAX_VALUE ? cnt[gx][gy] : -1;
    }
}
