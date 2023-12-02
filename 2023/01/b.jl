function processa_linha(line, nums, renums)
    rline = reverse(line)
    ff = line[findfirst(Regex(renums), line)]
    fl = reverse(rline[findfirst(Regex(reverse(renums)), rline)])
    d = (findfirst(item -> item == ff, nums) - 1) % 10
    u = (findfirst(item -> item == fl, nums) - 1) % 10

    return d * 10 + u
end

function parta()
    lines = readlines(Base.source_dir() * "/input")
	nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    renums = "0|1|2|3|4|5|6|7|8|9"
    total = 0
    for line in lines
        total += processa_linha(line, nums, renums)
    end
    println("-- Total A ", total)
end

function partb()
    lines = readlines(Base.source_dir() * "/input")
	nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]
    renums = "0|1|2|3|4|5|6|7|8|9|zero|one|two|three|four|five|six|seven|eight|nine"
    total = 0
    for line in lines
        total += processa_linha(line, nums, renums)
    end
    println("-- Total B ", total)
end

parta()
partb()