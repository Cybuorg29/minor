import java.util.List;
import java.util.stream.Collectors;

public class Solution {

  public static int getMostFrequentNumber(List<Integer> list) {
    return list.stream()
        .collect(Collectors.groupingBy(Integer::intValue, Collectors.counting()))
        .entrySet().stream()
        .max(Map.Entry.comparingByValue())
        .get().getKey();
  }
}