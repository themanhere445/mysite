using System;

class Enemy
{
    Random random = new Random();

    public int x;
    public int y = 0;

    public int speed = 2;

    public Enemy()
    {
        x = random.Next(0, 50);
    }

    public void Move()
    {
        y += speed;
    }

    public void Reset()
    {
        y = 0;
        x = random.Next(0, 50);
    }
}
