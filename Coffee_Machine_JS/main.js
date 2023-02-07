// Use "prompt()" to prompt a line from the user

function maxAmount(waterAmount, milkAmount, coffeeAmount) {
  let maxWater = waterAmount / 200;
  let maxMilk = milkAmount / 50;
  let maxCoffee = coffeeAmount / 15;
  return Math.min(Math.trunc(maxWater), Math.trunc(maxMilk), Math.trunc(maxCoffee));
}

class CoffeeCost {
  constructor(water, milk, coffee, money) {
    this.water = water;
    this.milk = milk;
    this.coffee = coffee;
    this.money = money;
  }
}
class CoffeeMachine {
  constructor() {
    this.water = 400;
    this.milk = 540;
    this.coffee = 120;
    this.cups = 9;
    this.money = 550;
    this.espresso = new CoffeeCost(250,0,16,4);
    this.latte = new CoffeeCost(350,75,20,7);
    this.cappuccino = new CoffeeCost(200,100,12,6);
  }

  show () {
    console.log(`The coffee machine has:
${this.water} ml of water
${this.milk} ml of milk
${this.coffee} g of coffee beans
${this.cups} disposable cups
$${this.money} of money`);
  }

  fillItems() {
    let askWater = prompt("Write how many ml of water you want to add: \n");
    let askMilk = prompt("Write how many ml of milk you want to add: \n");
    let askCoffee = prompt("Write how many grams of coffee beans you want to add: \n");
    let askCups = prompt("Write how many disposable cups you want to add: \n");
    let ansWater = parseInt(askWater);
    let ansMilk = parseInt(askMilk);
    let ansCoffee = parseInt(askCoffee);
    let ansCups = parseInt(askCups);

    this.water += ansWater;
    this.milk += ansMilk;
    this.coffee += ansCoffee;
    this.cups += ansCups;
    console.log("");
  }

  buyItem() {
    let ans = prompt("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino: \n")
    let ansInt = parseInt(ans);
    if (ansInt === 1) {
      if (this.water >= this.espresso.water) {
        if (this.coffee >= this.espresso.coffee) {
          if (this.cups >= 1) {
            this.water -= this.espresso.water;
            this.coffee -= this.espresso.coffee;
            this.cups -= 1;
            this.money += this.espresso.money;
            console.log("I have enough resources, making you a coffee!");

          } else {
            console.log("Sorry, not enough cups!");
          }
        } else {
          console.log("Sorry, not enough coffee!");
        }
      } else {
        console.log("Sorry, not enough water!");
      }
    } else if (ansInt === 2) {
      if (this.water >= this.latte.water) {
        if (this.milk >= this.latte.milk) {
          if (this.coffee >= this.latte.coffee) {
            if (this.cups >= 1) {
              this.water -= this.latte.water;
              this.milk -= this.latte.milk;
              this.coffee -= this.latte.coffee;
              this.cups -= 1;
              this.money += this.latte.money;
              console.log("I have enough resources, making you a coffee!");
            } else {
              console.log("Sorry, not enough cups!");
            }
          } else {
            console.log("Sorry, not enough coffee!");
          }
        } else {
          console.log("Sorry, not enough milk!");
        }
      } else {
        console.log("Sorry, not enough water!");
      }

    } else if (ansInt === 3) {
      if (this.water >= this.cappuccino.water) {
        if (this.milk >= this.cappuccino.milk) {
          if (this.coffee >= this.cappuccino.coffee) {
            if (this.cups >= 1) {
              this.water -= this.cappuccino.water;
              this.milk -= this.cappuccino.milk;
              this.coffee -= this.cappuccino.coffee;
              this.cups -= 1;
              this.money += this.cappuccino.money;
              console.log("I have enough resources, making you a coffee!");
            } else {
              console.log("Sorry, not enough cups!");
            }
          } else {
            console.log("Sorry, not enough coffee!");
          }
        } else {
          console.log("Sorry, not enough milk!");
        }
      } else {
        console.log("Sorry, not enough water!");
      }
    }
  }

  takeMoney() {
    console.log(`I gave you $${this.money}`);
    this.money = 0;

    console.log("");
  }

}

let coffeeMachine = new CoffeeMachine();

while (true) {
  let userAns = prompt("\nWrite action (buy, fill, take, remaining, exit): \n");
  if (userAns === 'buy') {
    coffeeMachine.buyItem();
  } else if (userAns === 'fill') {
    coffeeMachine.fillItems();
  } else if (userAns === 'take') {
    console.log("");
    coffeeMachine.takeMoney();
  } else if (userAns === 'remaining') {
    console.log("");
    coffeeMachine.show();
  } else if (userAns === 'exit') {
    break;
  }
}