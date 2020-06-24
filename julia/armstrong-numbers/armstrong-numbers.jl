function isarmstrong(number)
    digs = digits(number)
    sum(digs.^length(digs)) == number
end