/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if(head == NULL || k==0){
        return head;
    }

    struct ListNode *p = head;
    int i=1;
    while(head->next !=NULL){
        head=head->next;
        i++;
    }
    if(k==i){
        return p;
    }
    head->next = p;
    head= head->next;


    if(k>i){
        k=k%i;
    }

     while(i-k>1){
        head = head->next;
        i--;
     }

     p=head;
     head=head->next;
     p->next = NULL;
     return head;
    
}