"""
Basic class in JavaScript with a constructor, a method for changing the greeting and a method for saying the greeting
"""

class GreetingGenerator {
  constructor(greeting) {
    this.greeting = greeting
  }

  setGreeting(greeting) {
    this.greeting = greeting
  }

  sayGreeting() {
    console.log(this.greeting)
  }
}

const greet = new GreetingGenerator('Hello World!')
greet.setGreeting('Good Morning!')
greet.sayGreeting() // 'Good Morning!'