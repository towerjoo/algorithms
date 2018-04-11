#include <stdio.h>
#include <stdlib.h>

// https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=1142

void sort(int* S, int n) {
	// in place bubble sorting
	int t;
	for(int i=n-1; i>=1; i--) {
		for(int j=i-1; j>=0; j--) {
			if (S[i] < S[j]) {
				t = S[i];
				S[i] = S[j];
				S[j] = t;
			}
		}
	}
}

int compare_ints(const void *p, const void *q) {
    int x = *(const int *)p;
    int y = *(const int *)q;

	// the number won't be equal
    if (x < y)
        return -1;  // Return -1 if you want ascending, 1 if you want descending order. 
    else
        return 1;   // Return 1 if you want ascending, -1 if you want descending order. 
}

int find(int* S, int n, int left, int right) {
	// exploit the ordering to speed up
	int left_index=-1, right_index=-1;
	if (right < S[0] || left > S[n-1]) return 0;
	// left <= S[left]
	// so the left boundary is 0, right boundary is min(left, n)
	int r = left < n-1 ? left : n-1;
	for(int i=0; i<=r; i++) {
		if (S[i] >= left) {
			left_index = i;
			break;
		}
	}
	// left <= right <= S[right]
	// right - left + 1 >= range
	// => right - left >= right_index - left_index
	// => right_index <= right - left + left_index
	// so the left boundary is left_index
	// and the right boundary is min(right, n, right-left+left_index)
	r = right < n-1 ? right : n-1;
	r = (r < right-left+left_index) ? r : (right-left+left_index);
	
	for(int i=r; i>=left_index; i--) {
		if (S[i] <= right) {
			right_index = i;
			break;
		}
	}
	if (left_index == -1 || right_index == -1) return 0;
	return right_index - left_index + 1;
}

void print(int* S, int n) {
	for(int i=0; i<n; i++)
		printf("%d ", S[i]);
	printf("\n");
}

int main() {
	int n, m;
	int i = 0;
	int temp;
	int a, b;
	int* S;
	int* query;

	scanf("%d %d", &n, &m);
	S = (int*)malloc(sizeof(int) * n);
	for(i=0; i<n; i++){
		scanf("%d", &temp);
		S[i] = temp;
	}
	qsort(S, n, sizeof *S, &compare_ints);
	query = (int*)malloc(sizeof(int) * m * 2);
	for(i=0; i<m*2; i+=2) {
		scanf("%d %d", &a, &b);
		query[i] = a;
		query[i+1] = b;
	}
	for(i=0; i<m*2; i+=2) {
		a = query[i];		
		b = query[i+1];		
		printf("%d\n", find(S, n, a, b));
	}
	
	free(S);
	free(query);
	return 0;
}
