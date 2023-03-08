/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        sort(nums.begin(), nums.end());
        int i=0;
        int j=nums.size()-1;
        while(i<j){
            if(nums[i]+nums[j]==target){
                ret.push_back(i);
                ret.push_back(j);
                break;
            }
            if(nums[i]+nums[j]<target)
                i+=1;
            else
                j-=1;
        }
        return ret;
    }
};
// @lc code=end

