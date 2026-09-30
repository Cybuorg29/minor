class TestResults {
    // A map containing the question id as key and the selected answer as value
    Map<Integer, Integer> answers;
  
    // A map containing the question id as key and a boolean indicating whether the answer was correct or not as value
    Map<Integer, Boolean> scores;
  
    // A map containing the question id as key and a list of all the possible answers as value
    Map<Integer, List<String>> questions;
  
    public TestResults(Map<Integer, Integer> answers, Map<Integer, Boolean> scores, Map<Integer, List<String>> questions) {
        this.answers = answers;
        this.scores = scores;
        this.questions = questions;
    }
  
    public Map<Integer, Integer> getAnswers() {
        return answers;
    }
  
    public Map<Integer, Boolean> getScores() {
        return scores;
    }
    
    public Map<Integer, List<String>> getQuestions() {
        return questions;
    }
}