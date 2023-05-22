const throttle = (fn, time) => {
  let isThrottled = false;
  let pendingCall = null;
  return (...args) => {
    if (isThrottled) {
      // wait
      pendingCall = args;
    } else {
      isThrottled = true;
      fn(...args);
      setTimeout(helper, time);
    }
  };

  function helper() {
    isThrottled = false;
    // check if there is any pending call
    if (pendingCall) {
      fn(...pendingCall);
      pendingCall = null;
      isThrottled = true;
      setTimeout(helper, time);
    }
  }
};
const throttled = throttle((a, b, c) => console.log(a + b + c), 1000);

throttled(1, 2, 3);

throttled(2, 3, 6);

throttled(4, 6, 8);
