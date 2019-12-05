using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GOST
{
    class Program
    {
        static void Main(string[] args)
        {
            string message = "Test maessage";
            Hasher hasher = new Hasher();
            string hashCode = hasher.GetHashStringFormat(Encoding.ASCII.GetBytes(message), true);
            Console.WriteLine(hashCode);

            Console.ReadKey();
        }
    }
}
