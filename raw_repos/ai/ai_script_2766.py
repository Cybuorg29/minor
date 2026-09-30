import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.input.KeyCode;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

public class MoveSquare extends Application {
    public static void main(String[] args) {
        launch(args);
    }
    
    public void start(Stage primaryStage) {       
        Rectangle rect = new Rectangle(30, 30);
        rect.setFill(Color.BLUE);
        
        Pane root = new Pane();
        root.getChildren().add(rect);
        
        Scene scene = new Scene(root);
        scene.setOnKeyPressed(event -> {
            KeyCode keyPressed = event.getCode();
            if (keyPressed == KeyCode.UP) {
                rect.setY(rect.getY() - 5);
            } else if (keyPressed == KeyCode.DOWN) {
                rect.setY(rect.getY() + 5);
            } else if (keyPressed == KeyCode.LEFT) {
                rect.setX(rect.getX() - 5);
            } else if (keyPressed == KeyCode.RIGHT) {
                rect.setX(rect.getX() + 5);
            }
        });
        
        primaryStage.setTitle("Move Square");
        primaryStage.setScene(scene);
        primaryStage.setWidth(300);
        primaryStage.setHeight(300);
        primaryStage.show();
        
        scene.requestFocus();
    }
}