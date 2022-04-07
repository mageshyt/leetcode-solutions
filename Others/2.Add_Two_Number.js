
//  ! You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

//  ! You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// * Input: l1 = [2,4,3], l2 = [5,6,4]
// * Output: [7,0,8]
// * Explanation: 342 + 465 = 807.
// * Example 2:

// * Input: l1 = [0], l2 = [0]
// * Output: [0]

const addTwoNumbers=(l1, l2)=>{
    const sum_of_list=[]
    
    // ! max length of the array
    const max_length=Math.max(l1.length,l2.length)
    // ! loop through the lists 
    for(let i=0; i<max_length;i++){
            const sum=(l1[i] || 0) + (l2[i] ||0)
            if( sum <10){
                sum_of_list.push(sum)
            }else{
                sum_of_list[i]=
            }


    }
    console.log(sum_of_list);
}

let l1 = [2,4,3], l2 = [5,6,4]
addTwoNumbers(l1, l2)