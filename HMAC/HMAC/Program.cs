using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HMAC
{
    class Program
    {
        static void Main(string[] args)
        {
            const string message = "First Message";

            Console.WriteLine("HMAC");
            Console.WriteLine("----------------------------------");
            Console.WriteLine();

            var hMAC = new HMAC();
            var result = hMAC.Hmac(Encoding.UTF8.GetBytes(message));
            Console.WriteLine(Convert.ToBase64String(result));
            result = hMAC.Hmac(Encoding.UTF8.GetBytes((Convert.ToBase64String(result))));
            Console.WriteLine(Convert.ToBase64String(result));
            Console.ReadKey();
        }
    }
}
