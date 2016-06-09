// episode 5
// implement build-in function lsearch & bsearch

#include "stdio.h"

void *lsearch(void *key, void *base, int n, int elemSize, int (*cmpfn)(void *, void *))
{
	void *elemAddr;

	for (int i = 0; i < n; ++i)
	{
		elemAddr = (char *)base + i * elemSize;
		if (cmpfn(key, elemAddr) == 0)
			return elemAddr;
	}
	return NULL;
}

void *bsearch(void *key, void *base, int n, int elemsize, int (*cmpfn)(void *, void *))
{
	int low = 0, high = n -1;
	int mid;
	void *elemAddr;

	while (low <= high)
	{
		mid = (low + high) / 2;
		elemAddr = (char *)base + mid * elemsize;

		if (cmpfn(key, elemAddr) == 0)
			return elemAddr;

		if (cmpfn(key, elemAddr) < 0)
			high = mid -1;

		if (cmpfn(key, elemAddr) > 0)
			low = mid + 1;
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
	int size = 5;
	int number = 3;

	// lsearch 线性查找
	int larr[] = {6, 4, 7, 3, 10};
	int *found = (int *)lsearch(&number, larr, 5, sizeof(int), intCmp);

	printf("%d\n", *found);

	// bsearch 二分查找
	int barr[] = {3, 4, 6, 7, 10};
	found = (int *)lsearch(&number, barr, 5, sizeof(int), intCmp);

	printf("%d\n", *found);

	return 0;
}