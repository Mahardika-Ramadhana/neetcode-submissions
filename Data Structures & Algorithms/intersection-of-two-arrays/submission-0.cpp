class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> seen;
        for (int num : nums1) {
            seen[num] = 1;
        } 

        vector<int> result;
        for (int num : nums2) {
            if (seen[num] == 1) {
                seen[num] = 0;
                result.push_back(num);
            }
        }

        return result;
    }
};