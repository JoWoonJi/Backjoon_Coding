import java.util.Scanner;
class A10871{
    public static void main(String[]a){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt(),x=s.nextInt(),i;
        for (i=0;i<n;i++){
            int l=s.nextInt();
            if (l<x){
                System.out.print(l+" ");
            }
        s.close();
        }
    }
}

// import java.util.Scanner;
// class Main{
//     public static void main(String[]a){
//         Scanner s=new Scanner(System.in);
//         int n=s.nextInt(),x=s.nextInt(),i;
//         int[] l=new int[n];
//         for (i=0;i<n;i++){
//             l[i]=s.nextInt();
//         }
//         for (i=0;i<n;i++){
//             if(l[i]<x){
//                 System.out.print(l[i]+" ");
//             }
//         }
//         }
// }
