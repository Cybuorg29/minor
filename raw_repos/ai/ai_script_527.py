def combinations(arr)
  arr.length.times do |i|
    arr.length.times do |j|
      if i != j
        print arr[i], arr[j]
      end
    end
  end 
end

combinations(['a', 'b', 'c'])