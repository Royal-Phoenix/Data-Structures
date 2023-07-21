import java.util.*;
class Patterns {
    static void Pyramid(int n) {
	    int k = 0;
	    for (int i=1; i<=n; i++) {
		    for (int j=1; j<((n-i)+1); j++) {
			   System.out.print(" ");
		    }
		    while (k != ((2*i)-1)) {
		        System.out.print("*");
		        k += 1;
		    }
		    k = 0;
		    System.out.println();
	    }
    }
    static void Level(int n) {
    	int k = 0,i;
    	for (i=1; i<=n; i++) {
    		for (int j=1; j<((n-i)+1); j++) {
    		    System.out.print(" ");
    		}
    		while (k != ((2*i)-1)) {
    			System.out.print(i);
    			k += 1;
    		}
    		k = 0;
    		System.out.println();
    	}
    }
    static void Number(int n) {
    	int k = 0;
    	for (int i=1; i<=n; i++) {
    		for (int j=1; j<((n-i)+1); j++) {
    			System.out.print(" ");
    		}
    		while (k != ((2*i)-1)) {
    			System.out.print(k+1);
    			k += 1;
    		}
    		k = 0;
    		System.out.println();
    	}
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
    	int n, k, j, choice;
    	System.out.print("\n\nMENU\n1.Pyramid Pattern");
    	System.out.print("\n2.Level Pattern\n3.Number Pattern\n\n");
    	System.out.print("Enter the Number of Rows : ");
    	n = s.nextInt();
    	System.out.print("Enter the Choice : ");
    	choice = s.nextInt();
    	switch(choice) {
    		case 1:
    			Pyramid(n);
    			break;
    		case 2:
    			Level(n);
    			break;
    		case 3:
    			Number(n);
    			break;
    		default:
    			System.out.print("Invalid Choice \1\1\1");
    	}
    }
}