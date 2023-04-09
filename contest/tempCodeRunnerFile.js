  for (let i = 0; i < nums.length; i++) {
    if (!adj.has(nums[i])) {
      adj.set(nums[i], []);
    }
  }