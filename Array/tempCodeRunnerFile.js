    if (map.has(nums2[i])) {
      map.set(nums2[i], map.get(nums2[i]) - 1);
    } else {
      map.set(nums2[i], 1);
    }