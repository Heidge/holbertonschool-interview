int is_palindrome(unsigned long n)
{
	unsigned int nb = n;
	unsigned int inverse = 0;

    while (nombre > 0) {
        inverse = inverse * 10 + nombre % 10;
        nombre = nombre / 10;
    }

    if (n == inverse)
        return 1;
    else
        return 0;

}