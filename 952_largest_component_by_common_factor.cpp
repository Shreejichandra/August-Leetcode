/*
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.
*/

int Find(int i,int P[])
{
    if(P[i]==-1)
    {return i;}
   return Find(P[i],P); 
}
void Union(int x,int y,int P[])
{
    int a=Find(x,P);
    int b=Find(y,P);
    if(a!=b)
    {
        P[b]=a;
    }
}
class Solution {
public:
    int largestComponentSize(vector<int>& A)
    {
        int mx=0;
        for(int i:A)
        {mx=max(mx,i);}
        int P[mx+1];
        memset(P,-1,sizeof(P));
        for(int i:A)
        {
          for(int j=2;j<=sqrt(i);j++)
          {
              if(i%j==0)
              {
                  Union(j,i,P);
                  Union(i,i/j,P);
              }
          }
        }
       map<int,int> M;
       int ans=0; 
       for(int i:A) 
       {
           int r=Find(i,P);
           M[r]++;
           ans=max(ans,M[r]);
       }
      return ans;  
    }
};
