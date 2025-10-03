//finding minimum and maximum element
public class basics {
    public static void main(String[]args){
    int[] arr ={5,10,2,8,1};
    int min=arr[0];
    int max=arr[0];
    for(int num:arr){
        if(num<min)min=num;
        if(num>max)max=num;
    }
    System.out.println("Minimum: "+min);
    System.out.println("Maximum: "+max);
}
}
//Sum and average of elements
    