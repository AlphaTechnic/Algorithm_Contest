import java.util.Arrays;
import java.util.Collections;

public class problem1 {
    public static int solution(int[] prices, int[] discounts){
        Integer[] prices2 = new Integer[prices.length];
        Integer[] discounts2 = new Integer[discounts.length];

        for (int i = 0; i < prices.length; i++){
            prices2[i] = prices[i];
        }
        for (int i = 0; i < discounts.length; i++){
            discounts2[i] = discounts[i];
        }

        Arrays.sort(prices2, Collections.reverseOrder());
        Arrays.sort(discounts2, Collections.reverseOrder());

        double sum = 0;
        for (int i =0; i < prices2.length; i++){
            if (i < discounts2.length){
                sum += ((double)(100 - discounts2[i]) / 100) * prices2[i];
            }
            else{
                sum += prices2[i];
            }
        }

        return (int)sum;
    }

    public static void main(String[] args){
        int[] prices = {13000, 88000, 10000};
        int[] discounts = {30, 20};

        System.out.println(solution(prices, discounts));

    }
}
