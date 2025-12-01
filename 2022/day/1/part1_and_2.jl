# Learning Julia using the Advent of code challenges:
# https://adventofcode.com/2022/day/1

## Parsing Command line arguments and trying to count the number of lines in file

function get_data()
    if length(ARGS) == 0
        println("> Data File not passed as parameter")
        println("> Using input.data as file")
        data_file = "input.data"
    else
        data_file = ARGS[1]
    end

    println("> $(countlines(data_file)) lines in $(data_file)")
    return data_file
end

## Processing DataFile

function process_data(fn)
    all_sums = []
    let suma = 0
        for line in eachline(fn)
            if line == ""
                push!(all_sums, suma)
                suma = 0
            else
                suma = suma + parse(Int, line)
            end
        end
    end
    sort!(all_sums, rev=true)
    return all_sums
end

## Print Results 

function print_result(res)
    println("Part 1 ", res[1])
    println("Part 2 ", sum(res[1:3]))
end

## Entry point

function main()
    file_name = get_data()
    results = process_data(file_name)
    print_result(results)
end

main()
