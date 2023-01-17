/**
 * 
 * @author satis
 * 
 *         Problem statement -
 * 
 *         1.
 *         https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
 *         https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true
 *
 */
public class ArrayRevereseDemo1 {
	public static void main(String[] args) {
		int[] a = { 1, 2, 3, 4, 5, 6 };
		int len = a.length;
		printArray(a);
		rvereseArray(a, 0, len - 1);
		printArray(a);
	}

	private static void rvereseArray(int[] a, int start, int end) {
		while (start < end) {
			int tmp = a[start];
			a[start] = a[end];
			a[end] = tmp;
			start++;
			end--;
		}
	}

	private static void printArray(int[] a) {
		for (int i : a) {
			System.out.print(i + " ");
		}
		System.out.println();

	}

}
