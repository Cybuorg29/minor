import java.sql.Connection;
import java.sql.DriverManager;

String host = "localhost";
int port = 3306;
String username = "user";
String password = "password";
String database = "sampledb";

String connectionString = "jdbc:mysql://"+host+":"+port+"/"+database;
Connection connection = DriverManager.getConnection(connectionString , username, password);