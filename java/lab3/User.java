import java.util.ArrayList;
import java.util.List;

public class User {
    private String username;
    private String password;
    private List<Ticket> tickets;

    public User(String username, String password) {
        this.username = username;
        this.password = password;
        this.tickets = new ArrayList<>();
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public void addTicket(Ticket ticket) {
        tickets.add(ticket);
    }

    public List<Ticket> getTickets() {
        return tickets;
    }

    public void printTickets() {
        if (tickets.isEmpty()) {
            System.out.println("У вас нет купленных билетов.");
            return;
        }

        System.out.println("Ваши билеты:");
        for (Ticket ticket : tickets) {
            System.out.println(ticket);
        }
    }
}