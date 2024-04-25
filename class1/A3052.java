import java.util.Scanner;
class A3052{
    public static void main(String[]z){
        try(Scanner s=new Scanner(System.in)){
        int i,cnt=0;
        int[] x=new int[42];
        for (i=0;i<10;i++){
            int n=s.nextInt();
            if (x[n%42]==0){
                x[n%42]=1;
                cnt++;
            }
        }
        System.out.print(cnt);
        }
    }
}

// import java.util.Scanner;
// import java.util.HashSet;

// public class UniqueRemainders {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         HashSet<Integer> remainders = new HashSet<>();

//         for (int i = 0; i < 10; i++) {
//             int num = scanner.nextInt();
//             remainders.add(num % 42);
//         }
//         System.out.println(remainders.size());
//         scanner.close();
//     }
// }
