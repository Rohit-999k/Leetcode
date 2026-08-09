/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    if(head == NULL || head->next == NULL){
        return head;
    }

    int arr[10000];
    int j =-1;
    struct ListNode* iterator = head;
    for( ; iterator != NULL ; ){
        j++;
        arr[j] = iterator->val;
        iterator=iterator->next; 
    }

    iterator = head;
    for( ; iterator != NULL ; ){
         iterator->val = arr[j] ;
        iterator=iterator->next;
        j--; 
    }

    return head;


}