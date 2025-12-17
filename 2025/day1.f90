program day1
        implicit none
        integer :: pos = 50, part1 = 0, part2 = 0
        integer :: delta, full, ios=0, rem, valor
        integer, parameter :: MY_MOD = 100
        character(len=4) :: line 

        do while (ios==0)
                read(5,*, iostat=ios) line
                if (ios /= 0) exit

                read(line(2:) ,*) valor
                delta = valor * merge(1, -1, line(1:1)=='R')
                
                full = abs(delta)/ MY_MOD
                rem = mod(delta, MY_MOD)
                part2 = part2 + full + merge(1,0, (pos + rem >= MY_MOD) .or. &
                        (pos + rem <= 0 .and. pos /= 0))
                pos = mod(pos + delta, MY_MOD) 
                if (pos < 0) pos = pos + MY_MOD
                if (pos == 0 ) part1 = part1 + 1
        end do

        print *, "Part 1:" ,part1
        print *, "Part 2:", part2 
end program day1
