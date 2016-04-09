#include "stdio.h"

void *lsearch(void *key, void *base, int n, int elemSize, int (*cmpfn)(void *, void *))
{
	for (int i = 0; i < n; ++i)
	{
		void *elemAddr = (char *)base + i * elemSize;
		if (cmpfn(key, elemAddr) == 0)
			return elemAddr;
	}
	return NULL;
}

int intCmp(void *elem1, void *elem2)
{
	int *ip1 = (int *)elem1;
	int *ip2 = (int *)elem2;

	return *ip1 - *ip2;
}

int main(int argc, char const *argv[])
{
	int arr[] = {6, 4, 7, 3, 10};
	int size = 5;
	int number = 3;
	int *found = (int *)lsearch(&number, arr, 5, sizeof(int), intCmp);

	printf("%d\n", *found);

	return 0;
}