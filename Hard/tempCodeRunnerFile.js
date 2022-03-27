    let [val, freq] = this.stack.get(this.maxFreq);
    if (freq === 1) {
      this.stack.delete(this.maxFreq);
      this.hash.delete(val);
      this.maxFreq--;
    } else {
      this.hash.set(val, freq - 1);
      this.stack.set(val, [val, freq - 1]);
    }