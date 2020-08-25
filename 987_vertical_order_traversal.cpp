/*
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
*/


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
bool comp(pair<int,int>&A,pair<int,int> &B)
{
  return ( (A.first>B.first) || (A.first==B.first && A.second<B.second));
}
void dfs(TreeNode *root,int x,int y,map <int,vector<pair<int,int>>> &M)
{
  if(!root){return;}
  M[x].push_back({y,root->val});
  dfs(root->left,x-1,y-1,M);
  dfs(root->right,x+1,y-1,M);
}
class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root)
    {
        vector<vector<int>>vv;
      map <int,vector<pair<int,int>>> M;
     dfs(root,0,0,M);
   for(auto i:M)
  {
    sort(i.second.begin(),i.second.end(),comp);
    vector<int>V;
    for(int j=0;j<i.second.size();j++)
    {
      V.push_back(i.second[j].second);
    }
    vv.push_back(V);
  }
  return vv;
    }
};
