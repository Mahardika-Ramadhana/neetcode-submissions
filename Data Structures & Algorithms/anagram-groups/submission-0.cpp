class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char,int>, vector<int>> hashmap;
        
        for (int i = 0; i < strs.size(); i++) {
            map<char, int> freq;
            for (char c : strs[i]) {
                freq[c]++;
            }
            hashmap[freq].push_back(i);
        }
        
        vector<vector<string>> result;
        for (auto& [freq, indices] : hashmap) {
            vector<string> group;
            for (int idx : indices) {
                group.push_back(strs[idx]);
            }
            result.push_back(group);
        }
        
        return result;
    }
};
