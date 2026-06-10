class Solution {
public:
    bool isPalindrome(string s) {
        string cleaned;
        for (char x : s) {
            if(isalnum(x)) {
                cleaned+=tolower(x);
            }
        }

        for (int i = 0; i < (int)cleaned.length()/2; i++) {
            if (cleaned[i] != cleaned[cleaned.length()-1-i]) {
                return false;
                break;
            }
        }

        return true;
    }
};
