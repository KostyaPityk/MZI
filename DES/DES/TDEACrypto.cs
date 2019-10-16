using System;
using System.Collections.Generic;
using System.Text;

namespace DES
{
    public class TDEACrypto
    {

        private static readonly DESCrypto _DES = new DESCrypto();

        public string Encode(string inputString, string key)
        {
            var encodedText = _DES.Encode(inputString, key);
            encodedText = _DES.Encode(encodedText, key);
            encodedText = _DES.Encode(encodedText, key);
            return encodedText;
        }

        public string Encode(string inputString, string key1, string key2)
        {
            var encodedText = _DES.Encode(inputString, key1);
            encodedText = _DES.Encode(encodedText, key2);
            encodedText = _DES.Encode(encodedText, key1);
            return encodedText;
        }

        public string Encode(string inputString, string key1, string key2, string key3)
        {
            string decodedText = _DES.Decode(inputString, key1);
            decodedText = _DES.Decode(inputString, key2);
            decodedText = _DES.Decode(inputString, key3);

            return decodedText;
        }
        public string Decode(string inputString, string key)
        {
            var encodedText = _DES.Decode(inputString, key);
            encodedText = _DES.Decode(encodedText, key);
            encodedText = _DES.Decode(encodedText, key);
            return encodedText;
        }

        public string Decode(string inputString, string key1, string key2)
        {
            var decodedText = _DES.Decode(inputString, key1);
            decodedText = _DES.Decode(decodedText, key2);
            decodedText = _DES.Decode(decodedText, key1);
            return decodedText;
        }

        public string Decode(string inputString, string key1, string key2, string key3)
        {
            string decodedText = _DES.Decode(inputString, key3);
            decodedText = _DES.Decode(inputString, key2);
            decodedText = _DES.Decode(inputString, key1);
            return decodedText;
        }
    }
}
