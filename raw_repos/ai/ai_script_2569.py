public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Get a reference to the TextView
        TextView textView = (TextView) findViewById(R.id.textView);

        // Set the text view to present the current date and time
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String currentDateTimeString = sdf.format(new Date());
        textView.setText(currentDateTimeString);
    }
}