package Day13;

# https://adventofcode.com/2024/day/13

use strict;
use warnings;
use feature 'say';
use version; our $VERSION = qv(0.9.9);
use Math::Round;
use Readonly;
use Carp;

Readonly::Scalar my $EPSILON     => 0.001;
Readonly::Scalar my $PART2FACTOR => 10_000_000_000_000;

my ( $ax, $ay, $bx, $by, $px, $py );

sub _int {
    my $v = shift;
    return abs( $v - round($v) ) < $EPSILON;
}

my $result = 0;
my $p2     = 1;    # set to 1 for part 2
while ( my $line = <> ) {
    chomp $line;
    $px = 0;
    $py = 0;
    if ( $line =~
        m{Button[\N{SPACE}]+A:[\N{SPACE}]+X[+](\d+),[\N{SPACE}]+Y[+](\d+)}xms )
    {
        $ax = $1;
        $ay = $2;
    }
    if ( $line =~
        m{Button[\N{SPACE}]+B:[\N{SPACE}]+X[+](\d+),[\N{SPACE}]+Y[+](\d+)}xms )
    {
        $bx = $1;
        $by = $2;
    }
    if ( $line =~ m{Prize:[\N{SPACE}]+X=(\d+),[\N{SPACE}]+Y=(\d+)}xms ) {
        if ($p2) {
            $px = $1 + $PART2FACTOR;
            $py = $2 + $PART2FACTOR;
        }
        else {
            $px = $1;
            $py = $2;
        }
        my $m = ( ( $py - $px * $ay / $ax ) / ( $by - $bx * $ay / $ax ) );
        my $n = ( ( $px - $bx * $m ) / $ax );
        if ( _int($m) && _int($n) ) {
            $result += $n + $n + $n + $m;
        }
    }
}

say "\n\n> Result: $result" || croak 'died';
1;
