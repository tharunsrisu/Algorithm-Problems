class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> numMap;  // Use unordered_map for efficient lookups
        int curr_key=0;
        int remaining=0;
        int check_map=0;
        for(int i=0 ; i <nums.size() ; i++){
            curr_key=nums[i];
            remaining= target-curr_key;
            if(numMap.find(remaining)!=numMap.end()){
                return {numMap[remaining], i};
            }
            numMap[curr_key]=i;
            
        }

        return {} ;
