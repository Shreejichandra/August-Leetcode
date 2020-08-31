/*
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        vector <int> v;
        int l, i;
        ListNode *p;
        p = head;
        while (p != NULL) {
            v.push_back(p->val);
            p = p -> next;
        }
        
        l = v.size();
        p = head;
        int j = l - 1;
        for (i=0; i < l/2; i++) {
            p->val = v[i];
            p = p->next;
            p->val = v[j];
            p = p->next;
            j--;  
        }
        if (l%2 == 1) {
            p->val = v[i];
            p = p->next;
        }
        p = NULL;   
           
    }
};
