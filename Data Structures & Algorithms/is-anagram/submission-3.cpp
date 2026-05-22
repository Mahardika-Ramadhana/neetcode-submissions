class Solution {
public:
    bool isAnagram(string s, string t) {

        vector<char> arr;

        for (int i = 0; i < s.length(); i++) {
            arr.push_back(s[i]);
        }

        for (int i = 0; i < t.length(); i++) {

            bool found = false;

            for (int j = 0; j < arr.size(); j++) {

                if (t[i] == arr[j]) {

                    arr.erase(arr.begin() + j);

                    found = true;
                    break;
                }
            }

            if (!found) {
                return false;
            }
        }

        if (!arr.empty()) {
            return false;
        }

        return true;
    }
};
