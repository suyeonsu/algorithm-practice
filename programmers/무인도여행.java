import java.util.*;

class Solution {
    int[] dx = {-1, 0, 1, 0};
    int[] dy = {0, -1, 0, 1};
    int n, m;
    int[][] visited;

    static class Point {
        int x;
        int y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public int[] solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();
        n = maps.length;
        m = maps[0].length();
        visited = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maps[i].charAt(j) != 'X' && visited[i][j] == 0) {
                    Queue<Point> dq = new LinkedList<>();
                    int sum = maps[i].charAt(j) - '0';

                    dq.offer(new Point(i, j));
                    visited[i][j] = 1;
                    while (!dq.isEmpty()) {
                        Point cur = dq.poll();
                        for (int k = 0; k < 4; k++) {
                            int nx = cur.x + dx[k];
                            int ny = cur.y + dy[k];
                            if (0 <= nx && nx < n && 0 <= ny && ny < m && visited[nx][ny] == 0 && maps[nx].charAt(ny) != 'X') {
                                visited[nx][ny] = 1;
                                sum += maps[nx].charAt(ny) - '0';
                                dq.offer(new Point(nx, ny));
                            }
                        }
                    }
                    answer.add(sum);
                }
            }
        }
        return !answer.isEmpty() ? answer.stream().mapToInt(Integer::intValue).sorted().toArray() : new int[] {-1};
    }
}
