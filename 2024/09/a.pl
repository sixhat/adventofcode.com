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

my $left  = -1;
my $right = $#disk + 1;

while ( $right > $left ) {
    my $blkToMove;
    my $toLoc;
    do {
        $right--;
        $blkToMove = $disk[$right];
    } while ( $blkToMove eq '.' );

    do {
        $left++;
        $toLoc = $disk[$left];
    } while ( $toLoc ne '.' );

    if ( $right >= $left ) {
        @disk[ $left, $right ] = @disk[ $right, $left ];
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
