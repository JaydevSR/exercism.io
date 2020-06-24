function bob(stimulus::AbstractString)
    stimulus = strip(stimulus)
    allcaps(x) = (x == uppercase(x) && any(isuppercase, x))

    if allcaps(stimulus) && endswith(stimulus, '?')
        return "Calm down, I know what I'm doing!"
    elseif allcaps(stimulus)
        return "Whoa, chill out!"
    elseif endswith(stimulus, '?')
        return "Sure."
    elseif stimulus == ""
        return "Fine. Be that way!"
    else
        return "Whatever."
    end
end
