import java.time.Duration;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CinemaSystem {
    private List<Cinema> cinemas;
    private List<Movie> movies;
    private AuthService authService;
    private User currentUser;
    private Scanner scanner;

    public CinemaSystem() {
        this.cinemas = new ArrayList<>();
        this.movies = new ArrayList<>();
        this.authService = new AuthService();
        this.scanner = new Scanner(System.in);

        // Инициализация тестовых данных
        initializeTestData();
    }

    private void initializeTestData() {
        // Добавляем фильмы
        movies.add(new Movie("Леди Баг", Duration.ofMinutes(169), "Фантастика", "Мультфильм про супергероев"));
        movies.add(new Movie("Обитель Анубиса", Duration.ofMinutes(175), "Детектив", "Фильм про мифы Египта"));
        movies.add(new Movie("Мавка", Duration.ofMinutes(142), "Драма", "История Лесной песни"));

        // Добавляем кинотеатры и залы
        Cinema cinema1 = new Cinema("Мультиплекс", "ул. Портсити, 15");
        cinema1.addHall(new Hall(1, 10, 15));
        cinema1.addHall(new Hall(2, 8, 12));

        Cinema cinema2 = new Cinema("СинемаПорт", "ул. Пилипа Орлика, 95");
        cinema2.addHall(new Hall(1, 12, 20));

        cinemas.add(cinema1);
        cinemas.add(cinema2);

        // Добавляем сеансы
        Hall hall1 = cinema1.getHalls().get(0);
        Hall hall2 = cinema1.getHalls().get(1);
        Hall hall3 = cinema2.getHalls().get(0);

        LocalDateTime now = LocalDateTime.now();

        hall1.addSession(new Session(movies.get(0), now.plusHours(2), hall1));
        hall1.addSession(new Session(movies.get(1), now.plusHours(5), hall1));
        hall2.addSession(new Session(movies.get(2), now.plusHours(3), hall2));
        hall3.addSession(new Session(movies.get(0), now.plusHours(1), hall3));
    }

    public void run() {
        System.out.println("Добро пожаловать в билетную систему кинотеатров!");

        while (true) {
            if (currentUser == null) {
                showMainMenu();
            } else if (currentUser instanceof Admin) {
                showAdminMenu();
            } else {
                showUserMenu();
            }
        }
    }

    private void showMainMenu() {
        System.out.println("\nГлавное меню:");
        System.out.println("1. Вход");
        System.out.println("2. Регистрация");
        System.out.println("3. Выход");
        System.out.print("Выберите действие: ");

        int choice = scanner.nextInt();
        scanner.nextLine(); // consume newline

        switch (choice) {
            case 1:
                login();
                break;
            case 2:
                register();
                break;
            case 3:
                System.out.println("До свидания!");
                System.exit(0);
                break;
            default:
                System.out.println("Неверный выбор. Попробуйте снова.");
        }
    }

    private void login() {
        System.out.print("Введите имя пользователя: ");
        String username = scanner.nextLine();
        System.out.print("Введите пароль: ");
        String password = scanner.nextLine();

        // Сначала пробуем войти как администратор
        currentUser = authService.loginAdmin(username, password);

        if (currentUser == null) {
            // Если не администратор, пробуем как обычный пользователь
            currentUser = authService.loginUser(username, password);
        }

        if (currentUser != null) {
            System.out.println("Вход выполнен успешно!");
        } else {
            System.out.println("Неверное имя пользователя или пароль.");
        }
    }

    private void register() {
        System.out.print("Введите имя пользователя: ");
        String username = scanner.nextLine();
        System.out.print("Введите пароль: ");
        String password = scanner.nextLine();

        if (authService.registerUser(username, password)) {
            System.out.println("Регистрация прошла успешно!");
        } else {
            System.out.println("Пользователь с таким именем уже существует.");
        }
    }

    private void showAdminMenu() {
        System.out.println("\nМеню администратора:");
        System.out.println("1. Добавить кинотеатр");
        System.out.println("2. Добавить зал в кинотеатр");
        System.out.println("3. Добавить фильм");
        System.out.println("4. Создать сеанс");
        System.out.println("5. Просмотреть все кинотеатры");
        System.out.println("6. Выход из системы");
        System.out.print("Выберите действие: ");

        int choice = scanner.nextInt();
        scanner.nextLine(); // consume newline

        switch (choice) {
            case 1:
                addCinema();
                break;
            case 2:
                addHall();
                break;
            case 3:
                addMovie();
                break;
            case 4:
                addSession();
                break;
            case 5:
                listCinemas();
                break;
            case 6:
                currentUser = null;
                System.out.println("Выход из системы выполнен.");
                break;
            default:
                System.out.println("Неверный выбор. Попробуйте снова.");
        }
    }

    private void showUserMenu() {
        System.out.println("\nМеню пользователя:");
        System.out.println("1. Поиск сеансов");
        System.out.println("2. Купить билет");
        System.out.println("3. Просмотреть мои билеты");
        System.out.println("4. Поиск ближайшего сеанса");
        System.out.println("5. Выход из системы");
        System.out.print("Выберите действие: ");

        int choice = scanner.nextInt();
        scanner.nextLine(); // consume newline

        switch (choice) {
            case 1:
                searchSessions();
                break;
            case 2:
                buyTicket();
                break;
            case 3:
                currentUser.printTickets();
                break;
            case 4:
                findNearestSession();
                break;
            case 5:
                currentUser = null;
                System.out.println("Выход из системы выполнен.");
                break;
            default:
                System.out.println("Неверный выбор. Попробуйте снова.");
        }
    }

    private void addCinema() {
        System.out.print("Введите название кинотеатра: ");
        String name = scanner.nextLine();
        System.out.print("Введите адрес кинотеатра: ");
        String address = scanner.nextLine();

        cinemas.add(new Cinema(name, address));
        System.out.println("Кинотеатр успешно добавлен.");
    }

    private void addHall() {
        if (cinemas.isEmpty()) {
            System.out.println("Сначала добавьте кинотеатр.");
            return;
        }

        listCinemas();
        System.out.print("Выберите кинотеатр (номер): ");
        int cinemaIndex = scanner.nextInt() - 1;
        scanner.nextLine(); // consume newline

        if (cinemaIndex < 0 || cinemaIndex >= cinemas.size()) {
            System.out.println("Неверный выбор кинотеатра.");
            return;
        }

        System.out.print("Введите номер зала: ");
        int number = scanner.nextInt();
        System.out.print("Введите количество рядов: ");
        int rows = scanner.nextInt();
        System.out.print("Введите количество мест в ряду: ");
        int seatsPerRow = scanner.nextInt();
        scanner.nextLine(); // consume newline

        Cinema cinema = cinemas.get(cinemaIndex);
        cinema.addHall(new Hall(number, rows, seatsPerRow));
        System.out.println("Зал успешно добавлен в кинотеатр " + cinema.getName());
    }

    private void addMovie() {
        System.out.print("Введите название фильма: ");
        String title = scanner.nextLine();
        System.out.print("Введите продолжительность фильма (в минутах): ");
        int minutes = scanner.nextInt();
        scanner.nextLine(); // consume newline
        System.out.print("Введите жанр фильма: ");
        String genre = scanner.nextLine();
        System.out.print("Введите описание фильма: ");
        String description = scanner.nextLine();

        movies.add(new Movie(title, Duration.ofMinutes(minutes), genre, description));
        System.out.println("Фильм успешно добавлен.");
    }

    private void addSession() {
        if (cinemas.isEmpty()) {
            System.out.println("Нет доступных кинотеатров.");
            return;
        }

        if (movies.isEmpty()) {
            System.out.println("Нет доступных фильмов.");
            return;
        }

        // Выбираем кинотеатр
        listCinemas();
        System.out.print("Выберите кинотеатр (номер): ");
        int cinemaIndex = scanner.nextInt() - 1;
        scanner.nextLine(); // consume newline

        if (cinemaIndex < 0 || cinemaIndex >= cinemas.size()) {
            System.out.println("Неверный выбор кинотеатра.");
            return;
        }

        Cinema cinema = cinemas.get(cinemaIndex);

        // Выбираем зал
        if (cinema.getHalls().isEmpty()) {
            System.out.println("В этом кинотеатре нет залов.");
            return;
        }

        System.out.println("Доступные залы:");
        for (int i = 0; i < cinema.getHalls().size(); i++) {
            System.out.println((i + 1) + ". " + cinema.getHalls().get(i));
        }

        System.out.print("Выберите зал (номер): ");
        int hallIndex = scanner.nextInt() - 1;
        scanner.nextLine(); // consume newline

        if (hallIndex < 0 || hallIndex >= cinema.getHalls().size()) {
            System.out.println("Неверный выбор зала.");
            return;
        }

        Hall hall = cinema.getHalls().get(hallIndex);

        // Выбираем фильм
        listMovies();
        System.out.print("Выберите фильм (номер): ");
        int movieIndex = scanner.nextInt() - 1;
        scanner.nextLine(); // consume newline

        if (movieIndex < 0 || movieIndex >= movies.size()) {
            System.out.println("Неверный выбор фильма.");
            return;
        }

        Movie movie = movies.get(movieIndex);

        // Вводим дату и время сеанса
        System.out.print("Введите дату и время сеанса (ГГГГ-ММ-ДД ЧЧ:ММ): ");
        String dateTimeStr = scanner.nextLine();
        LocalDateTime startTime = LocalDateTime.parse(dateTimeStr.replace(" ", "T"));

        hall.addSession(new Session(movie, startTime, hall));
        System.out.println("Сеанс успешно добавлен.");
    }

    private void listCinemas() {
        if (cinemas.isEmpty()) {
            System.out.println("Нет доступных кинотеатров.");
            return;
        }

        System.out.println("Список кинотеатров:");
        for (int i = 0; i < cinemas.size(); i++) {
            System.out.println((i + 1) + ". " + cinemas.get(i));
        }
    }

    private void listMovies() {
        if (movies.isEmpty()) {
            System.out.println("Нет доступных фильмов.");
            return;
        }

        System.out.println("Список фильмов:");
        for (int i = 0; i < movies.size(); i++) {
            System.out.println((i + 1) + ". " + movies.get(i));
        }
    }

    private void searchSessions() {
        if (movies.isEmpty()) {
            System.out.println("Нет доступных фильмов.");
            return;
        }

        listMovies();
        System.out.print("Выберите фильм (номер) или 0 для всех: ");
        int movieIndex = scanner.nextInt() - 1;
        scanner.nextLine(); // consume newline

        Movie selectedMovie = null;
        if (movieIndex >= 0 && movieIndex < movies.size()) {
            selectedMovie = movies.get(movieIndex);
        } else if (movieIndex != -1) {
            System.out.println("Неверный выбор фильма.");
            return;
        }

        System.out.println("Доступные сеансы:");
        boolean found = false;

        for (Cinema cinema : cinemas) {
            for (Hall hall : cinema.getHalls()) {
                for (Session session : hall.getSessions()) {
                    if (selectedMovie == null || session.getMovie().equals(selectedMovie)) {
                        System.out.println(cinema.getName() + ", " + hall + ", " + session);
                        found = true;
                    }
                }
            }
        }

        if (!found) {
            System.out.println("Сеансы не найдены.");
        }
    }

    private void buyTicket() {
        searchSessions();

        if (cinemas.isEmpty()) {
            return;
        }

        System.out.print("Введите название кинотеатра: ");
        String cinemaName = scanner.nextLine();
        System.out.print("Введите номер зала: ");
        int hallNumber = scanner.nextInt();
        System.out.print("Введите название фильма: ");
        scanner.nextLine(); // consume newline
        String movieTitle = scanner.nextLine();
        System.out.print("Введите дату и время сеанса (ГГГГ-ММ-ДД ЧЧ:ММ): ");
        String dateTimeStr = scanner.nextLine();
        LocalDateTime startTime = LocalDateTime.parse(dateTimeStr.replace(" ", "T"));

        Session selectedSession = null;

        for (Cinema cinema : cinemas) {
            if (cinema.getName().equalsIgnoreCase(cinemaName)) {
                for (Hall hall : cinema.getHalls()) {
                    if (hall.getNumber() == hallNumber) {
                        for (Session session : hall.getSessions()) {
                            if (session.getMovie().getTitle().equalsIgnoreCase(movieTitle) &&
                                    session.getStartTime().equals(startTime)) {
                                selectedSession = session;
                                break;
                            }
                        }
                    }
                }
            }
        }

        if (selectedSession == null) {
            System.out.println("Сеанс не найден.");
            return;
        }

        if (selectedSession.getAvailableSeats() == 0) {
            System.out.println("На этот сеанс нет свободных мест.");
            return;
        }

        // Показываем схему зала
        selectedSession.printSeatMap();

        // Выбираем место
        System.out.print("Введите номер ряда: ");
        final int row = scanner.nextInt(); // Делаем финальной
        System.out.print("Введите номер места: ");
        final int seat = scanner.nextInt(); // Делаем финальной
        scanner.nextLine(); // consume newline

        // Проверяем, что место существует
        if (row < 1 || row > selectedSession.getHall().getRows() ||
                seat < 1 || seat > selectedSession.getHall().getSeatsPerRow()) {
            System.out.println("Неверно указано место.");
            return;
        }

        // Проверяем, что место свободно
        boolean isOccupied = selectedSession.getTickets().stream()
                .anyMatch(t -> t.getRow() == row && t.getSeat() == seat);

        if (isOccupied) {
            System.out.println("Это место уже занято.");
            return;
        }

        // Рассчитываем цену (просто пример)
        double price = 300 + (selectedSession.getHall().getRows() - row) * 50;

        // Создаем билет
        Ticket ticket = new Ticket(selectedSession, row, seat, price);
        selectedSession.addTicket(ticket);
        currentUser.addTicket(ticket);

        System.out.println("Билет успешно куплен:");
        System.out.println(ticket);
    }

    private void findNearestSession() {
        if (movies.isEmpty()) {
            System.out.println("Нет доступных фильмов.");
            return;
        }

        listMovies();
        System.out.print("Выберите фильм (номер): ");
        int movieIndex = scanner.nextInt() - 1;
        scanner.nextLine(); // consume newline

        if (movieIndex < 0 || movieIndex >= movies.size()) {
            System.out.println("Неверный выбор фильма.");
            return;
        }

        Movie movie = movies.get(movieIndex);
        LocalDateTime now = LocalDateTime.now();
        Session nearestSession = null;
        long minDiff = Long.MAX_VALUE;

        for (Cinema cinema : cinemas) {
            for (Hall hall : cinema.getHalls()) {
                for (Session session : hall.getSessions()) {
                    if (session.getMovie().equals(movie) &&
                            session.getStartTime().isAfter(now) &&
                            session.getAvailableSeats() > 0) {

                        long diff = java.time.Duration.between(now, session.getStartTime()).toMinutes();
                        if (diff < minDiff) {
                            minDiff = diff;
                            nearestSession = session;
                        }
                    }
                }
            }
        }

        if (nearestSession != null) {
            System.out.println("Ближайший сеанс:");
            Cinema cinema = null;
            for (Cinema c : cinemas) {
                if (c.getHalls().contains(nearestSession.getHall())) {
                    cinema = c;
                    break;
                }
            }

            System.out.println(cinema.getName() + ", " +
                    nearestSession.getHall() + ", " +
                    nearestSession);
        } else {
            System.out.println("Нет доступных сеансов для выбранного фильма.");
        }
    }
}