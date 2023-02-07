// Use "prompt()" to prompt a line from the user
// Use "prompt(str)" to print some text before requesting prompt

let win = 'You survived!';
let lose = '\nYou lost!';
let wordsList = ["python","java", "swift", "javascript"];
let won = 0;
let lost = 0;
console.log("H A N G M A N");


function getRandomWord(listOfWords) {
  return listOfWords[Math.floor(Math.random() * listOfWords.length)];
}

function gameStart() {
  let selectedWord = getRandomWord(wordsList);
  let charsToKeep = '';
  let guessesAttempts = '';
  let attempts = 8;
  while (attempts > 0) {
    let lenWord = selectedWord.split("").filter((item, index, self) => self.indexOf(item) === index).join("").length;
    let lenUser = charsToKeep.split("").filter((item, index, self) => self.indexOf(item) === index).join("").length;

    if (lenUser === lenWord) {
      console.log(`\nYou guessed the word ${selectedWord}!\n` + win);
      won += 1;
      //attempts = 0;
      break;
    } else {
      let replacedWord = selectedWord.replace(new RegExp("[^" + charsToKeep + "]", "g"), "-");
      console.log("\n" + replacedWord);
      let askAnswer = prompt('prompt a letter: ');
      if (askAnswer.length === 1) {
        if (/^[a-z]$/.test(askAnswer)) {
          if (guessesAttempts.includes(askAnswer)) {
            console.log("You've already guessed this letter.");
          } else if (selectedWord.includes(askAnswer)) {
            charsToKeep += askAnswer;
            guessesAttempts += askAnswer;
          } else {
            console.log(`That letter doesn't appear in the word.`);
            guessesAttempts += askAnswer;
            attempts -= 1;
          }
        } else {
          console.log("Please, enter a lowercase letter from the English alphabet.");
        }
      } else {
        console.log("Please, prompt a single letter.");
      }
    }
  }


  if (attempts === 0) {
    console.log(lose);
    lost += 1;
  }
}

function scoreboardShow() {
  console.log(`You won: ${won} times.\nYou lost: ${lost} times.`);
}

while (true) {
  let askUser = prompt('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ');
  if (askUser === "play") {
    gameStart();
  } else if (askUser === "results") {
    scoreboardShow()

  } else if (askUser === "exit") {
    break;
  }
}
