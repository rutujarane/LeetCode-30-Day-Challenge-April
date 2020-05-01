/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
public:
    int i = 0;
    TreeNode *bstFromPreorder(vector<int> &preorder, int parentVal = INT_MAX)
    {
        //Start
        if (i == preorder.size() || preorder[i] > parentVal){
            return NULL;
        }
        
        int currentVal = preorder[i++];
        
        TreeNode *t = new TreeNode(currentVal);
        t->left = bstFromPreorder(preorder, currentVal);
        t->right = bstFromPreorder(preorder, parentVal);
        
        return t;
    }
};