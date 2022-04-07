// Weekly employee time-card of an organization has three data items: an identification number, the hourly wage rate, and the number.
// of hours worked during a given week. Each employee is paid one and half of the 
//wages for all hours worked over 40 hr 
// amount of 3.625% of gross wages will be deducted.
// Given an identification number, hourly wage rate and number of hours worked, write a 'C' program to display the employee's number
// and net pay separated by a tab. Round the net pay of the employee to three decimal places
// Input Format
// First line contains the identification Number
// Next line contains the hourly wage rate
// Next line contains the number of Hours worked
// Output Format
// Print the Employee number and net pay separated by a space
// Input:
// 1001
// 50
// 40
// Output:
// 1001 1927.500
// For example:
// Test Input Result
// 1001

// 50
// 40

#include <stdio.h>
void employee(rate, hours, id){
    float net;
    net = rate * hours;
    if (hours > 40){
        net = net + (rate * 1.5 * (hours - 40));
    }
    net = net - (net * 0.0625);
    printf("%d %.3f\n", id, net);

}
int main(){
        int id;
    float rate, hours;
    scanf("%d", &id);
    scanf("%f", &rate);
    scanf("%f", &hours);
    employee(id, rate, hours );   
    return      0;
}

