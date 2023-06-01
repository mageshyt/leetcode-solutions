`2694. Event Emitter




subscribe('event_name', callback) 
can can use hash map to store the event name and callback function in a Array
{
    'event_name': [callback1, callback2]
}

emit('event_name', data)


`;

type Callback = (...args: any[]) => any;
type Subscription = {
  unsubscribe: () => void;
};

class EventEmitter {
  events: Map<string, Callback[]>;
  constructor() {
    this.events = new Map();
  }
  subscribe(eventName: string, callback: Callback): Subscription {
    // if no event name , then create a new array

    this.events.set(
      eventName,
      this.events.has(eventName)
        ? [...this.events.get(eventName), callback]
        : [callback]
    );

    return {
      unsubscribe: () => {
        // get the callback array
        const callbacks: any = this.events.get(eventName);

        // remove the callback from the array
        const index = callbacks.indexOf(callback);
        if (index > -1) {
          callbacks.splice(index, 1);
        }
      },
    };
  }

  emit(eventName: string, args: any[] = []): any {
    // if no event name , then return []
    if (!this.events.has(eventName)) return [];

    // get the callback array
    const callbacks: any = this.events.get(eventName);

    // call each callback
    const res: any = [];
    callbacks.forEach((callback: Callback) => {
      res.push(callback(...args));
    });
    return res;
  }
}

const emitter = new EventEmitter();

const step = ["EventEmitter", "emit", "subscribe", "subscribe", "emit"];

const data = [
  [],
  ["firstEvent"],
  [
    "firstEvent",
    function cb1() {
      return 5;
    },
  ],
  [
    "firstEvent",
    function cb1() {
      return 6;
    },
  ],
  ["firstEvent"],
];

step.forEach((step, index) => {
  if (step === "EventEmitter") {
    console.log("EventEmitter");
  } else if (step === "emit") {
    console.log("emit");
    emitter.emit(data[index][0]);
  } else if (step === "subscribe") {
    console.log("subscribe");
    emitter.subscribe(data[index][0], data[index][1]);
  }
});
console.log(emitter.events);
