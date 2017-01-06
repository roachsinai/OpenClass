#ifndef _STACK_H
#define _STACK_H

typedef struct 
{
	int *elems;
	int logicallen;
	int alloclength;
} stack;

void StackNew(stack *s);
void StackDispose(stack *s);
void StackPush(stack *s, int value);
int StackPop(stack *s);

#endif