#include <iostream>

using namespace std;

class string1
{
protected:
    string word1;
};

class string2 : public string1
{
protected:
    string word2;

public:
    void isEqual()
    {
        if (word1 == word2)
            cout << "Equal" << endl;
        else
            cout << "Not Equal" << endl;
    }

    void readData()
    {
        cin >> word1 >> word2;
    }
};

int main()
{
    string2 s;
    s.readData();
    s.isEqual();
    return 0;
}