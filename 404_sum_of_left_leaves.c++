// 
//Find the sum of all left leaves in a given binary tree.

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

int leaves(TreeNode* root, int &sum) {
    if (root == NULL)
        return 0;
    if (root->left != NULL && root->left->left == NULL && root->left->right == NULL)
        sum += root->left->val;
    leaves(root->left, sum);
    leaves(root->right, sum);
    return sum;
}
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
       int sum = 0 ;
       leaves(root, sum);
       return sum;
    }
};
