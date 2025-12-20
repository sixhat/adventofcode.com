program day3
        implicit none
        integer, parameter :: ik8 = selected_int_kind(18)
        integer(kind=ik8) :: total1, total2
        character(len=128) :: line
        integer ios

        total1 = 0_ik8
        total2 = 0_ik8
        ios = 0
        do
                read (*, '(A)', iostat=ios) line
                if (ios /= 0) exit
                total1 = total1 + jolt(trim(line), "", 2)
                total2 = total2 + jolt(trim(line), "", 12)
        end do
        print *, "Part 1:", total1
        print *, "Part 2:", total2

contains
        recursive function jolt(bank, current, n) result(zut)
                implicit none
                character(len=*), intent(in) :: bank, current
                integer, intent(in) :: n !number of digits to select
                integer :: ni, i, ios, limit
                integer(kind=ik8) :: zut

                if (n == 0) then
                        read (current, *, iostat=ios) zut
                        if (ios /= 0) stop "Error, could not read current and assign to zut"
                        return
                end if
                ni = 1

                ! We can do this comparisson without converting to integers
                ! because comparing [0-9] in ASCII gives the same result
                limit = len(bank) - n + 1
                do i = 1, limit
                        if (bank(i:i) > bank(ni:ni)) ni = i
                end do

                zut = jolt(bank(ni + 1:), current//bank(ni:ni), n - 1)
        end function jolt
end program day3
