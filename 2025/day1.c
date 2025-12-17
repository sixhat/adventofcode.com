#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MOD 100
int wrap_by_remainder(int pos, int rem)
{
        return (pos + rem > MOD - 1) || (pos + rem <= 0 && pos != 0);
}
int main(void)
{
        char line[8];
        int pos = 50;
        int part1 = 0;
        int part2 = 0;
        while (fgets(line, sizeof line, stdin))
        {
                int value = atoi(line + 1);
                int delta = (line[0] == 'L') ? -value : value;
                int full = abs(delta) / MOD;
                int rem = delta % MOD;
                part2 += full + wrap_by_remainder(pos, rem);
                pos = (pos + delta) % MOD;
                if (pos < 0)
                        pos += MOD;
                part1 += (pos == 0);
        }
        printf("Part 1: %d\n", part1);
        printf("Part 2: %d\n", part2);
        return 0;
}
