`An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card ID equal to id, checks in at the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time it takes to travel from startStation to endStation.
The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

 

Example 1:

Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);  // Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12`;

class UndergroundSystem {
  constructor() {
    this.In = new Map();
    this.Out = new Map();
  }
  checkIn(id, StartingStation, startTime) {
    this.In.set(id, { StartingStation, startTime });
  }

  checkOut(id, station, t) {
    let data = this.In.get(id);
    this.In.delete(id);
    const stationPar = data.StartingStation + "-" + station;
    if (this.Out.has(stationPar)) {
      this.Out.get(stationPar).push(t - data.startTime);
    } else {
      this.Out.set(stationPar, [t - data.startTime]);
    }
  }

  getAverageTime(statingStation, endStation) {
    let totalTime = 0;
    let count = 0;
    let pair = statingStation + "-" + endStation;
    if (this.Out.has(pair)) {
      this.Out.get(pair).forEach((time) => {
        totalTime += time;
        count++;
      });
    }

    return totalTime / count;
  }
}

const solve = new UndergroundSystem();

solve.checkIn(45, "Leyton", 3);
solve.checkIn(32, "Paradise", 8);
solve.checkIn(27, "Leyton", 10);
solve.checkOut(45, "Waterloo", 15);
solve.checkOut(27, "Waterloo", 20);
solve.checkOut(32, "Cambridge", 22);
solve.getAverageTime("Paradise", "Cambridge");
solve.getAverageTime("Leyton", "Waterloo");
solve.checkIn(10, "Leyton", 24);
console.log(solve.getAverageTime("Leyton", "Waterloo"));

console.log(solve);
