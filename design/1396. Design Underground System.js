`
checkIn(int id, string stationName, int t) 
    - id: user id
    - stationName: station name
    - t: timestamp

checkOut(int id, string stationName, int t)
    - id: user id
    - stationName: station name
    - t: timestamp

getAverageTime(string startStation, string endStation)
    - startStation: start station name
    - endStation: end station name
    - return: average time from startStation to endStation


Logic :

we will have 2 maps
    - map1 : key = id, value = {stationName, t}
    - map2 : key = {startStation, endStation}, value = {totalTime, count}

`;
class UndergroundSystem {
  constructor() {
    this.userInfo = new Map(); // key = id, value = {stationName, t}
    this.StationInfo = new Map(); // key = {startStation, endStation}, value = {totalTime, count}
  }

  checkIn(id, stationName, t) {
    // one id can only check in once
    if (!this.userInfo.has(id)) {
      this.userInfo.set(id, { stationName, t });
    }
  }

  checkOut(id, stationName, t) {
    if (this.userInfo.has(id)) {
      // get the start station and time
      const { stationName: startStation, t: startTime } = this.userInfo.get(id);

      // get the key for map2
      const key = `${startStation}-${stationName}`;

      // get the value for map2
      const { totalTime = 0, count = 0 } = this.StationInfo.get(key) || {};

      // update the value for map2

      this.StationInfo.set(key, {
        totalTime: totalTime + t - startTime, // we add previous total time with current time
        count: count + 1, // we add previous count with 1
      });

      // delete the user from map1
      this.userInfo.delete(id);
    }
  }

  getAverageTime(startStation, endStation) {
    const { totalTime, count } =
      this.StationInfo.get(`${startStation}-${endStation}`) || {};

    return totalTime / count;
  }
}
