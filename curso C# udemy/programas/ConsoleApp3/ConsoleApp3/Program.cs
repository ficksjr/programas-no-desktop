using System;
using System.Globalization;

namespace ConsoleApp3
{
    class Program
    {
        static void Main(string[] args)
        {
            Retangulo x;
            x = new Retangulo();

            Console.WriteLine("Entre com a largura e a altura do retângulo");
            x.L = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            x.C = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            x.Diagonal();
            x.Perimetro();
            Console.WriteLine("AREA = " +  x.Area());
            Console.WriteLine("DIAGONAL = " + x.Diagonal());
            Console.WriteLine("PERIMETRO = " + x.Perimetro());
        }
    }
}
// CultureInfo.InvariantCulture