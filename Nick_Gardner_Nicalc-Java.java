//Final Java project
import java.lang.Math;
import java.util.*;
public class Nicalc 
{
    public static void main(String [ ] args)
    {
    double num1, num2, a, b, c, x1, x2, y1, y2;
    Scanner scan = new Scanner(System.in);  
    System.out.println("-----------------------------------------------------------------------------");
    System.out.println("*** Please type in the number of the operation you would like to execute ***");
    System.out.println("|1.Add|2.Subtract|3.Divide|4.Multiply|5.Exponent|6.Square Root|7.Distance|8.Midpoint|9.Quadratic|10.Ellipse Foci|11.Logarithm|12.Quit|  ");
    int op = scan.nextInt();
        if(op == 1)
        {
        System.out.println("Please type in number 1");
        num1 = scan.nextDouble();
        System.out.println("Please type in number 2");
        num2 = scan.nextDouble();

        System.out.println("The answer is " + (num1 + num2));
        }
        if(op == 2)
        {
        System.out.println("Please type in number 1");
        num1 = scan.nextDouble();
        System.out.println("Please type in number 2");
        num2 = scan.nextDouble();

        System.out.println("The answer is " + (num1 - num2));
        }
        if(op == 3) 
        {
        System.out.println("Please type in number 1");
        num1 = scan.nextDouble();
        System.out.println("Please type in number 2");
        num2 = scan.nextDouble();

        System.out.println("The answer is " + (num1 / num2));
        }
        if(op == 4) 
        {
        System.out.println("Please type in number 1");
        num1 = scan.nextDouble();
        System.out.println("Please type in number 2");
        num2 = scan.nextDouble();

        System.out.println("The answer is " + (num1 * num2));
        } 
        if(op == 5) 
        {
        System.out.println("Please type in a base");
        num1 = scan.nextDouble();
        System.out.println("Please type in an exponent");
        num2 = scan.nextDouble();

        System.out.println("The answer is " + (Math.pow(num1, num2)));
        }
        if(op == 6) 
        {
        System.out.println("Please type in number 1");
        num1 = scan.nextDouble();

        System.out.println("The answer is " + (Math.sqrt(num1)));
        }
        if(op == 7) 
        {
        System.out.println("Please type in x1");
        x1 = scan.nextDouble();
        System.out.println("Please type in y1");
        y1 = scan.nextDouble();
        System.out.println("Please type in x2");
        x2 = scan.nextDouble();
        System.out.println("Please type in y2");
        y2 = scan.nextDouble();

        System.out.println("The answer is " + (Math.sqrt((Math.pow((x2 - x1), 2)) + (Math.pow((y2 - y1), 2)))));
        }
        if(op == 8) 
        {
        System.out.println("Please type in x1");
        x1 = scan.nextDouble();
        System.out.println("Please type in y1");
        y1 = scan.nextDouble();
        System.out.println("Please type in x2");
        x2 = scan.nextDouble();
        System.out.println("Please type in y2");
        y2 = scan.nextDouble();

        System.out.println("The answer is (" + ((x1 + x2) / 2) + "," + ((y1 + y2) / 2) + ")");
        }   
        if(op == 9)
        {
        System.out.println("Please type in your a value");
        a = scan.nextDouble();
        System.out.println("Please type in your b value");
        b = scan.nextDouble();
        System.out.println("Please type in your c value");
        c = scan.nextDouble();
        double bottom_term, top_left_term, right, right2, right3, right4, step, step2, step3, step4;
        
        bottom_term = 2 * a;
        top_left_term = b * - 1;
        right = (Math.pow(b, 2));
        right2 = (4 * a * c);
        right3 = right - right2;
        right4 = Math.sqrt(Math.abs(right3));
        step = (b * -1) + right4;
        step2 = (b * -1) - right4;
        step3 = step / (2 * a);
        step4 = step2 / (2 * a);
            
          if(right4 - (Math.round(right4)) == 0);
          {
          System.out.println("Your zeroes are " + step3 + " and " + step4);
          }
          if(right4 - (Math.round(right4)) > 0);
          System.out.println(top_left_term + " +- sqrt(" + right3 + ")"); 
          System.out.println("--------------");
          System.out.println(" " + bottom_term + " ");
          System.out.println("Your zeroes are " + step3 + " and " + step4);
         }
        if(op == 10)
        {
        double orientation, h_input, k_input, choice3, choice4, minor, major, right_term, cF, k, k2, h, h2;
		System.out.println("Is the ellipse 1.vertical or 2.horizontal?");
        orientation = scan.nextDouble();
        System.out.println("Please type in h value");
        h_input = scan.nextDouble();
        System.out.println("Please type in k value");
        k_input= scan.nextDouble();
        System.out.println("Please type in the distance of your major axis ");
        choice3 = scan.nextDouble();
        System.out.println("Please type in the distance of your minor axis ");
        choice4 = scan.nextDouble();
        
		minor = Math.pow((choice4 * .5), 2);
		major = Math.pow((choice3 * .5), 2);

		  if(orientation == 1)
		  {
			if(minor > 0)
			{
			right_term = major - minor;
		    cF = Math.sqrt(right_term);
		    k = k_input + cF;
		    k2 = k_input - cF;
			System.out.println("Your first focus is (" + h_input + "," + k + ")");
			System.out.println("Your second focus is (" + h_input + "," + k2 + ")");
            }
			if(minor < 0)
			{
			right_term = major + minor;
			cF = Math.sqrt(right_term);
			k = k_input + cF;
			k2 = k_input - cF;
			System.out.println("Your first focus is (" + h_input + "," + k + ")");
			System.out.println("Your second focus is (" + h_input + "," + k2 + ")");
            }
          }
		if(orientation == 2)
		{
			if(minor > 0)
			{
			right_term = major - minor;
			cF = Math.sqrt(right_term);
			h = h_input + cF;
			h2 = h_input - cF;
			System.out.println("Your first focus is (" + h + "," + k_input + ")");
			System.out.println("Your second focus is (" + h2 + "," + k_input + ")");
            }
			if(minor < 0)
			{
			right_term = major + minor;
			cF = Math.sqrt(right_term);
			h = h_input + cF;
			h2 = h_input - cF;
			System.out.println("Your first focus is (" + h + "," + k_input + ")");
			System.out.println("Your second focus is (" + h2 + "," + k_input + ")");
            }
         }
        }
        if(op == 11)
        {
        double base, x, output;
        System.out.println("Please input the corresponding numbers or type '0.0' if they do not exist.");
        System.out.println("Please type in the base");
        base = scan.nextDouble();
        System.out.println("Please type in the x");
        x = scan.nextDouble();
        System.out.println("Please type in the output");
        output = scan.nextDouble();
            if(x == 0.0)
            {
            x = Math.log(output) / Math.log(base);
            System.out.print(x);
            }
            if(base == 0.0)
            {
            base = Math.pow(output,  (1 / x));
            System.out.println(base);
            }
            if(output == 0.0)
            {
            output = Math.pow(base, x);
            System.out.println(output);
            }
        }
        if(op == 12)
        {
        System.exit(0);
        }
    }
}
    
