public class Ticket {
    private Session session;
    private int row;
    private int seat;
    private double price;

    public Ticket(Session session, int row, int seat, double price) {
        this.session = session;
        this.row = row;
        this.seat = seat;
        this.price = price;
    }

    public Session getSession() {
        return session;
    }

    public int getRow() {
        return row;
    }

    public int getSeat() {
        return seat;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return "Билет на " + session.getMovie().getTitle() +
                ", ряд " + row + ", место " + seat +
                ", цена: " + price + " руб.";
    }
}