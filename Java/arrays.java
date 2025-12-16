//public class Array {
//
//    private
//    private int size;
//
//    public void traverse() {
//        for (int i=0; i<size; i++) {
//            System.out.println(item[i]);
//        }
//    }
//}

public class Main {
    
    public static void main(String[] args) {

        // array = used to store multiple values within a single variable

        String[] cars = new String[3];

        cars[0] = "Camaro";
        cars[1] = "Corvette";
        cars[2] = "Tesla";

        for (String car : cars) {
            System.out.println(car);
        }
    }
}