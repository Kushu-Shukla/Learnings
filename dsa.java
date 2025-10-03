//in java last element arr[arr.length-1]
//forloop
// for(int i = 0; i < arr.length; i++) {
//     System.out.println(arr[i]);
// }
// //while loop
// int i = 0;
// while(i < arr.length) {
//     System.out.println(arr[i]);
//     i++;
// }
// //for each loop
// for(int num : arr) {
//     System.out.println(num);
// }
// //input/output
// Scanner sc = new Scanner(System.in);
// int n = sc.nextInt();
// int[] arr = new int[n];
// for(int i = 0; i < n; i++) {
//     arr[i] = sc.nextInt();
// }
// //output array
// for(int num : arr) {
//     System.out.print(num + " ");
// }
// //ACcessing elements
// int[] arr = {5, 10, 15, 20};
// System.out.println(arr[0]); // 5
// System.out.println(arr[3]); // 20 (last element)
// //updating elements
// arr[1] = 50; // Update second element
// System.out.println(arr[1]); // 50
// //insertion
// int[] arr = {1, 2, 4, 5, 0}; // 0 is empty slot
// int insertVal = 3;
// int pos = 2; // index where we insert

// for(int i = arr.length - 1; i > pos; i--) {
//     arr[i] = arr[i - 1]; // shift elements
// }
// arr[pos] = insertVal; // insert
// //deletion
// // Delete element at index 2
// for(int i = 2; i < arr.length - 1; i++) {
//     arr[i] = arr[i + 1];
// }
// arr[arr.length - 1] = 0; // optional, clear last element
// //searching
// int key = 15;
// for(int i = 0; i < arr.length; i++) {
//     if(arr[i] == key) {
//         System.out.println("Found at index: " + i);
//     }
// }
// //Binary Search
// Arrays.sort(arr); // must be sorted
// int key = 15;
// int result = Arrays.binarySearch(arr, key);
// System.out.println("Index: " + result);
// //length of array
// System.out.println("Array size: " + arr.length);
