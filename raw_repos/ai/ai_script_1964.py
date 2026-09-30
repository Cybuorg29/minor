@Configuration
public class StringBeanProvider {

    @Bean
    public String provideString() {
        return "Hello World!";
    }

}