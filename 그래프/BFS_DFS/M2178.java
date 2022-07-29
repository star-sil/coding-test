/*
 * 미로탐색
 */
package 그래프.BFS_DFS;

import java.util.*;

class Pair{
    int x;
    int y;
    Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class M2178 {
    public static final int[] dx = {0,0,1,-1};
    public static final int[] dy = {1,-1,0,0};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] a = new int[n][m];
        sc.nextLine();
        for(int i = 0; i < n; i++){
            String s = sc.nextLine();
            for(int j = 0; j < m; j++){
                a[i][j] = s.charAt(j) - '1';
            }
        }
        Queue<Pair> q = new LinkedList<Pair>();
        q.add(new Pair(0,0));
        a[0][0] = 1;
        while(!q.isEmpty()){
            Pair p = q.remove();
            int x = p.x;
            int y = p.y;
            for(int i= 0; i < 4;i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx >= 0 && ny >= 0 && nx < n && ny < m ){
                    if(a[nx][ny] == 0){
                        q.add(new Pair(nx,ny));
                        a[nx][ny] = a[x][y]+1;
                    }
                }
            }
        }
        System.out.println(a[n-1][m-1]);
    }
}
