
#include <iostream>

using namespace std;

class Rectangle
{

private:
    int width;
    int length;

public:
    void setLength(float value)
    {
        length = value;
    };


    void setWidth(float value)
    {
        width = value;
    };

    float perimeter()
    {
        cout << 2 * (width + length) << endl;
        return 2 * (width + length);
    };

    float area()
    {
        cout << width * length << endl;
        return width * length;
    };
    void show()
    {
        //! display the len and width
        cout << length << endl;
        cout << width << endl;
    }

    int IsSameArea(Rectangle r)
    {
        if (r.area() == area())
        {
            cout << "YES" << endl;
            return 1;
        }
        else
        {
            cout << "NO" << endl;
            return 0;
        }
    }
};

int main()
{
    Rectangle r1, r2;
    r1.setLength(10);
    r1.setWidth(4);
    r1.area();
    r1.perimeter();

    r2.setLength(15);
    r2.setWidth(13);
    r2.area();
    r2.perimeter();

    r1.IsSameArea(r2);
    return 0;
}
