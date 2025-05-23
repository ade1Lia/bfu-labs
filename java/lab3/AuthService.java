import java.util.ArrayList;
import java.util.List;

public class AuthService {
    private List<User> users;
    private List<Admin> admins;

    public AuthService() {
        this.users = new ArrayList<>();
        this.admins = new ArrayList<>();

        // Добавляем тестовых пользователей
        users.add(new User("user1", "password1"));
        users.add(new User("user2", "password2"));

        // Добавляем тестовых администраторов
        admins.add(new Admin("admin", "admin123"));
    }

    public User loginUser(String username, String password) {
        for (User user : users) {
            if (user.getUsername().equals(username) && user.getPassword().equals(password)) {
                return user;
            }
        }
        return null;
    }

    public Admin loginAdmin(String username, String password) {
        for (Admin admin : admins) {
            if (admin.getUsername().equals(username) && admin.getPassword().equals(password)) {
                return admin;
            }
        }
        return null;
    }

    public boolean registerUser(String username, String password) {
        // Проверяем, нет ли уже пользователя с таким именем
        for (User user : users) {
            if (user.getUsername().equals(username)) {
                return false;
            }
        }

        users.add(new User(username, password));
        return true;
    }
}