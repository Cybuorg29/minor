import scala.io.Source

val products = Source.fromFile("products.txt").getLines.toList
val avgPrice = products.map(p => p.split(",")(4).toDouble).sum/products.length
println(s"The average price is: $avgPrice")