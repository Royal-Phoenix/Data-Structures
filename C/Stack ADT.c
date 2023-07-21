#include <stdio.h>
#include <stdlib.h>
#define MAX 100
int count = 0;
struct stack {
	int items[MAX];
  	int top;
};
typedef struct stack st;
void createEmptyStack(st *s) {
  	s->top = -1;
}
int isFull(st *s) {
  	if (s->top == MAX - 1)
    	return 1;
  	else
    	return 0;
}
int isEmpty(st *s) {
  	if (s->top == -1)
    	return 1;
  	else
    	return 0;
}
void push(st *s, int data) {
  	if (isFull(s))
    	printf("STACK FULL");
  	else {
    	s->top++;
    	s->items[s->top] = data;
  	}
}
void pop(st *s) {
  	if (isEmpty(s))
    	printf("\n STACK EMPTY \n");
  	else
    	s->top--;
  	printf("\n");
}
void printStack(st *s) {
	int i;
  	printf("  STACK\n");
  	for (i = s->top; i > -1; i--) {
  		printf("|       |\n");
    	printf("|   %d   |\n", s->items[i]);
    	printf("|_______|\n");
    }
  	printf("\n");
}
int main() {
	int i,n,val;
  	st *s = (st *)malloc(sizeof(st));
  	createEmptyStack(s);
  	printf("Enter the Number of Elements : ");
  	scanf("%d",&n);
  	for (i=0; i<n; i++) {
  		printf("Enter the Element : ");
  		scanf("%d",&val);
  		push(s, val);
	}
  	printStack(s);
  	pop(s);
  	printStack(s);
}
