import java.util.*;
import java.util.stream.Collectors;

public class Library {
    private final List<Book> books;
    private final Set<String> authors;
    private final Map<String, Integer> authorStatistics;

    public Library() {
        books = new ArrayList<>();
        authors = new HashSet<>();
        authorStatistics = new HashMap<>();
    }

    public void addBook(Book book) {
        if (book == null) return;

        books.add(book);
        authors.add(book.getAuthor());
        authorStatistics.merge(book.getAuthor(), 1, Integer::sum);
    }

    public boolean removeBook(Book book) {
        if (book == null || !books.remove(book)) {
            return false;
        }

        int count = authorStatistics.get(book.getAuthor()) - 1;
        if (count == 0) {
            authors.remove(book.getAuthor());
            authorStatistics.remove(book.getAuthor());
        } else {
            authorStatistics.put(book.getAuthor(), count);
        }
        return true;
    }

    public List<Book> findBooksByAuthor(String author) {
        return books.stream()
                .filter(book -> book.getAuthor().equalsIgnoreCase(author))
                .collect(Collectors.toList());
    }

    public List<Book> findBooksByYear(int year) {
        return books.stream()
                .filter(book -> book.getYear() == year)
                .collect(Collectors.toList());
    }

    public void printAllBooks() {
        if (books.isEmpty()) {
            System.out.println("В библиотеке нет книг");
            return;
        }
        System.out.println("Все книги в библиотеке:");
        books.forEach(System.out::println);
    }

    public void printUniqueAuthors() {
        if (authors.isEmpty()) {
            System.out.println("В библиотеке нет авторов");
            return;
        }
        System.out.println("Уникальные авторы:");
        authors.forEach(System.out::println);
    }

    public void printAuthorStatistics() {
        if (authorStatistics.isEmpty()) {
            System.out.println("Нет статистики по авторам");
            return;
        }
        System.out.println("Статистика по авторам:");
        authorStatistics.forEach((author, count) ->
                System.out.printf("%s: %d %s%n",
                        author,
                        count,
                        getBookCountForm(count)));
    }

    private String getBookCountForm(int count) {
        if (count % 100 >= 11 && count % 100 <= 14) {
            return "книг";
        }
        return switch (count % 10) {
            case 1 -> "книга";
            case 2, 3, 4 -> "книги";
            default -> "книг";
        };
    }
}