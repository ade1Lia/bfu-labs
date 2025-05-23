import java.util.List;
public class LibraryTest {
    public static void main(String[] args) {
        Library library = new Library();

        // Создание тестовых данных
        Book[] testBooks = {
                new Book("To Kill a Mockingbird", "Harper Lee", 1960),
                new Book("1984", "George Orwell", 1949),
                new Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
                new Book("Pride and Prejudice", "Jane Austen", 1813),
                new Book("The Catcher in the Rye", "J.D. Salinger", 1951),
                new Book("The Hobbit", "J.R.R. Tolkien", 1937),
                new Book("The Lord of the Rings", "J.R.R. Tolkien", 1954),
                new Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
        };

        // Добавление книг в библиотеку
        System.out.println("Добавляем книги в библиотеку...");
        for (Book book : testBooks) {
            library.addBook(book);
        }

        // Тестирование методов
        System.out.println("\n=== Тест 1: Вывод всех книг ===");
        library.printAllBooks();

        System.out.println("\n=== Тест 2: Уникальные авторы ===");
        library.printUniqueAuthors();

        System.out.println("\n=== Тест 3: Статистика по авторам ===");
        library.printAuthorStatistics();

        System.out.println("\n=== Тест 4: Поиск по автору (J.R.R. Tolkien) ===");
        List<Book> tolstoyBooks = library.findBooksByAuthor("J.R.R. Tolkien");
        tolstoyBooks.forEach(System.out::println);

        System.out.println("\n=== Тест 5: Поиск по году (1954) ===");
        List<Book> books1869 = library.findBooksByYear(1954);
        books1869.forEach(System.out::println);

        System.out.println("\n=== Тест 6: Удаление книги ===");
        Book toRemove = testBooks[5]; // "The Hobbit"
        System.out.println("Удаляем: " + toRemove);
        library.removeBook(toRemove);

        System.out.println("\nОбновленная статистика:");
        library.printAuthorStatistics();
    }
}