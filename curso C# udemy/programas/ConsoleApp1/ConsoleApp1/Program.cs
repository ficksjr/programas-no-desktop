using System;
using System.Globalization;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string produto1 = "Computador";
            string produto2 = "Mesa de escritório";
            
            byte idade = 30;
            int codigo = 5290;
            char genero = 'M';

            double preco1 = 2100.0;
            double preco2 = 650.50;
            double medida = 53.234567;

            Console.WriteLine("Produtos:");
            Console.WriteLine($"{produto1}, cujo preço é $ {preco1:F2}");
            Console.WriteLine($"{produto2}, cujo preço é $ {preco2:F2}");
            Console.Write("Registro: ");
            Console.WriteLine($"{idade} anos de idade, código {codigo} e gênero {genero}");
            Console.Write("Medida com oito casas decimais: ");
            Console.WriteLine($"{medida:F8}");
            Console.Write("Arredondando (três casas decimais): ");
            Console.WriteLine($"{medida:F3}");
            Console.Write("Separador decimal invariant culture: ");
            Console.WriteLine(medida.ToString("F3", CultureInfo.InvariantCulture));
        }
    }
}
