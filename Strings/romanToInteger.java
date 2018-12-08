import java.util.*;

class Solution {
    public int romanToInt(String s) {
        HashMap<String, Integer> hm = new HashMap<String, Integer>();
        hm.put("I", 1);
        hm.put("V", 5);
        hm.put("X", 10);
        hm.put("L", 50);
        hm.put("C", 100);
        hm.put("D", 500);
        hm.put("M", 1000);

        int ans = 0;
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == 'I') {
                if((i < s.length() - 1) && s.charAt(i+1) == 'V') {
                    ans += 4;
                    i++;
                } else if ((i < s.length() - 1) && s.charAt(i+1) == 'X') {
                    ans += 9;
                    i++;
                } else {
                    ans += 1;
                }
            } else if (s.charAt(i) == 'X') {
                if((i < s.length() - 1) && s.charAt(i+1) == 'L') {
                    ans += 40;
                    i++;
                } else if ((i < s.length() - 1) && s.charAt(i+1) == 'C') {
                    ans += 90;
                    i++;
                } else {
                    ans += 10;
                }
            } else if (s.charAt(i) == 'C') {
                if((i < s.length() - 1) && s.charAt(i+1) == 'D') {
                    ans += 400;
                    i++;
                } else if ((i < s.length() - 1) && s.charAt(i+1) == 'M') {
                    ans += 900;
                    i++;
                } else {
                    ans += 100;
                }
            } else {
                ans += hm.get(String.valueOf(s.charAt(i)));
            }
        }

        return ans;
    }
}