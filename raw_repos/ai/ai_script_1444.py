public class TimestampProcessing {
    public static List<String> process(String[] timestamps) {
        List<String> result = new ArrayList<>();
        for (String timestamp : timestamps) {
            String dateFormat = "dd/MM/yyyy hh:mm:ss";
            Date date = new SimpleDateFormat(dateFormat).parse(timestamp);
            Calendar cal = Calendar.getInstance();
            cal.setTime(date);
            cal.add(Calendar.HOUR_OF_DAY, -2);
            String dateFormatUpdated = "MM/dd/yyyy hh:mm:ss a";
            SimpleDateFormat simpleDateFormat = new SimpleDateFormat(dateFormatUpdated);
            result.add(simpleDateFormat.format(cal.getTime()));
        }
        return result;
    }
}