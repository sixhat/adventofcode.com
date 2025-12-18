#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long is_repeating_digits_twice(long id)
{
        char str[24];
        snprintf(str, 24, "%ld", id);
        size_t str_length = strlen(str);

        if (0 != str_length % 2)
        {
                return 0;
        }
        size_t len = str_length / 2;
        for (size_t i = len; i < str_length; i++)
        {
                if (str[i] != str[i - len])
                {
                        return 0;
                }
        }

        return id;
}

long is_repeating_digits_multiple_times(long id)
{
        char str[24];
        snprintf(str, 24, "%ld", id);
        size_t str_length = strlen(str);

        for (size_t len = 1; len <= str_length / 2; len++)
        {
                if (str_length % len != 0)
                {
                        continue;
                }
                int ok = 1;
                for (size_t i = len; i < str_length; i++)
                {
                        if (str[i] != str[i % len])
                        {
                                ok = 0;
                                break;
                        }
                }
                if (ok)
                {
                        return id;
                }
        }
        return 0;
}

int main(void)
{
        long lower_bound;
        long upper_bound;

        long total1 = 0, total2 = 0;

        while (scanf("%ld-%ld,", &lower_bound, &upper_bound) == 2)
        {
                for (long i = lower_bound; i <= upper_bound; i++)
                {
                        total1 += is_repeating_digits_twice(i);
                        total2 += is_repeating_digits_multiple_times(i);
                }
        }
        printf("Part 1: %ld\nPart 2: %ld\n", total1, total2);
        return 0;
}
