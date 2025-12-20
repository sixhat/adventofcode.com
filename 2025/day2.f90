program day2
        implicit none
        integer, parameter :: ik8 = selected_int_kind(18)
        integer(kind=ik8) :: lower_bound, upper_bound, total1, total2, i
        integer :: ios, pos, comma, dash
        character(len=516) :: buffer
        character(len=:), allocatable :: line
        character(len=:), allocatable :: token

        total1 = 0
        total2 = 0
        ios = 0
        read (5, '(A)', iostat=ios) buffer
        if (ios /= 0) stop "Error at input"
        line = trim(buffer)

        ios = 0
        pos = 1

        do
                comma = index(line(pos:), ',')
                if (comma == 0) then
                        token = line(pos:)
                else
                        token = line(pos:pos + comma - 2)
                        pos = pos + comma
                end if

                dash = index(token, '-')
                if (dash == 0) stop "Invalid range format"
                read (token(:dash - 1), *, iostat=ios) lower_bound
                if (ios /= 0) stop "Error reading lower bound"
                read (token(dash + 1:), *, iostat=ios) upper_bound
                if (ios /= 0) stop "Error reading upper bound"

                do i = lower_bound, upper_bound
                        if (is_repeating_digits_twice(i)) total1 = total1 + i
                        if (is_repeating_digits_multiple_times(i)) total2 = total2 + i
                end do

                if (comma == 0) exit
        end do

        print *, "Part 1:", total1
        print *, "Part 2:", total2
contains
        logical function is_repeating_digits_twice(n)
                implicit none
                integer(kind=ik8), intent(in)::n
                integer :: i
                character(len=24) :: str
                integer :: s_n, s_n2

                write (str, '(I0)') n
                s_n = len_trim(str)

                if (modulo(s_n, 2) /= 0) then
                        is_repeating_digits_twice = .false.
                        return
                end if
                s_n2 = s_n/2

                do i = s_n2 + 1, s_n
                        if (str(i:i) /= str(i - s_n2:i - s_n2)) then
                                is_repeating_digits_twice = .false.
                                return
                        end if
                end do

                is_repeating_digits_twice = .true.
        end function is_repeating_digits_twice

        logical function is_repeating_digits_multiple_times(n)
                implicit none

                integer(kind=ik8), intent(in)::n
                integer :: i, j
                character(len=24) :: str
                integer :: s_n
                logical :: ok

                write (str, '(I0)') n
                s_n = len_trim(str)

                do i = 1, s_n/2
                        if (modulo(s_n, i) /= 0) cycle
                        ok = .true.
                        do j = i + 1, s_n
                                if (str(j:j) /= str(1 + modulo(j - 1, i):1 + modulo(j - 1, i))) then
                                        ok = .false.
                                        exit
                                end if
                        end do
                        if (ok) then
                                is_repeating_digits_multiple_times = .true.
                                return
                        end if
                end do

                is_repeating_digits_multiple_times = .false.
        end function is_repeating_digits_multiple_times

end program day2

