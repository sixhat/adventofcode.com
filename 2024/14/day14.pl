package day14;

# https://adventofcode.com/2024/day/14

use strict;
use warnings;
use feature 'say';
use Readonly;

Readonly::Scalar my $dimX     => 101;
Readonly::Scalar my $dimY     => 103;
Readonly::Scalar my $SEGUNDOS => 100;

my $mx = int( $dimX / 2 );
my $my = int( $dimY / 2 );

my ( $q1, $q2, $q3, $q4 ) = ( 0, 0, 0, 0 );

while ( my $robot = <> ) {
    chomp($robot);

    if ( $robot =~ m{p=(\d+),(\d+)[\N{SPACE}]+v=(-?\d+),(-?\d+)}xms ) {
        my ( $px, $py, $vx, $vy ) = ( $1, $2, $3, $4 );
        my $incx = ( $SEGUNDOS * $vx );
        my $incy = ( $SEGUNDOS * $vy );
        $px = ($px + $incx) % $dimX;
        $py = ($py + $incy) % $dimY;
        $q1++ if ( $px < $mx && $py < $my );
        $q2++ if ( $px > $mx && $py < $my );
        $q3++ if ( $px > $mx && $py > $my );
        $q4++ if ( $px < $mx && $py > $my );
    }
}

say "Part 1: ", $q1 * $q2 * $q3 * $q4;
1;