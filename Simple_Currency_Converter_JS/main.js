const listCurrencies = ["usd", "jpy", "eur", "rub", "gbp"];
console.log("Welcome to Currency Converter!");
console.log("1 USD equals 1 USD");
console.log("1 USD equals 113.5 JPY");
console.log("1 USD equals 0.89 EUR");
console.log("1 USD equals 74.36 RUB");
console.log("1 USD equals 0.75 GBP");

function convertCurrency(from, to, amount) {
    let jpy = 113.5;
    let eur = 0.89;
    let rub = 74.36;
    let gbp = 0.75;
    let exchangeRate = 0;
    switch (from) {
        case "usd":
            exchangeRate = 1;
            break;
        case "jpy":
            exchangeRate = jpy;
            break;
        case "eur":
            exchangeRate = eur;
            break;
        case "rub":
            exchangeRate = rub;
            break;
        case "gbp":
            exchangeRate = gbp;
            break;
        default:
            console.log("Invalid from currency");
            return;
    }
    let amountInDollar = amount / exchangeRate;
    switch (to) {
        case "jpy":
            exchangeRate = jpy;
            break;
        case "eur":
            exchangeRate = eur;
            break;
        case "rub":
            exchangeRate = rub;
            break;
        case "gbp":
            exchangeRate = gbp;
            break;
        case "usd":
            exchangeRate = 1;
            break;
        default:
            console.log("Invalid to currency");
            return;
    }
    let convertedAmount = amountInDollar * exchangeRate;
    let fromCur = from.toUpperCase()
    let toCur = to.toUpperCase()
    console.log(`Result: ${amount} ${fromCur} equals ${convertedAmount.toFixed(4)} ${toCur}`);
    return true;
}

function askAmount() {

    while (true) {
        let userAmount = prompt("Amount: ");
        if (/^[-\d]+$/.test(userAmount)) {
            if (userAmount >= 1) {
                return userAmount;
            } else {
                console.log("The amount cannot be less than 1");
            }
        } else {
            console.log("The amount has to be a number");
        }
    }

}

function askFrom (listCurrencies) {
    while (true) {
        console.log("What do you want to convert?");
        let userCurrencyFrom = prompt("From: ");
        if (listCurrencies.includes(userCurrencyFrom.toLowerCase())) {
            return userCurrencyFrom;
        } else {
            console.log("Unknown currency")
        }
    }
}

function askTo (listCurrencies) {
    while (true) {
        let userCurrencyTo = prompt("To: ");
        if (listCurrencies.includes(userCurrencyTo.toLowerCase())) {
            return userCurrencyTo;
        } else {
            console.log("Unknown currency")
        }
    }
}



while (true) {
    console.log("What do you want to do?\n1-Convert currencies 2-Exit program");
    let mainAsk = prompt();
    let mainAskInt = parseInt(mainAsk);
    if (mainAskInt === 1) {
        convertCurrency(askFrom(listCurrencies).toLowerCase(), askTo(listCurrencies).toLowerCase(), askAmount());
    } else if (mainAskInt === 2) {
        console.log("Have a nice day!");
        break;
    } else {
        console.log("Unknown prompt");
    }
}
