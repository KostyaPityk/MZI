using static System.Console;
using DES;

namespace DesConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            OutputEncoding = System.Text.Encoding.UTF8;

            string sentence = "BSUIR135";

            DESCrypto cipher = new DESCrypto();
            string key = "12345678";

            string encodedText = cipher.Encode(sentence, key);

            WriteLine($"Encode: {encodedText}");

            string decodedText = cipher.Decode(encodedText, key);

            WriteLine($"Decode: {decodedText}");

            ReadKey();
        }
    }
}
