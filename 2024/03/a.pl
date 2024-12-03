use strict;
use warnings;

my $acc = 0;
while (my $line = <>) {
        my @matches = $line =~/mul\((\d{1,3}),(\d{1,3})\)/g;
        for (my $i = 0; $i < $#matches; $i = $i + 2){
                $acc += $matches[$i]*$matches[$i+1];
        }
}
print "Part 1: $acc \n";

