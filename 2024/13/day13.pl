package Day13;

# https://adventofcode.com/2024/day/13

use strict;
use warnings;
use feature 'say';
my $ax;
my $ay;
my $bx;
my $by;
my $px;
my $py;

sub _int {
    my $v = shift;
    return abs( $v - int( $v + 0.5 ) ) < 0.0001;

    # return $v =~ /\d+/;
}

my $result = 0;
my $p2    = 1;    # set to 1 for part 2
while ( my $line = <> ) {
    chomp($line);
    $px = 0;
    $py = 0;

    if ( $line =~ m/Button A: X\+(\d+), Y\+(\d+)/ ) {
        $ax = $1;
        $ay = $2;
    }
    if ( $line =~ m/Button B: X\+(\d+), Y\+(\d+)/ ) {
        $bx = $1;
        $by = $2;
    }
    if ( $line =~ m/Prize: X=(\d+), Y=(\d+)/ ) {

        if ($p2) {
            $px = $1 + 10000000000000;
            $py = $2 + 10000000000000;
        }
        else {
            $px = $1;
            $py = $2;
        }

        print "\n$ax n + $bx m = $px\n";
        print "$ay n + $by m = $py\n";
        my $m = ( ( $py - $px * $ay / $ax ) / ( $by - $bx * $ay / $ax ) );
        my $n = ( ( $px - $bx * $m ) / $ax );
        say "m: ", $m;
        say "n: ", $n;

        if ( _int($m) && _int($n) ) {
            $result += 3 * $n + $m;
            say "----- Part 1: $result\n";
        }
    }
}

say "\n\n> Result: $result";
