package day14;

# https://adventofcode.com/2024/day/14

use strict;
use warnings;
use feature 'say';
use Readonly;
use Carp;

Readonly::Scalar my $dimX => 101;
Readonly::Scalar my $dimY => 103;

my $mx = int( $dimX / 2 );
my $my = int( $dimY / 2 );



my @fich;
open my $FH, '<', 'input' or cloak $!;
while (<$FH>) {
    my $l = $_;
    push( @fich, $l );
}
close($FH);

# say @fich;

my $minv = 227286000;
my $iter = 0;
# my @pos;

for my $i (1..11000 ) {
    my $SEGUNDOS = $i;
    my ( $q1, $q2, $q3, $q4 ) = ( 0, 0, 0, 0 );

    for my $robot (@fich) {
        chomp($robot);

        # say $robot;

        if ( $robot =~ m{p=(\d+),(\d+)[\N{SPACE}]+v=(-?\d+),(-?\d+)}xms ) {
            my ( $px, $py, $vx, $vy ) = ( $1, $2, $3, $4 );
            my $incx = ( $SEGUNDOS * $vx );
            my $incy = ( $SEGUNDOS * $vy );
            $px = ( $px + $incx ) % $dimX;
            $py = ( $py + $incy ) % $dimY;
            # push(@pos, [$py, $px]);
            $q1++ if ( $px < $mx && $py < $my );
            $q2++ if ( $px > $mx && $py < $my );
            $q3++ if ( $px > $mx && $py > $my );
            $q4++ if ( $px < $mx && $py > $my );
        }
    }
    my $qq = ($q1 + $q4) * ($q2 + $q3);

    say "$i\tSECS\t", $qq if $qq < 28_360;
    if ($qq < $minv){
        $minv = $qq;
        $iter = $i;
    }

}

say "$iter\t$minv";

    # for my $r (0..($dimY)){
    #     for my $c (0..($dimX)){
    #         my $out = ' ';
    #         for my $el (@pos){
    #             if (@$el[0] == $r && @$el[1] == $c){
    #                 $out = 'X';
    #             }
    #         }
    #         print $out;
    #     }
    #     print "\n";
    # }

1;

