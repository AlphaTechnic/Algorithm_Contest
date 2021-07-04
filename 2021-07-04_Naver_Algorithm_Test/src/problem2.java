import java.util.*;

public class problem2 {
    public static String[] solution(String s){
        String[] tmp = new String[10];

        int i = 0;
        int odd_flag = 0;

        int l = 0;
        int r = s.length() - 1;
        while (true){
            if (s.length() == 0){
                break;
            }
            if(l > r){
                odd_flag = 1;
                break;
            }

            if(s.charAt(l) == s.charAt(r)){
                if(s.substring(0, l + 1).compareTo(s.substring(s.length() - l - 1, s.length())) == 0){
                    tmp[i++] = s.substring(0, l + 1);
                    if (l + 1 <= s.length() - l - 1){
                        s = s.substring(l + 1, s.length() - l - 1);

                        l = 0;
                        r = s.length() - 1;
                        continue;
                    }
                }
            }
            l++;
        }

        if (odd_flag == 1){
            int j;
            for (j = 0; tmp[j] != null; j++);
            for (int k = j - 2; k >= 0; k--){
                tmp[i++] = tmp[k];
            }
        }
        else{
            int j;
            for (j = 0; tmp[j] != null; j++);
            for (int k = j - 1; k >= 0; k--){
                tmp[i++] = tmp[k];
            }
        }

        String answer[] = new String[i];
        for (int a = 0; a < answer.length; a++){
            answer[a] = tmp[a];
        }

        return answer;
    }

    public static void main(String[] args) {
        String s = "abcxyasdfasdfxyabc";
        System.out.println(Arrays.toString(solution(s)));
    }
}