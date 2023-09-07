using System;
using System.Collections.Generic;
using System.Text;

namespace Project_2
{
    class Point
    {
        private double x;
        public double X
        {
            get { return x; }
            set { x = value; }
        }
        private double y;
        public double Y
        {
            get { return y; }
            set { y = value; }
        }
        private double z;
        public double Z
        {
            get { return z; }
            set 
            {
                if (is2D == false)
                {
                    z = value;
                }
                else
                {
                    z = 0;
                }
            }
        }
        private bool is2D;
        public bool IS2D
        {
            get { return is2D; }
            set { is2D = value; }
        }
        public Point(bool flag2d)
        {
            is2D = flag2d;
            if (is2D == true)
            {
                x = 0;
                y = 0;
            }
            else
            {
                x = 0;
                y = 0;
                z = 0;
            }
        }
        public Point(Point pt)
        {
            is2D = true;

            if (is2D == true)
            {
                x = pt.x;
                y = pt.y;
            }
            else
            {
                x = pt.x;
                y = pt.y;
                z = pt.z;
            }

        }
        public Point(double x_, double y_, double z_)
        {          
            x = x_;
            y = y_;
            z = z_;
            is2D = false;
        }
        public Point(double x_, double y_)
        {
            x = x_;
            y = y_;
            is2D = true;
        }

        public void Convert2D()
        {
            z = 0;
            is2D = true;
        }
        public void Convert3D(double z_)
        {
            is2D = false;
            Z = z_;
        }

        public double GetDistance(Point pt)
        {
            double answer = 0;
            double sub1 = 0, sub2 = 0;

            double x2 = X;
            double y2 = Y;
            double z2 = Z;

            double x = pt.x;
            double y = pt.y;
            double z = pt.z;

            if (x2 - x == 0 && y2 - y == 0 || z2 - z == 0)
            {
                return 0;
            }
            else if (is2D == true)
            {
                sub1 = x2 - x;
                sub1 = sub1 * sub1;
                sub2 = y2 - y;
                sub2 = sub2 * sub2;

                answer = sub1 + sub2;
                answer = Math.Sqrt(answer);
            }

            return answer;

            
        }
        public double GetDistance(double x_, double y_, double z_)
        {
            double answer = 0;
            double sub1 = 0, sub2 = 0, sub3 = 0;

            double x2 = X;
            double y2 = Y;
            double z2 = Z;

            double x = x_;
            double y = y_;
            double z = z_;

            sub1 = x2 - x;
            sub1 = sub1 * sub1;
            sub2 = y2 - y;
            sub2 = sub2 * sub2;
            sub3 = z2 - z;
            sub3 = sub3 * sub3;
            answer = sub1 + sub2 + sub3;
            answer = Math.Sqrt(answer);

            return answer;

        }
        public void Transform(Point pt)
        {
            x += pt.x;
            y += pt.y;
            z += pt.z;
        }

        public void Transform(double x_, double y_, double z_)
        {
            x += x_;
            y += y_;
            z += z_;
        }
        public bool IsEqual (Point pt)
        {
            if (is2D && pt.is2D && x == pt.x && y == pt.y)
                return true;
            else if (!is2D && !pt.is2D && x == pt.x && y == pt.y && z == pt.z)
                return true;
            else
                return false;
        }
        public bool IsEqual(double x_, double y_, double z_)
        {
            if (!is2D && x == x_ && y == y_ && z == z_)
                return true;
            else
                return false;
        }
        public bool IsEqual(double x_, double y_)
        {
            if (is2D && x == x_ && y == y_)
                return true;
            else
                return false;
        }
        public bool IsOrigin()
        {
            return true;
        }
        public void Copy(Point pt)
        {
            pt.is2D = is2D;
            pt.x = x;
            pt.y = y;
            pt.z = z;
        }
        public override string ToString()
        {
            if (is2D == true)
                return " (" + x + "," + " " + y + ")";
            else
                return " (" + x + "," + " " + y + "," + " " + z + ")";
        }
    }
}