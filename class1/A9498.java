import java.util.Scanner;
class A9498 {
    public static void main(String[] a){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        if (89<n&&n<101){
            System.out.print("A");
        }
        else if(79<n&&n<90){
            System.out.print("B");
        }
        else if(69<n&&n<80){
            System.out.print("C");
        }
        else if(59<n&&n<70){
            System.out.print("D");
        }
        else{
            System.out.print("F");
        }
        s.close();
    }
    
}
