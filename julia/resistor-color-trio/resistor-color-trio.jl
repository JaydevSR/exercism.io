function label(colors)
    value = 0
    codes = Dict("black" => 0, 
        "brown" => 1, 
        "red" => 2, 
        "orange" => 3, 
        "yellow" => 4, 
        "green" => 5,
        "blue" => 6,
        "violet" => 7,
        "grey" => 8,
        "white" => 9)

    value = 10^(codes[colors[3]] + 1) * codes[colors[1]] + 10^(codes[colors[3]]) * codes[colors[2]]
    if value % 1000 == 0
        return "$(Int(value/1000)) kiloohms"
    else
        return "$value ohms"
    end
end


