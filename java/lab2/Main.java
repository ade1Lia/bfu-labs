import java.util.Scanner;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {
    private static final Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("Введите номер задания");
            int num = in.nextInt();
            switch (num) {
                case 1:
                    task_1();
                    break;
                case 2:
                    task_2();
                    break;
                case 3:
                    task_3();
                    break;
                case 4:
                    task_4();
                    break;
                case 5:
                    task_5();
                    break;
                case 6:
                    task_6();
                    break;
                case 7:
                    task_7();
                    break;
                case 8:
                    task_8();
                    break;
            }
            break;
        }
    }

    static void task_1() {

        System.out.println("Введите строку");
        String str = in.next();
        Map<Character, Integer> charIndexMap = new HashMap<>();
        int start = 0;
        String substr = "";

        for (int end = 0; end < str.length(); end++) {
            char currentChar = str.charAt(end);
            if (charIndexMap.containsKey(currentChar)) {
                start = Math.max(start, charIndexMap.get(currentChar) + 1);
            }

            charIndexMap.put(currentChar, end);

            if (substr.length() < end - start + 1) {
                substr = str.substring(start, end + 1);
            }
        }
        System.out.println(substr);
    }

    static void task_2() {

        System.out.println("Введите длину первого массива");
        int length_a = in.nextInt();
        int[] a = new int[length_a];

        System.out.println("Введите элементы массива:");
        for (int i = 0; i < a.length; i++) {
            a[i] = in.nextInt();
        }

        System.out.println("Введите длину второго массива");
        int length_b = in.nextInt();
        int[] b = new int[length_b];

        System.out.println("Введите элементы массива:");
        for (int i = 0; i < b.length; i++) {
            b[i] = in.nextInt();
        }

        int[] c = new int[a.length + b.length];
        int count = 0;
        for (int i = 0; i < a.length; i++) {
            c[i] = a[i];
            count++;
        }
        for (int j = 0; j < b.length; j++) {
            c[count++] = b[j];
        }

        Arrays.sort(c);
        for (int i = 0; i < c.length; i++) System.out.print(c[i] + " ");

    }

    static void task_3() {

        System.out.println("Введите длину массива");
        int length = in.nextInt();
        int subArr = 0;
        int[] arr = new int[length];
        System.out.println("Введите элементы массива:");
        for (int i = 0; i < length; i++) {
            arr[i] = in.nextInt();
        }
        int maxSum = 0;

        for (int i = 0; i < length; i++) {
            subArr += arr[i];
            subArr = Integer.max(subArr, 0);
            maxSum = Integer.max(subArr, maxSum);
        }
        System.out.println("Максимальная сумма подмассива:" + subArr);

    }

    static void task_4() {

        System.out.println("Введите количество строк");
        int row = in.nextInt();
        System.out.println("Введите количество столбцов");
        int column = in.nextInt();
        int arr[][] = new int[row][column];
        System.out.println("Введите элементы массива");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                arr[i][j] = in.nextInt();
            }
        }

//        Вывод массива
        System.out.println("Исходный массив");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

        int arr2[][] = new int[column][row];
        System.out.println("Поворот на 90 по часовой");
        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row; j++) {
                arr2[i][j] = arr[row - j - 1 ][i];
                System.out.print(arr2[i][j] + " ");
            }
            System.out.println();
        }
    }

    static void task_5() {

        System.out.println("Введите длина массива");
        int length = in.nextInt();
        int arr[] = new int[length];
        System.out.println("Введите элементы массива");

        for (int i = 0; i < length; i++) {
            arr[i] = in.nextInt();
        }

        System.out.println("Массив: " + Arrays.toString(arr));

        System.out.println("Введите target");
        int target = in.nextInt();

        boolean flag = false;
        for (int i = 0; i < length; i++) {
            for (int j = i + 1; j < length; j++) {
                if (arr[i] != arr[j]) {
                    if (arr[i] + arr[j] == target) {
                        System.out.println(arr[i] + " " + arr[j]);
                        flag = true;
                    }
                }
            }
        }

        if (!flag) {
            System.out.println("null");
        }

    }

    static void task_6() {

        System.out.println("Введите количество строк");
        int row = in.nextInt();
        System.out.println("Введите количество столбцов");
        int column = in.nextInt();
        int arr[][] = new int[row][column];
        System.out.println("Введите элементы массива");
        int sum = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                arr[i][j] = in.nextInt();
                sum += arr[i][j];
            }
        }

        //   Вывод массива
        System.out.println("Исходный массив");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("Сумма массива равна " + sum);
    }

    static void task_7() {

        System.out.println("Введите количество строк");
        int row = in.nextInt();
        System.out.println("Введите количество столбцов");
        int column = in.nextInt();
        int arr[][] = new int[row][column];
        System.out.println("Введите элементы массива");
        int maxIsArr[] = new int[row];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                arr[i][j] = in.nextInt();

            }
        }

        //   Вывод массива
        System.out.println("Исходный массив");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

        for (int i = 0; i < row; i++) {
            maxIsArr[i] = Arrays.stream(arr[i]).max().getAsInt();
            System.out.println("Максимальный элемент " + (i + 1) + " строки равен " + maxIsArr[i]);
        }
    }

    static void task_8() {

        System.out.println("Введите количество строк");
        int row = in.nextInt();
        System.out.println("Введите количество столбцов");
        int column = in.nextInt();
        int arr[][] = new int[row][column];
        System.out.println("Введите элементы массива");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                arr[i][j] = in.nextInt();

            }
        }

        //   Вывод массива
        System.out.println("Исходный массив");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

        int[][] arr2 = new int[column][row];
        System.out.println("Поворот на 90 против часовой");
        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row; j++) {
                arr2[i][j] = arr[j][column - 1 - i];
                System.out.print(arr2[i][j] + " ");
            }
            System.out.println();
        }

    }
}