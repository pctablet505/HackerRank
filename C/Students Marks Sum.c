

//Complete the following function.

int marks_summation(int *marks, int number_of_students, char gender) {
    int sum = 0;
    int start = 0;
    if (gender == 'g') {
        start += 1;
    }
    if (start > number_of_students) {
        return sum;
    }
    while (start < number_of_students) {
        sum += marks[start];
        start += 2;
    }
    return sum;
    //Write your code here.
}

