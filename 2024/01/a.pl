#!/usr/bin/env perl -W
use strict;
use warnings;

if ( $#ARGV + 1 != 1 ) {
    print "> Enter input data file's name!!! \n";
    exit;
}

open( my $in, "<", "$ARGV[0]" ) or die $!;

my @vec1;
my @vec2;

while ( my $line = <$in> ) {
    unless ( $line =~ /^\s$/ ) {
        my @nums = split( ' ', $line );
        push( @vec1, $nums[0] );
        push( @vec2, $nums[1] );
    }
}

@vec1 = sort @vec1;
@vec2 = sort @vec2;

my $distancia  = 0;
my $similarity = 0;
for my $i ( 0 .. $#vec1 ) {
    $distancia += abs( $vec1[$i] - $vec2[$i] );
    my $v2cnt = 0;
    foreach (@vec2) {
        if ( $vec1[$i] == $_ ) {
            $v2cnt++;
        }
    }
    $similarity += $vec1[$i] * $v2cnt;

}
print "Part 1: $distancia\n";
print "Part 2: $similarity\n";

