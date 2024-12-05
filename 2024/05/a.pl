use strict;
use warnings;
use 5.010;
use experimental 'smartmatch';

my @rules;
my $rule  = 1;
my $part1 = 0;
my $part2 = 0;

sub is_valid {
    my @x = @_;
    for my $i ( 0 .. $#x ) {
        my $e = $x[$i];
        for my $j ( $i + 1 .. $#x ) {
            my $s = $e . '|' . $x[$j];
            unless ( $s ~~ @rules ) {
                return ( $i, $j );
            }
        }
    }
    return -1;
}

while ( my $line = <> ) {
    chomp($line);
    if ( $line eq "" ) {
        $rule = 0;
        next;
    }
    if ($rule) {
        push( @rules, $line );
        next;
    }

    my @x = split( /,/, $line );

    if ( is_valid(@x) == -1 ) {
        $part1 += $x[ $#x / 2 ];
    }
    else {
        while (1) {
            my (@el) = is_valid(@x);
            if ( $el[0] == -1 ) {
                last;
            }
            @x[ $el[0], $el[1] ] = @x[ $el[1], $el[0] ];
        }
        $part2 += $x[ $#x / 2 ];
    }
}
print "Part 1: ", $part1, "\n";
print "Part 2: ", $part2, "\n";
