#include <stdio.h>
#include <stdlib.h>

void sort(int* S, int n) {
	// in place sorting
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

int find(int* S, int n, int left, int right) {
	// the range won't exceed (right - left+1)
	// exploit the ordering to speed up
	int left_index=-1, right_index=-1;
	if (right < S[0] || left > S[n-1]) return 0;
	// try to find the left_index at first, then use range <= right - left + 1 to find right_index
	// use binary search
	int l=0, r=n;
	int mid; 
	while(1) {
		mid = (r - l) / 2;
		if (mid <= 0) {
			if (S[l] <= left) {
				left_index = l;
			}
			break;
		}
		if (S[mid] < left) {
			// left part
			r = mid;
		}
		else if (S[mid] == left) {
			// hit
			left_index = mid;
			break;
		}
		else {
			// right part
			l = mid;
		}
	}
	if (left_index == -1) {
		printf("left Error");
		return -1;
	}
	int bound = left_index+right-left+1;
	bound = bound > n ? n : bound;
	for(int i=bound-1; i>=left_index; i--) {
		if (S[i] <= right) {
			right_index = i;
			break;
		}
	}
	if (right_index == -1) {
		printf("right Error");
		return -1;
	}
	printf("%d %d\n", left_index, right_index);
	return right_index - left_index + 1;
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
	sort(S, n);
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
