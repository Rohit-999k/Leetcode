/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    int arr[100000];
    int i=0;
    if(head->next==NULL){
        return true;
    }
    while(head->next!=NULL){
        arr[i]=head->val;
        i++;
        head=head->next;
    }
    arr[i]=head->val;

    int j=0;
    while(i>j){
        if(arr[i]!=arr[j]){
            return false;
        }
        i--;
        j++;
    }
    return true;
    
}