# https://adventofcode.com/2022/day/3
# This solution takes advantage of Set operations (namely intersect)

function naif_parte1(lines)
    # Part 1
    iSoma = 0
    for line in lines
        iMeio::Int = length(line) / 2
        sLeft = Set(line[1:iMeio])
        sRight = Set(line[(iMeio + 1):(2 * iMeio)])
        lSet = intersect(sLeft, sRight)
        letter = Int(first(lSet))
        letter -= letter > 94 ? 96 : 38
        iSoma += letter
    end
    println(iSoma)
end

function naif_parte2(lines)
    # Part 2 (each elf group is made of 3 lines of strings)
    iSoma2 = 0
    for i = 1:3:length(lines)
        s1 = Set(lines[i])
        s2 = Set(lines[i + 1])
        s3 = Set(lines[i + 2])
        lSet = intersect(s1, s2, s3)
        letter = Int(first(lSet))
        letter -= letter > 94 ? 96 : 38
        iSoma2 += letter
    end
    println(iSoma2)
end

function compara_2(a, b)
    for i in a, j in b
        if i == j
            l = Int(i)
            l -= l > 94 ? 96 : 38
            return l
        end
    end
    return 0
end

function compara_3(a, b, c)
    for i in a, j in b
        if i == j
            for k in c
                if i == k
                    l = Int(i)
                    l -= l > 94 ? 96 : 38
                    return l
                end
            end
        end
    end
    return 0
end

function parte1(lines)
    soma = 0
    for l in lines
        meio::Int = length(l) / 2
        @views soma += compara_2(l[1:meio], l[(meio + 1):end])
    end
    println(soma)
end

function parte2(lines)
    soma = 0
    for l = 1:3:length(lines)
        @views soma += compara_3(lines[l], lines[l + 1], lines[l + 2])
    end
    println(soma)
end



lines = readlines("input.data")
println("-------------------- Naif - Utiliza Sets")
@time naif_parte1(lines)
@time naif_parte1(lines)

println("-------------------- Rápido - menos alocações de memória ")
@time parte1(lines)
@time parte1(lines)

println("-------------------- Naif - Interseta Sets")
@time naif_parte2(lines)
@time naif_parte2(lines)

println("-------------------- Rápido - menos alocações")
@time parte2(lines)
@time parte2(lines)
