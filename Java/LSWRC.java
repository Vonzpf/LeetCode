package LeetCode.Java;

/**
 * Created by Vonzpf on 17/3/21.
 */
public class LSWRC {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 1;
        if(s.length() == 0){
            maxLength = 0;
        }
        if(s.length() == 1){
            maxLength = 1;
        }
        if(s.length() > 1){
            String subString = String.valueOf(s.charAt(0));
            for (int i = 1; i < s.length(); i++){
                int j = isRepeating(subString, s.charAt(i));
                if(j != -1){
                    subString = s.substring(j + 1);
                    break;
                }
                else {
                    subString = subString.concat(String.valueOf(s.charAt(i)));
                    maxLength = subString.length();
                }
            }
            if(subString.length() < s.length()){
                int temp = lengthOfLongestSubstring(subString);
                if(temp > maxLength){
                    maxLength = temp;
                }
            }
        }

        return maxLength;
    }
    //判断重复字符
    public int isRepeating(String s, char a){
        for (int j = 0; j < s.length(); j++){
            if(s.charAt(j) == a){
                return j;
            }
        }
        return -1;
    }
}
