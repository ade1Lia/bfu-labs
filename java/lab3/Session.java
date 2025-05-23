import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class Session {
    private Movie movie;
    private LocalDateTime startTime;
    private Hall hall;
    private List<Ticket> tickets;

    public Session(Movie movie, LocalDateTime startTime, Hall hall) {
        this.movie = movie;
        this.startTime = startTime;
        this.hall = hall;
        this.tickets = new ArrayList<>();
    }

    public void addTicket(Ticket ticket) {
        tickets.add(ticket);
    }

    public Movie getMovie() {
        return movie;
    }

    public LocalDateTime getStartTime() {
        return startTime;
    }

    public Hall getHall() {
        return hall;
    }

    public List<Ticket> getTickets() {
        return tickets;
    }

    public int getAvailableSeats() {
        return hall.getTotalSeats() - tickets.size();
    }

    public void printSeatMap() {
        System.out.println("Экран");
        System.out.println("-------------------");

        for (int row = 1; row <= hall.getRows(); row++) {
            final int currentRow = row; // Создаем финальную копию для использования в лямбде
            for (int seat = 1; seat <= hall.getSeatsPerRow(); seat++) {
                final int currentSeat = seat; // Создаем финальную копию для использования в лямбде
                boolean isOccupied = tickets.stream()
                        .anyMatch(t -> t.getRow() == currentRow && t.getSeat() == currentSeat);
                System.out.print(isOccupied ? "[X]" : "[ ]");
            }
            System.out.println();
        }
    }

    @Override
    public String toString() {
        return movie.getTitle() + ", начало: " + startTime +
                ", зал №" + hall.getNumber() +
                ", свободных мест: " + getAvailableSeats();
    }
}