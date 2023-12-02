#include <stdio.h>
// #todo
int main()
{
    const char *file_name = "input";
    FILE *file = fopen(file_name, "r");
    char line[256];

    while (fgets(line, sizeof(line), file))
    {
        printf("%s", line);
    }

	fclose(file);
    return 0;
}