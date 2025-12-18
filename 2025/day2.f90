program day2
    implicit none
    integer , parameter :: ik8 = selected_int_kind(18)
    integer(kind=ik8) :: lower_bound, upper_bound, total1, total2, i
    integer :: ios, pos, comma, dash
    character(516) :: line
    character(44):: token


    total1 = 0
    total2 = 0
    ios = 0
    read(5, '(A)', iostat=ios) line
    if (ios/=0) stop "Error at input"

    ios = 0
    pos = 1

    do 
    comma = index(line(pos:), ',')
    if (comma == 0) then
        token = line(pos:)
    else
        token =line(pos:pos+comma-2)
        pos = pos + comma
    end if

    dash = index(token, '-')
    read(token(:dash-1), *, iostat=ios) lower_bound
    read(token(dash+1:), *) upper_bound

    do i = lower_bound, upper_bound
        total1 = total1 + is_repeating_digits_twice(i)
        total2 = total2 + is_repeating_digits_multiple_tiemes(i)
    end do

    if (comma == 0) exit
    end do

    print *, "Part 1:", total1
    print *, "Part 2:", total2
contains
    integer(kind=ik8) function is_repeating_digits_twice(n)
        implicit none
        integer(kind=ik8), intent(in)::n
        integer(kind=ik8) :: i
        character(len=24) :: str
        integer ::s_n, s_n2

        s_n = int(log10(real(n)))+1

        if (modulo(s_n, 2) /= 0) then
            is_repeating_digits_twice = 0
            return
        end if
        s_n2 = s_n / 2
        
        write(str, '(I0)') n

        do i = s_n2+1, s_n
            if (str(i:i) /= str(i-s_n2:i-s_n2)) then
                !print *, ">>> ", i, s_n, s_n2, str(i:i) , str(i-s_n2:i-s_n2)
                is_repeating_digits_twice = 0
                RETURN
            end if
        end do 

        is_repeating_digits_twice = n
    end function is_repeating_digits_twice
    
    integer(kind=ik8) function is_repeating_digits_multiple_tiemes(n)
        implicit none

        integer(kind=ik8), intent(in)::n
        integer(kind=ik8) :: i, j
        character(len=24) :: str
        integer(kind=ik8) ::s_n, s_n2
        logical :: ok
         
        s_n = int(log10(real(n)))+1
        write(str, '(I0)') n

        do i=1, s_n / 2
            if (modulo(s_n, i) /= 0) cycle
            ok = .true.
            do j = i+1, s_n
                if (str(j:j) /= str(1+modulo(j-1,i):1+modulo(j-1,i))) then
                    ok = .false.
                    exit
                end if
            end do
            if (ok) then
                is_repeating_digits_multiple_tiemes = n
                return
            end if
        end do

        is_repeating_digits_multiple_tiemes = 0
    end function is_repeating_digits_multiple_tiemes

end program day2

