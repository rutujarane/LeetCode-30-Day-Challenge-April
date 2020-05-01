/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *   public:
 *     int get(int x, int y);
 *     vector<int> dimensions();
 * };
 */

class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        vector<int> dimensions;
        dimensions = binaryMatrix.dimensions();
        // cout << dimensions[0] << dimensions[1] << endl;
        int i=0;
        int j=dimensions[1]-1;
        while(i<=dimensions[0]-1 and j>=0){
            // cout << i << j << endl;
            if(binaryMatrix.get(i,j) == 0){
                i++;
            }
            else{
                j--;
            }
        }
        if(j==dimensions[1]-1)
            return -1;
        else
            return j+1;
        return -1;
    }
};