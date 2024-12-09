use strict;
use warnings;
use feature 'say';

my $dm = <>;
chomp($dm);
my @pos = split( '', $dm );

say @pos;

# 1. transform the compressed representation into long representation
my @disk;
my $block = 0;
for my $i ( 0 .. $#pos ) {
    if ( ( $i + 1 ) % 2 ) {
        for my $r ( 1 .. $pos[$i] ) {
            push( @disk, $block );
        }
        $block++;
    }
    else {
        for my $r ( 1 .. $pos[$i] ) {
            push( @disk, '.' );
        }
    }
}

# say @disk;

# 2. move blocks from right to empty blocks in left
# two indices (left and right)
#   take elements from right if they are not '.'
#   search first . from left and swap
#   repeat until left=right;

my $left  = 0;
my $right = $#disk;

while ( $right > $left ) {
    my $blkToMove;
    my $toLoc;
    do {
        $blkToMove = $disk[$right];
        $right--;
    } while ( $blkToMove eq '.' );

    do {
        $toLoc = $disk[$left];
        $left++;
    } while ( $toLoc ne '.' );

    if ( $right >= $left ) {
        @disk[ $left - 1, $right + 1 ] = @disk[ $right + 1, $left - 1 ];
    }
}

# 3. compute checksum
my $part1 = 0;
for ( my $c = 0 ; $c <= $#disk ; $c++ ) {
    if ( $disk[$c] ne '.' ) {
        $part1 += $c * $disk[$c];
    }
}
say "Part 1: $part1";
