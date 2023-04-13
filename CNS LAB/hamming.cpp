#include <iostream>

using namespace std;

int main()
{
    int createarray[8];

    cout << "Enter 4 bits of data one by one\n";
    cin >> createarray[7];
    cin >> createarray[6];
    cin >> createarray[5];
    cin >> createarray[3];

    createarray[4] = createarray[5] ^ createarray[6] ^ createarray[7];
    createarray[2] = createarray[3] ^ createarray[6] ^ createarray[7];
    createarray[1] = createarray[3] ^ createarray[5] ^ createarray[7];

    cout << "\nEncoded data is\n";
    for (int i = 1; i <= 7; i++)
        cout << createarray[i];

    int recivedDataArray[8], c, c1, c2, c3, i;
    cout << "\n\nEnter received data bits one by one\n";
    for (i = 1; i <= 7; i++)
        cin >> recivedDataArray[i];

    c1 = recivedDataArray[1] ^ recivedDataArray[3] ^ recivedDataArray[5] ^ recivedDataArray[7];
    c2 = recivedDataArray[2] ^ recivedDataArray[3] ^ recivedDataArray[6] ^ recivedDataArray[7];
    c3 = recivedDataArray[4] ^ recivedDataArray[5] ^ recivedDataArray[6] ^ recivedDataArray[7];
    c = c3 * 4 + c2 * 2 + c1;
    if (c == 0)
    {
        cout << "\n no error: ";
    }
    else
    {
        cout << "\nerror on the postion:" << c;
        cout << "\nCorrect message is:";
        if (recivedDataArray[c] == 0)
            recivedDataArray[c] = 1;
        else
            recivedDataArray[c] = 0;
        for (i = 1; i <= 7; i++)
        {
            cout << recivedDataArray[i];
        }
    }

    return 0;
}
