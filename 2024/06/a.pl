# NOT CORRECT, YET... OR EVER,...  
# Tried to check for right previous paths, but this only gives
# partial results
# Thought about brutforcing all elements of previous path and check
# which lead to loops.
# best way probably is to brute force it and place the #
# in all available locations.
# And keep track of $seen grid elements.
# FAIL SKILL ISSUES.
use strict;
use warnings;
use feature 'say';
use List::Util qw(max );
my @in;

my $row = -1;
my $col = -1;
while ( my $line = <> ) {
    chomp($line);
    push( @in, $line );

    $row++ if $col == -1;
    $col = max( $col, index( $line, "^" ) );
}

sub print_map {
    say "";
    for my $line (@in) {
        say $line;
    }
}

# row, col -> N,E,S,W
my @direction = ( [ -1, 0 ], [ 0, 1 ], [ 1, 0 ], [ 0, -1 ] );
my @pos       = ( $row, $col );
my $dir       = 0;
my $obstacle  = 0;
my @obs;


sub move {
    # put an X at current pos
    substr( @in[ $pos[0] ], $pos[1], 1, "$dir" );

    # try to move in the current direction.
    my @nPos =
      ( $direction[$dir][0] + $pos[0], $direction[$dir][1] + $pos[1] );
    my @rPos = (
        $direction[ ( $dir + 1 ) % 4 ][0] + $pos[0],
        $direction[ ( $dir + 1 ) % 4 ][1] + $pos[1]
    );

    # if move to out of board return 0
    if (   $nPos[0] < 0
        || $nPos[1] < 0
        || $nPos[0] > $#in
        || $nPos[1] > $#in )
    {
        return 0;
    }



    if ( substr( @in[ $nPos[0] ], $nPos[1], 1 ) eq "#" ) {
        $dir = ( $dir + 1 ) % 4;
        @pos = @rPos;
        return 1;
    }

    @pos = @nPos;
    return 1;
}


my $steps =0;

while (move() ) {
    $steps++;
}
print_map();    # final map.

say "\nSTEPS: $steps";


my $count = 0;
for my $line (@in) {
    $count += $line =~ tr/0|1|2|3//;
}

say "Part 1: ", $count;
say $obstacle;
say "@obs";
