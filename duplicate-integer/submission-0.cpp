#include<iostream>
#include<set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> unique_nums;
        // bool duplicate_elem = false;
        std::pair<std::set<int>::iterator, bool> ret;

        for(auto & i : nums){
            ret = unique_nums.insert(i);
            if(ret.second == false){
                return true;
            }
        }
        return false;
    }
};
