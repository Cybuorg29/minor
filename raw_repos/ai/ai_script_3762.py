@RestController
public class PaymentController {
    @PostMapping("/payment")
    public void processPayment(@RequestBody PaymentRequest request) {
        // Process the payment inside this method
    }
}