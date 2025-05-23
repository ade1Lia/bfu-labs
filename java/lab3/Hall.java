import java.util.ArrayList;
import java.util.List;

public class Hall {
    private int number;
    private int rows;
    private int seatsPerRow;
    private List<Session> sessions;

    public Hall(int number, int rows, int seatsPerRow) {
        this.number = number;
        this.rows = rows;
        this.seatsPerRow = seatsPerRow;
        this.sessions = new ArrayList<>();
    }

    public void addSession(Session session) {
        sessions.add(session);
    }

    public int getNumber() {
        return number;
    }

    public int getRows() {
        return rows;
    }

    public int getSeatsPerRow() {
        return seatsPerRow;
    }

    public List<Session> getSessions() {
        return sessions;
    }

    public int getTotalSeats() {
        return rows * seatsPerRow;
    }

    @Override
    public String toString() {
        return "Зал №" + number + ", мест: " + getTotalSeats() + " (" + rows + "x" + seatsPerRow + ")";
    }
}