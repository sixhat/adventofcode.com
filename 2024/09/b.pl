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

say "\t\t", @disk;

# 2. move entire files from right to empty blocks in left
# two indices (left and right)
#   take elements from right if they are not '.'
#   search first . from left and swap
#   repeat until left=right;
# 2333133121414131402
# 00...111...2...333.44.5555.6666.777.888899
# use the compressed representation? and extract

sub defrag {

    my $right = $_[0];

    # say $right;
    my $blkToMove;
    my $toLoc;
    do {
        $right--;
        $blkToMove = $disk[$right];
    } while ( $blkToMove eq '.' );

    my $count = 1;
    while ( $disk[ $right - 1 ] eq $blkToMove ) {
        $right--;
        $count++;
    }

    # Now we have the count and the index of the file.
    my $nDots = 0;
    my $left  = -1;
    for my $l ( 0 .. $right ) {
        if ( $disk[$l] eq '.' ) {
            $nDots++;
            if ( $nDots == $count ) {
                $left = $l - $count + 1;
                @disk[
                  ( $left .. ( $left + $nDots - 1 ) ),
                  ( $right .. ( $right + $count - 1 ) )
                  ]
                  = @disk[
                  ( $right .. ( $right + $count - 1 ) ),
                  ( $left .. ( $left + $nDots - 1 ) )
                  ];

                # say $left,'-',$nDots,'/',$right,'-',$count ,">\t",@disk;
                return $right;
            }
        }
        else {
            $nDots = 0;
        }
    }

    # say $left,'-',$nDots,'/',$right,'-',$count ,">\t",@disk;
    return $right;
}

my $r = $#disk + 1;
while ( $r >= 0 ) {
    $r = defrag($r);
}

# 3. compute checksum
my $part1 = 0;
for ( my $c = 0 ; $c <= $#disk ; $c++ ) {
    if ( $disk[$c] ne '.' ) {
        $part1 += $c * $disk[$c];
    }
}
say "Part 2: $part1";
