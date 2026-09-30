//class definition 
class Item { 
  constructor(cost, taxRate) { 
    this.cost = cost;
    this.taxRate = taxRate;
  }
  
  //calculate the cost including sales tax
  getCostWithTax() {
    return this.cost * (1 + this.taxRate);
  }
  
} 

//instantiate Item and calculate cost
let item = new Item(10, 0.1); 
let costWithTax = item.getCostWithTax();
console.log(costWithTax); //11