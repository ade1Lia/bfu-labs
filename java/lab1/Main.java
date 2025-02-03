import java.util.Objects;
import java.util.Scanner;
import java.util.ArrayList;
import static java.util.Collections.min;

public class Main {
    private static final Scanner in = new Scanner(System.in);

    public static void main(String[] args) {

        while (true){
            System.out.println("Введите номер задания");
            int num = in.nextInt();
            switch (num){
                case 1:
                    sequence();
                    break;
                case 2:
                    series();
                    break;
                case 3:
                    treasure();
                    break;
                case 4:
                    transportation();
                    break;
                case 5:
                    even_number();
                    break;

            }
            break;
        }
    }

    static void sequence() {

        System.out.println("Введите число:");
        int n = in.nextInt();
        int k = 0;

        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;
                k += 1;
            } else {
                n = 3 * n + 1;
                k += 1;
            }
        }

        System.out.println("Количество шагов: " + k);
    }

    static void series() {

        System.out.println("Введите число:");
        int n = in.nextInt();
        System.out.printf("Введите %d чисел (каждое число с новой строки):", n);
        int[] numbers = new int[n];
        int sum = 0;

        for (int i = 0; i < n; i++) {
            numbers[i] = in.nextInt();
            if (i % 2 != 0) {
                sum -= numbers[i];
            } else {
                sum += numbers[i];
            }

        }
        System.out.print("Знакочередующая сумма ряда: " + sum);
    }

    static void treasure() {
        System.out.println("Введите координаты клада:");
        int x = in.nextInt();
        int y = in.nextInt();
        int counter = 0;
        String s;

        while (true) {
            s = in.nextLine();
            if (Objects.equals(s, "стоп")) {
                break;
            }
            if (Objects.equals(s, "север")) {
                int step = in.nextInt();

                if (y != 0) {
                    y -= step;
                    counter += 1;
                }
                else {
                    continue;
                }
            }

            if (Objects.equals(s, "юг")) {
                int step = in.nextInt();

                if (y!= 0) {
                    y += step;
                    counter += 1;
                }
                else {
                    continue;
                }
            }

            if (Objects.equals(s, "запад")) {
                int step = in.nextInt();

                if (x != 0) {
                    x += step;
                    counter += 1;
                }
                else {
                    continue;
                }
            }

            if (Objects.equals(s, "восток")) {
                int step = in.nextInt();

                if (x != 0) {
                    x -= step;
                    counter += 1;
                }
                else {
                    continue;
                }
            }
        }
        System.out.println("Минимальное количество указаний карты: " + counter);
    }

    static void transportation(){

        System.out.println("Введите количество дорог:");
        int number_roads = in.nextInt();
        int number = 0;
        int maxim_min = 0;
        System.out.println("Введите количество туннелей и их высоту:");
        for (int i = 0; i < number_roads; i ++){
            int tunnel = in.nextInt();
            ArrayList<Integer> minim = new ArrayList<>();

            for (int j = 0; j < tunnel; j++){
                int height = in.nextInt();
                minim.add(height);
            }

            int minim_element = min(minim);
            if (minim_element > maxim_min){
                maxim_min = minim_element;
                number = i;
            }
        }
        System.out.println("Номер дороги: " + (number+1) + "\nВыстоа грузовика:  " + maxim_min);
    }

    static void even_number(){
        System.out.println("Введите трёхзначное число:");
        int num = in.nextInt();
        int sum_dig = num / 100 + num % 100 / 10 + num % 10;
        int pr_dig =  num / 100 * num % 100 / 10 * num % 10;
        if (sum_dig % 2 == 0 && pr_dig % 2 == 0){
            System.out.printf("Число %d является дважды чётным", num);
        }
        else {
            System.out.printf("Число %d  не является дважды чётным", num);

        }
    }
}