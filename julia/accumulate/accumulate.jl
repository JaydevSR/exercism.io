function accumulate(arr::AbstractArray, oper)
    return broadcast(oper, arr, arr)
end