#include <stdio.h>
#include <stdlib.h>

// https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=1142

int compare_ints(const void *p, const void *q) {
    int x = *(const int *)p;
    int y = *(const int *)q;

	// the number won't be equal
    if (x < y)
        return -1;  // Return -1 if you want ascending, 1 if you want descending order. 
    else
        return 1;   // Return 1 if you want ascending, -1 if you want descending order. 
}

int bin_search_left(int* S, int target, int left, int right) {
	int mid = (right - left) / 2;
	if (mid <= 0) return right;
	if (S[mid] == target) return mid;
	else if (S[mid] < target) return bin_search_left(S, target, mid, right);
	else return bin_search_left(S, target, left, mid);
}

int bin_search_right(int* S, int target, int left, int right) {
	int mid = (right - left) / 2;
	if (mid <= 0) return left;
	if (S[mid] == target) return mid;
	else if (S[mid] < target) return bin_search_right(S, target, mid, right);
	else return bin_search_right(S, target, left, mid);
}

int find(int* S, int n, int left, int right) {
	// exploit the ordering to speed up
	int left_index=-1, right_index=-1;
	if (right < S[0] || left > S[n-1]) return 0;
	// left <= S[left]
	// so the left boundary is 0, right boundary is min(left, n)
	int r = left < n-1 ? left : n-1;
	left_index = bin_search_left(S, left, 0, r);
	// left <= right <= S[right]
	// right - left + 1 >= range
	// => right - left >= right_index - left_index
	// => right_index <= right - left + left_index
	// so the left boundary is left_index
	// and the right boundary is min(right, n, right-left+left_index)
	r = right < n-1 ? right : n-1;
	r = (r < right-left+left_index) ? r : (right-left+left_index);
	right_index = bin_search_right(S, right, left_index, r);
	if (left_index == -1 || right_index == -1) return 0;
	return right_index - left_index + 1;
}

void print(int* S, int n) {
	for(int i=0; i<n; i++)
		printf("%d\n", S[i]);
}

int main() {
	int n, m;
	int i = 0;
	int temp;
	int a, b;
	int* S;

	scanf("%d %d", &n, &m);
	S = (int*)malloc(sizeof(int) * n);
	for(i=0; i<n; i++){
		scanf("%d", S+i);
	}
	qsort(S, n, sizeof *S, &compare_ints);
	for(i=0; i<m; i++) {
		scanf("%d %d", &a, &b);
		printf("%d\n", find(S, n, a, b));
	}
	free(S);
	return 0;
}
