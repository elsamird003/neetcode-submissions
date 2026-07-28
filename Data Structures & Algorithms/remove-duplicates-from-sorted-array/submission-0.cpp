class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
       // nums is sorted

       if (nums.empty()){
        return 0;
       }

       // We can use the two pointers approach for this.

       int indexone = 1;
       
        for (int i = 1; i < nums.size(); i++){
            if (nums[i] != nums[i- 1]){
                nums[indexone] = nums[i];
                indexone++;
            }
 
         }

         return indexone;
    }
};