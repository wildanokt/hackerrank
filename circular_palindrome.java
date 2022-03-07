import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/*
 9 test case = success
 15 test case = timeout
 1 test case = runtime error
*/

class Result {

    /*
     * Complete the 'circularPalindromes' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts STRING s as parameter.
     */
    
    private static boolean isPalindrome(String word){
        int midpoint = word.length()/2;
        int start = 0;
        int end = word.length()-1;
        while(start<midpoint){
            if (word.charAt(start)!= word.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
    
    private static String rotateString(String word){
        String result = "";
        result += word.substring(1,word.length());
        result += word.charAt(0);
        return result;
    }
    
    public static List<Integer> circularPalindromes(String s) {
    // Write your code here
        ArrayList<Integer> result = new ArrayList<>();
        String word = s;
        TreeSet<Integer> temp_result;
        for (int i = 0; i < s.length(); i++) {
            System.out.println("Last word : "+word);
            if (i>0) {
                // rotasi huruf pertama menjadi huruf terakhir
                word = rotateString(word);    
                System.out.println("New word : "+word);
            }
            // set untuk menyimpan panjang kata palindrome dari 1 perulangan
            temp_result = new TreeSet<>();
            int start = 0;
            int end = s.length()-1;
            /*
                perulangan untuk memeriksa apakah huruf pertama dan terakhir sama.
                loop 1 :
                aaaaaabbbbbbaaaaa
                ^               ^
                loop 2 : 
                aaaaaabbbbbbaaaaa
                ^              ^
		loop 3 : 
                aaaaaabbbbbbaaaaa
                ^             ^
                loop terakhir :
                aaaaaabbbbbbaaaaa
                              ^ ^
            */  
            while(start<end-1){
                int count=word.length()-1;
                while(count>start){
                    if (word.charAt(start)==word.charAt(count)) {
                        String temp = word.substring(start,count+1);
                        /* 
                            jika panjang string yang kemungkinan palindrome 
                            lebih besar dari panjang string terpanjang di treeset
                            maka akan diproses deteksi palindrome.
                            
                            jika lebih kecil akan dilewati dan perulangan berhenti.
                        */
                        if (temp_result.isEmpty()) {
                            // untuk kondisi ketika treeset masih kosong
                            if (isPalindrome(temp) && temp.length()>=3) {
                                temp_result.add(temp.length());
                                System.out.println(temp.length());
                            }
                        }else{
                            if (temp.length()>temp_result.last()) {
                                if (isPalindrome(temp) && temp.length()>=3) {
                                    temp_result.add(temp.length());
                                    System.out.println(temp.length());
                                }
                            }else{
                                break;
                            }
                        }
                    }
                    count--;
                }
                start++;
            }
            result.add(temp_result.last());
        }
        System.out.println(result);
        return result;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        String s = bufferedReader.readLine();

        List<Integer> result = Result.circularPalindromes(s);

        for (int i = 0; i < result.size(); i++) {
            bufferedWriter.write(String.valueOf(result.get(i)));

            if (i != result.size() - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
