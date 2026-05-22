class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> store;

        for (int i = 0; i < nums.size(); i++) {

            bool exists = false;

            for (int j = 0; j < store.size(); j++) {
                if (nums[i] == store[j]) {
                    exists = true;
                    break;
                }
            }

            if (exists) {
                return true;
            }

            store.push_back(nums[i]);
        }

        return false;        
    }
};