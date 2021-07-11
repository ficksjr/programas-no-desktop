using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp3
{
    class Retangulo
    {
        public double L;
        public double C;

        public double Area()
        {
            return L * C;
        }
        public double Perimetro()
        {
            return 2 * L + 2 * C;
        }
        public double Diagonal()
        {
            return Math.Sqrt(L * L + C * C);
        }
    }
}
