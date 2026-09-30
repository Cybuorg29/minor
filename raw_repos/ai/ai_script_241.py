public class TowersOfHanoi { 
    public static void towersOfHanoi(int n, char from_rod, 
                              char to_rod, char aux_rod) 
    { 
        if (n == 1) { 
            System.out.println("Move disk 1 from rod " +  from_rod + " to rod " + to_rod); 
            return; 
        } 
        towersOfHanoi(n - 1, from_rod, aux_rod, to_rod); 
        System.out.println("Move disk " + n + " from rod " +  from_rod + " to rod " + to_rod); 
        towersOfHanoi(n - 1, aux_rod, to_rod, from_rod); 
    } 
  
    //  Driver method 
    public static void main(String args[]) 
    { 
        // Number of disks 
        int n = 4; 
  
        // A, B and C are names of rods 
        towersOfHanoi(n, 'A', 'C', 'B'); 
    } 
}