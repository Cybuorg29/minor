import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DatabaseRetrieve {

    private Connection connection;
    private String query;

    public DatabaseRetrieve(Connection connection, String query) {
        this.connection = connection;
        this.query = query;
    }

    public ResultSet getData() throws SQLException {
        Statement stmt = connection.createStatement();
        ResultSet rs = stmt.executeQuery(query);
        return rs;
    }

}