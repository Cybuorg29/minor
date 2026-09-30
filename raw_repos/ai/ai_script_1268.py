def search_array(arr, condition)
    arr.find { |item| condition.call(item) }
end