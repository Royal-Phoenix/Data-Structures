#include <stdio.h>
#include <stdlib.h>
struct Node {
	int data;
  	struct Node *next, *head;
};
void insertNode(struct Node *temp, int data) {
	struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = data;
	if (temp == NULL) {
		struct Node *temp = newNode;
		newNode->next = NULL;
		return;
	}
	else {
  		while (temp->next != NULL) {
    		temp = temp->next;
  		}
  		temp->next = newNode;
  	}
}
void printList(struct Node *temp) {
	if (temp == NULL) {
		printf("List Empty");
		return;
	}
	else {
  		while (temp != NULL) {
    		printf("%d ", temp->data);
    		temp = temp->next;
  		}
  	}
}
void deleteNode(struct Node *temp, int nodeOffset) {
	struct Node *prev;
	int i;
	prev = temp;
	temp = temp->next;
	for (i=1; i<nodeOffset; i++) {
		prev = prev->next;
		temp = temp->next;
	}
	prev->next = temp->next;
}
int main() {
  	struct Node *obj = NULL;
  	int n, val, i;
  	printf("Enter the Number of Elements : ");
  	scanf("%d",&n);
  	for (i=0; i<n; i++){
    	printf("Enter the Element : ");
    	scanf("%d",&val);
    	insertNode(obj, val);
	}
    printf("Elements of the list are : ");
    printList(NULL);
    printf("\n");
    printf("Enter the index of element to delete : ");
    scanf("%d",&val);
    deleteNode(obj, val);
    printf("Elements of the list are : ");
    printList(obj);
    printf("\n");
    return 0;
    /*
  struct Node *one = NULL;
  struct Node *two = NULL;
  struct Node *three = NULL;

  // Allocate memory
  one = malloc(sizeof(struct Node));
  two = malloc(sizeof(struct Node));
  three = malloc(sizeof(struct Node));

  // Assign value values
  one->data = 1;
  two->data = 2;
  three->data = 3;

  // Connect nodes
  one->next = two;
  two->next = three;
  three->next = NULL;

  // printing node-value
  head = one;
  printList(head);*/
}
