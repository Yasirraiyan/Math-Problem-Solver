#include <iostream>

using namespace std;

bool test(int n)
{
    bool isArmstrong = false;
    int rem, sum = 0;
    int original_n = n;

    while (n > 0)
    {
        rem = n % 10;
        sum += rem * rem * rem;
        n /= 10;
    }

    if (sum == original_n)
    {
        isArmstrong = true;
        cout << "The number you input is: Armstrong" << endl;
    }
    else
    {
        cout << "The number you input is: Not Armstrong" << endl;
    }

    return isArmstrong;
}

int main()
{
    int n;
    cout << "Enter the value of N: ";
    cin >> n;

    test(n); // Call the function correctly

    return 0;
}
