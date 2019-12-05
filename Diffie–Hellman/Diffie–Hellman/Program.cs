using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Diffie_Hellman
{
    class Program
    {
        static void Main(string[] args)
        {
            byte[] a_private = new byte[DiffieHellman.DH_KEY_LENGTH];
            byte[] b_private = new byte[DiffieHellman.DH_KEY_LENGTH];
            byte[] a_public = new byte[DiffieHellman.DH_KEY_LENGTH];
            byte[] b_public = new byte[DiffieHellman.DH_KEY_LENGTH];

            DiffieHellman.generate_key_pair(a_public, a_private);
            DiffieHellman.generate_key_pair(b_public, b_private);

            byte[] b_secret = DiffieHellman.generate_key_secret(b_private, a_public);
            foreach(var a in b_secret)
            {
                Console.Write(a);
            }

            Console.ReadLine();
        }
    }
}
