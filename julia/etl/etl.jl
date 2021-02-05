function transform(input::AbstractDict)
    newdata = Dict()
    for (score, letters) in pairs(input)
        for letter in letters
            newdata[lowercase(letter)] = score
        end
    end
    newdata
end

