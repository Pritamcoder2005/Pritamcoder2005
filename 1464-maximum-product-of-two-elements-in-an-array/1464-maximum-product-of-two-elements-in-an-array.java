class Solution {
    public int maxProduct(int[] nums) {
        int first=0;
        int second=0;
        for(int n : nums){
            second = Math.max(second,Math.min(first,n));
            first=Math.max(first,n);

        }
        return (first-1)*(second-1);
    }
}