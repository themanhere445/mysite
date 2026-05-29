using System;

class Player
{
    public int x = 350;
    public int y = 500;

    public int speed = 5;

    public void Move(ConsoleKey key)
    {
        if (key == ConsoleKey.LeftArrow && x > 0)
        {
            x -= speed;
        }

        if (key == ConsoleKey.RightArrow && x < 750)
        {
            x += speed;
        }
    }
}
