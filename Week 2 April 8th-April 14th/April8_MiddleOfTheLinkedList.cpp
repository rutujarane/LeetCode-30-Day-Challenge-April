/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* x = head;
        int len = 1;
        int mid = 0;
        while(x->next!=NULL){
            x = x->next;
            len++;
        }
        mid = len/2 + 1;
        len = 1;
        x = head;
        while(len!=mid){
            x = x->next;
            len++;
        }
        return x;
    }
};