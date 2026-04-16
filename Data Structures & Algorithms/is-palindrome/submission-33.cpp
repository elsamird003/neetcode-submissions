class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            // 1. If the left character isn't a letter/number, skip it
            if (!isalnum(s[left])) {
                left++;
            } 
            // 2. If the right character isn't a letter/number, skip it
            else if (!isalnum(s[right])) {
                right--;
            } 
            // 3. Both are letters/numbers! Now compare them as lowercase
            else {
                if (tolower(s[left]) != tolower(s[right])) {
                    return false;
                }
                left++;
                right--;
            }
        }
        
        return true;
    }
};