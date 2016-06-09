#include "stdio.h"
#include "stdlib.h"
#include "assert.h"

#include "stack.h"

void StackNew(stack *s)
{
	s->logicallen = 0;
	s->alloclength = 4;
	s->elems = (int *)malloc(4 * sizeof(int));

	assert(s->elems != NULL);
}

void StackDispose(stack *s)
{
	free(s->elems);
}
void StackPush(stack *s, int value)
{
	if (s->logicallen == s->alloclength)
	{
		s->alloclength *= 2;
		s->elems = (int *)realloc(s->elems, s->alloclength * sizeof(int));
	}
	assert(s->elems != NULL);

	s->elems[s->logicallen] = value;
	s->logicallen++;
}

int StackPop(stack *s)
{
	assert (s->logicallen > 0);
	s->logicallen--;
	return s->elems[s->logicallen];
}

int main(int argc, char const *argv[])
{
	
	return 0;
}