class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int,int> num_counter;
         for (int num: nums){
            num_counter[num]++;
         }
            

            vector<pair<int,int>> arr;
            for(const auto& p: num_counter){
                arr.push_back({p.second,p.first});
            }
            sort(arr.rbegin(),arr.rend());

            vector<int> res;
            for(int i = 0; i < k; ++i){
                res.push_back(arr[i].second);
            }

            return res;


         }

    
};
