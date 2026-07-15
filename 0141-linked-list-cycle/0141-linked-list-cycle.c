/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if (head==NULL || head->next==NULL){
        return false;
    }
    while(head->next != NULL){
        head->val = -999;
        head = head->next;
        if(head->val == -999 && head->next->val == -999){
            return true;
        }
    }
    return false;
}