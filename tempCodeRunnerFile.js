// // // let cat = Object.create({ type: "lion" });
// // // cat.size = "large";
// // // let copyCat = { ...cat };
// // // cat.type = "tiger";
// // // console.log(copyCat.type, copyCat.size);

// // // console.log("I");
// // // setTimeout(() => {
// // //   console.log("love");
// // // }, 0);
// // // console.log("JavaScript!");

// // let animals = ["jaguar", "eagle"];
// // //Missing Line
// // animals.reverse();
// // console.log(animals.pop()); //Prints jaguar

// // //How would you add a data item named animal with a value of sloth to local storage for the current domain?
// // localStorage.setItem("animal", "sloth");

// // What type of function can have its execution suspended and then resumed at a later point?
// // Generator function

// // var sound = "grunt";
// // var bear = { sound: "roar" };
// // function roar() {
// //   console.log(this.sound);
// // }

// // // let cat = { type: "tiger", size: "large" };
// // let json = JSON.stringify(cat, ["type"]);
// // console.log(json); //prints {"type": "tiger")

// // const foo = {
// //   bar() {
// //     console.log("Hello, world!");
// //   },
// //   name: "Albert",
// //   age: 26,
// // };

// // console.log("👉 foo.bar()", foo.bar());

// // var cat = { name: "Athena" };
// // function swap(feline) {
// //   feline.name = "Wild";
// //   feline = { name: "Tabby" };
// // }
// // swap(cat);
// // console.log(cat);

// //How can you attempt to access the property a . b on obj without throwing an error if a is undefined? let obj = {);
// // let obj = {};
// // console.log(obj?.a?.b);

// // What statement can be used to select the element from the DOM containing the text "The Linked Learning library has great JavaScript courses"
// // rom this markup?
// // <h1 class="content ">LinkedIn Learning</hi>
// // ‹div class="content">
// // <span class="content">The LinkedIn Learning library has great JavaScript courses!</span>
// // </div>

// // document.querySelector(".content span");

// // const dessert = { type: "pie" };
// // dessert.type = "pudding";
// // const seconds = dessert;
// // seconds.type = "fruit";

// // console.log("👉 dessert.type", dessert);

// const Arr = ["🍊", "🍏", "🍇", "🍌", "🍉"];

// const Arr2 = Arr.map((fruit) => fruit + "🍎");
// console.log("Map -->", Arr2);

// console.log();

// // filter

// const Arr3 = Arr.filter((fruit) => fruit != "🍌");

// console.log("Filter -->", Arr3);

// console.log();
// // reduce

// const Arr4 = Arr.reduce((acc, fruit) => acc + fruit, "🍎");

// console.log("Reduce -->", Arr4);

function getResult(x, y, flag) {
  return new Promise((resolve) => {
    setTimeout(() => {
      flag ? resolve(x ** y) : resolve(x * y);
    }, 2000);
  });
}

async function addFunc(x, flag) {
  let res = 0;
  for (let i = 1; i <= 3; i++) {
    res += await getResult(x, i, flag);
  }

  return res;
}

addFunc(10, true).then((res) => console.log(res));
addFunc(20, true).then((res) => console.log(res));
