import java.time.Duration;

public class Movie {
    private String title;
    private Duration duration;
    private String genre;
    private String description;

    public Movie(String title, Duration duration, String genre, String description) {
        this.title = title;
        this.duration = duration;
        this.genre = genre;
        this.description = description;
    }

    public String getTitle() {
        return title;
    }

    public Duration getDuration() {
        return duration;
    }

    public String getGenre() {
        return genre;
    }

    public String getDescription() {
        return description;
    }

    @Override
    public String toString() {
        return title + " (" + genre + ", " + duration.toMinutes() + " мин)";
    }
}