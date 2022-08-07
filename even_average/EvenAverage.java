public class EvenAverage {
    public static void main(String[] args) {
        double sum = 0;
        double c = 0;
        double avg = 0;
        for(int counter = 1; counter < 10000; counter++) {
            if(counter % 2 == 0) {
                sum += counter;
                c++;

            }
        }
        avg = sum / c;
        System.out.println("The average of even numbers between 1 and 10 is: "+ avg);
    }
}
