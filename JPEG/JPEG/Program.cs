using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JPEG
{
    class Program
    {
        static void Main(string[] args)
        {
            Encode encode = new Encode();
            encode.EncodeImage("image.jpeg", "text.txt", "newImage.jpeg");

            encode.DecodeJPEG("newImage.jpeg", "textFromNewImage.txt");
        }
    }
}
